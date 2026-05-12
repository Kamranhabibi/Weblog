from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone


# default name in django doc : ** objects ** like be " Article.objects.all()
# Model Manege
#Choices=(
        #('a','LifeStyle'),
        #('b','Natures'),
        #('c','Others')
    #)
    #ctgory=models.CharField(choices=Choices ,default='c')
    # test =models.CharField(unique_for_date='pup_date') *** unique for date ,محدودیت برای ساخت روزانه

# Create your models here.

class Category(models.Model):
    title =models.CharField(max_length=50 ,unique=True ,verbose_name='عنوان')
    create =models.DateTimeField(auto_now_add=True,verbose_name='تاریخ انتشار')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title




class Article(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='نویسنده')
    title=models.CharField(max_length=70,help_text='Enter a valid title',unique=True , verbose_name='عنوان')
    category=models.ManyToManyField(Category,verbose_name='دسته بندی')
    image =models.ImageField(upload_to='articles',verbose_name='تصویر')
    body=models.TextField(verbose_name='شرح')
    create=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ساخت')
    update=models.DateTimeField(auto_now_add=True,verbose_name='بروزرسانی')
    status = models.BooleanField(default=True,verbose_name='وضعیت')
    published = models.BooleanField(default=True,null=True,verbose_name='وضعیت انتشار')

    pub_date = models.DateTimeField(default=timezone.now())

    slug = models.SlugField(blank=True , unique= True,verbose_name='برچسب')





    def save(
            self,*,force_insert=False,force_update=False,using=None,update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Article , self).save()


    def get_absolute_url(self):
        return reverse('weblog:detail',args=[self.slug])


    def __str__(self):
        return f"{self.title}-{self.body[:25]}"

    class Meta:
        ordering = ['update']
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'




class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE , related_name='comments',verbose_name='مرتبط با مقاله :')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments',verbose_name='حساب کاربری')

    parent = models.ForeignKey('self',on_delete=models.CASCADE,related_name='replies' , null=True , blank=True ,verbose_name='زیر مجموعه')

    body = models.TextField(verbose_name='نظر')
    create = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ انتشار')


    def __str__(self):
        return self.body[:35]

    class Meta:
        ordering = ['-create']
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'




class Input(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام')
    subject = models.CharField(verbose_name='موضوع')
    body = models.TextField(verbose_name='پیام')
    email = models.EmailField(null=True,blank=True,verbose_name='ایمیل')
    date = models.DateField(auto_now_add=True,verbose_name='تاریخ')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']
        verbose_name = 'پیام'
        verbose_name_plural = 'ارتباط باما'

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="likes",verbose_name='کاربر')
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name="likes",verbose_name="مقاله")
    create = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ")

    def __str__(self):
        return f"{self.user.username}-{self.article.title}"

    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'