from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.views.generic import DetailView, ListView, TemplateView, FormView, RedirectView, UpdateView, CreateView, \
    DeleteView

from verification.models import Profile
from .models import Article, Comment, Category, Input , Like
from .form import  Massage_form
from .mixin import Custom_Require_Mixin
from django.urls import reverse_lazy


# Create your views here.

#---------------------------------------------------------------------------------------------------------

def index(request):
    return render(request,'weblog/index.html')

#---------------------------------------------------------------------------------------------------------
def about(request):
    return render(request,'weblog/about.html')


#---------------------------------------------------------------------------------------------------------
#def contact(request):
 #   if request.method == 'POST':
#        form = Massage_form(data=request.POST)
#        if form.is_valid():
 #         #name = form.cleaned_data['name']
  #        #subject = form.cleaned_data['subject']
 #         #body = form.cleaned_data['body']
  #        #email = form.cleaned_data['email']
  #        #Input.objects.create(name=name,subject=subject , body=body, email=email)
   #         form.save(commit=True)

   # else:
   #         form = Massage_form()
   # return render(request,'weblog/contact.html',{"form":form})



#---------------------------------------------------------------------------------------------------------
#def detail(request ,slug):
 #   article = get_object_or_404(Article , slug =slug)
#    now = timezone.now()
#    if request.method == 'POST':
#        parent_id = request.POST.get('parent_id')
#        body = request.POST.get('body')

#        Comment.objects.create(body=body , article=article ,user=request.user,parent_id=parent_id)
#    return render(request,'weblog/post-details.html',{'article' : article,'now':now})


#---------------------------------------------------------------------------------------------------------
def blog_post(request):
    art = Article.objects.all().order_by('-create')
    page_number = request.GET.get('page')
    paginator = Paginator(art,3)
    objects_list = paginator.get_page(page_number)
    return render(request , 'weblog/blog.html',{'art':objects_list})


#---------------------------------------------------------------------------------------------------------
def post_partial(request):
    date = {'kamran':'kkk'}
    return render(request , 'weblog/include/post.html',context=date)

#---------------------------------------------------------------------------------------------------------
def category_detail(request , pk=None):
    category = get_object_or_404(Category , id=pk)
    articles = category.article_set.all()
    return render(request,'weblog/blog.html',{'art':articles})
#---------------------------------------------------------------------------------------------------------
def search_sidebar(request):
    s = request.GET.get('s')

    articles = Article.objects.filter(title__icontains=s)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    objects_list = paginator.get_page(page_number)
    return render(request ,'weblog/blog.html' ,{objects_list : 'art'})



#---------------------------------------------------------------------------------------------------------
class Detail(DetailView):
    model = Article
    template_name = 'weblog/post-details.html'
    #context_object_name = 'article'
    #slug_field = 'slug'
    #slug_url_kwarg = 'slug'      #هر چیزی بجز اسلاگ


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        if self.request.user.likes.filter(article__slug=self.object.slug , user_id=self.request.user.id).exists():
            context["is_liked"]=True
        else:
            context["is_liked"] =False

        return context



#---------------------------------------------------------------------------------------------------------
class Post_list(Custom_Require_Mixin,ListView):
    model = Article
    template_name = 'weblog/blog.html'
    context_object_name = 'art'
    paginate_by = 3
    queryset = Article.objects.order_by('-create')




#---------------------------------------------------------------------------------------------------------
class ContactUs(FormView):
    template_name = 'weblog/contact.html'
    form_class = Massage_form
    success_url = reverse_lazy("weblog:home")

    def form_valid(self, form):
        form_date = form.cleaned_data

        Input.objects.create(**form_date)
        return super().form_valid(form)

    """      0 == 1
    
   0 = Input.object.create(**form_date)
    
   1 = Input.objects.create(name=form_date['name'],subject=form_date['subject'],email=form_date['email'],body=form_date['body'])
    
    """


#---------------------------------------------------------------------------------------------------------
class Comment_View(CreateView):
    model = Comment
    fields = ['parent_id','body']
    template_name = 'weblog/post-details.html'



    def post(self, request, *args, **kwargs):
        self.object = Comment
        return super().post(request,parent_id='parent_id',body='body')



#---------------------------------------------------------------------------------------------------------
class Massage_List(ListView):
    model = Input
    template_name = 'crate.html'
    context_object_name = 'list'




#---------------------------------------------------------------------------------------------------------
class Massage_Update(UpdateView):
    model = Input
    fields = ('name','subject')
    template_name = 'edit.html'
    success_url = reverse_lazy('weblog:home')




#---------------------------------------------------------------------------------------------------------
class Massage_Delete(DeleteView):
    model = Input
    success_url = reverse_lazy('weblog:home')
#---------------------------------------------------------------------------------------------------------
class About(TemplateView):
    template_name = 'weblog/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.all()
        context['aaa'] = Article.objects.order_by('-create')
        return context

#---------------------------------------------------------------------------------------------------------




class Re_direct(RedirectView):
    pattern_name = 'weblog:home'
    permanent = False


#---------------------------------------------------------------------------------------------------------


def like(request,slug , pk):
    try:
        like = Like.objects.get(article__slug=slug ,user_id=request.user.id)
        like.delete()
        return JsonResponse({"response":'like'})

    except:
        Like.objects.create(article_id=pk ,user_id=request.user.id)


    return redirect('weblog:detail',slug)


#---------------------------------------------------------------------------------------------------------
