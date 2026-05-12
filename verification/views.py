from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import login , logout ,authenticate

from verification.forms import Login_form, User_Edit_form


# Create your views here.
def login_user(request):
    if request.user.is_authenticated == True :
        return redirect('weblog:home')


    if request.method == 'POST' :
        form = Login_form(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('weblog:home')
    else:
        form = Login_form()
    return render(request ,'verification/index.html',{'form':form})



def logout_user(request):
    logout(request)
    return redirect('/')


def register_user(request):
    contact = {'Error':[]}
    if request.user.is_authenticated == True :
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password != password2:
            contact["Error"].append('Passwords is not matched')
            return render(request, 'verification/register.html', contact)
        user = User.objects.create(username=username,password=password,email=email)
        login(request, user)
        return redirect('/')

    return render(request, 'verification/register.html', {})

def user_edit(request):
    user = request.user
    form = User_Edit_form(instance=user)
    if request.method == "POST":
        form = User_Edit_form(data=request.POST,instance=user)
        if form.is_valid():
            form.save()

    return render(request,'verification/edit_user.html',{'form':form})
