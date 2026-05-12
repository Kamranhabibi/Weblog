from django.shortcuts import redirect


class Custom_Require_Mixin:
    def dispatch(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect('auth:login')
        return super(Custom_Require_Mixin,self).dispatch(request,*args,**kwargs)
