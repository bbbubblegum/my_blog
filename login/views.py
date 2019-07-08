from django.shortcuts import render,redirect
from . import models
from .form import register_form
from .form import login_form


def login(request):
    if request.method == "POST":
        form = login_form(request.POST) # form 包含提交的数据
        if form.is_valid():# 如果提交的数据合法
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = models.User.object.get(name=username)
                print(user)
                if user.password == password:
                    request.session['username']=username
                    return redirect('/')
                else:
                    message = "密码不正确！请重新输入"
            except:
                    message = "用户名不存在！"      
    elif  "login_state" in request.session.keys() :
        return redirect('/')
    else:
        username='游客'
        form = login_form()
        
    return render(request, 'login/login.html', locals())


def register(request):
    if request.method == 'POST':# 当提交表单时   
        form = register_form(request.POST) # form 包含提交的数据
        if form.is_valid():# 如果提交的数据合法
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']
            message = "请输入正确的信息" 
            if password!=password2:
                message = "确认密码不一致！请重新输入密码"
            else:
                try:
                    user = models.User.object.get(name=username)
                    print(user)
                    if user.name == username:
                        message = "用户名已存在！请重新输入用户名"
                except:
                    try:
                        user = models.User.object.get(email=email)
                        print(user)
                        message = "用户邮箱已存在！请重新输入邮箱地址"
                    except:
                        user = models.User()
                        user.name=username
                        user.password=password
                        user.email=email
                        user.save()
                        request.session['username']=username
                        return redirect('/')         
    elif  "login_state" in request.session.keys() :
        return redirect('/')
    else:
        username='游客'
        form = register_form()
        
    return render(request,'login/register.html',locals())

def logout(request):
    request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
    url=request.session['login_from']
    # 清除当前对应session所有数据
    request.session.clear()

    return redirect(url)
