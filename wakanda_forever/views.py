from django.shortcuts import render
from .import models
from comment.models import Comment
from login import models as login_models
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def index(request):
    tags=models.Tag.object.all()
    articles=models.Article.object.all()

    if "username" in request.session.keys():
        username=request.session['username']
        request.session['login_state'] = 1
        login_state=request.session['login_state']
    else:
        username='游客'  
    return render(request,'wakanda_forever/index.html',locals())


def login(request):
    request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            #更多的其它验证.....
            try:
                user = login_models.User.object.get(name=username)
                request.session['username'] = username
                if user.password == password:
                   message='登陆成功,请留下您的评论' 
                   request.session['login_state'] = 1
                else:
                   message = "密码不正确！请重新输入"
            except:
                message = "用户名不存在！"
            request.session['message'] = message          
    return redirect(request.session['login_from'])

def article_id(request,article_id):
    article=models.Article.object.get(pk=article_id)
    
    if "login_state" in request.session.keys():
        username=request.session['username']
        login_state=request.session['login_state']
    else:
        username='游客'
        message='登陆后才能进行评论，请先登录' 
    
    comments=Comment.object.filter(content_type=article_id)  
    paginator = Paginator(comments, 5)
    page = request.GET.get('page')
    
    try:
        contacts = paginator.page(page) # contacts为Page对象！
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,'wakanda_forever/content.html',locals())
 



