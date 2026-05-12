from django.urls import path
from django.views.generic import ArchiveIndexView

from .models import Article
from .views import index, ContactUs, About, Re_direct, Detail, Post_list, Massage_Update, post_partial, search_sidebar, \
    category_detail, Massage_List , Massage_Delete , like

app_name ='weblog'
urlpatterns=[
    path('',index , name = 'home'),
    path('contact',ContactUs.as_view(),name='contact'),
    path('detail/<slug:slug>',Detail.as_view(),name='detail'),
    path('about',About.as_view(),name='about'),
    path('search/',search_sidebar ,name='search'),
    path('category/<int:pk>',category_detail,name='category_detail'),
    path('post',post_partial , name='post_partial'),
    path('redirect',Re_direct.as_view(),name='redirect'),
    path('blog-post',Post_list.as_view(),name='blog'),
    path('list',Massage_List.as_view(),name='list'),
    path('update/<int:pk>',Massage_Update.as_view(),name='edit'),
    path('Delete/<int:pk>',Massage_Delete.as_view(),name='delete'),
    path('archive',ArchiveIndexView.as_view(model=Article , date_field="pub_date"),name='article_archive'),
    path('like/<slug:slug>/<int:pk>',like,name='like'),
]