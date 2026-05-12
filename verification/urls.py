from django.urls import path
from .views import login_user, logout_user, register_user, user_edit

app_name = 'auth'
urlpatterns = [
    path('login',login_user,name='login'),
    path('logout',logout_user,name='logout'),
    path('register',register_user,name='register'),
    path('edit',user_edit,name='edit')

]