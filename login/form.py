from django import forms
from django.forms import widgets

class register_form(forms.Form):
    username = forms.CharField(max_length=100,label='用户名',widget=widgets.TextInput
                               (attrs={'placeholder': '请输入用户名'}),)
    password = forms.CharField(widget=forms.PasswordInput
                    (attrs={'placeholder':u'请输入密码'})
                            ,label='密码')
    password2 = forms.CharField(widget=forms.PasswordInput
                                (attrs={'placeholder':u'与上面密码保持一致'})
                                ,label='确认密码')
    gender = (
            ('male', "男"),
            ('female', "女"),
             )
    email = forms.EmailField(required=False,label='邮箱',widget=widgets.TextInput
                               (attrs={'placeholder': '请输入邮箱'}))
    sex = forms.ChoiceField(choices=gender,required=True,label='性别')



class login_form(forms.Form):
    
    username = forms.CharField(max_length=100,label='用户名',widget=widgets.TextInput
                               (attrs={'placeholder': '请输入用户名'}),)
    password = forms.CharField(widget=forms.PasswordInput
                    (attrs={'placeholder':u'请输入密码'})
                            ,label='密码')