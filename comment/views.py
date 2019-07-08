from django.shortcuts import render
from comment.models import Comment
from wakanda_forever.models import Article
from login.models import User

from django.forms import ModelChoiceField

from django.shortcuts import redirect



def up_comment(request):
    request.session['up_comment'] = request.META.get('HTTP_REFERER', '/')
    
    article_id=int(request.session['up_comment'][-1])
    content_type=Article.object.get(pk=article_id)
    
    username=request.session['username']
    print('会话信息：',request.session['username'])
    user = User.object.get(name=username)
    print('用户信息：',user)
    comment_text = request.POST.get('desc','')  
    comment=Comment()
    comment.user_id = user
    comment.text = comment_text
    comment.content_type=content_type
    comment.save()
    return redirect(request.session['up_comment'])
