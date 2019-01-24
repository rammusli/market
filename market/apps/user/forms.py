from django import forms
from django_redis import get_redis_connection

from user.helper import set_password
from user.models import User


"""注册表单, 验证"""
class RegisterModelForm(forms.ModelForm):
    # 单独添加字段
    password1 = forms.CharField(max_length=16,
                                min_length=6,
                                error_messages={
                                    'required': '密码必填',
                                    'max_length': '密码长度不能大于32个字符',
                                    'min_length': '密码长度必须大于6个字符',
                                }
                                )
    password2 = forms.CharField(error_messages={'required': "确认密码必填"})

    #验证码
    captcha = forms.CharField(max_length=4,
                              error_messages={
                                  'required':'验证码必须填写'
                              })

    agree = forms.BooleanField(error_messages={'required':'须同意用户协议'})

    class Meta:
        model = User
        # 需要验证的字段
        fields = ['user_phone']

        error_messages = {
            "user_phone": {
                "required": "手机号码必须填写!"
            }
        }

    def clean_user_phone(self):
        # 验证手机号码是否唯一
        user_phone = self.cleaned_data.get('user_phone')
        rs = User.objects.filter(user_phone=user_phone).exists()  # 返回bool
        if rs:
            raise forms.ValidationError("手机号码已经被注册")
        return user_phone


    def clean(self):
        # 验证密码输入
        pwd1 = self.cleaned_data.get("password1")
        pwd2 = self.cleaned_data.get("password2")
        if pwd1 and pwd2 and pwd1 != pwd2:
            raise forms.ValidationError({'pwd2':'两次输入代码不一致'})

        # 验证验证码输入
        try:
            captcha = self.cleaned_data.get('captcha')

            # redis保存
            user_phone = self.cleaned_data.get('user_phone', '')
            # 获取redis中的
            r = get_redis_connection("default")
            random_code = r.get(user_phone)  # 二进制, 转码
            random_code = random_code.decode('utf-8')
            if captcha and captcha != random_code:
                raise  forms.ValidationError({"captcha":"验证码输入错误"})
        except:
            raise forms.ValidationError({"captcha":"验证码输入错误"})
        return  self.cleaned_data




"""登录表单, 验证"""
class LoginModelForm(forms.ModelForm):
    password = forms.CharField(max_length=16,
                               min_length=8,
                               error_messages={
                                   'required': '密码必填',
                                   'max_length': '密码长度不能大于32个字符',
                                   'min_length': '密码长度必须大于6个字符',
                               })

    class Meta:
        model = User
        # 需要验证的字段
        fields = ['user_phone', ]

        error_messages = {
            "user_phone": {
                "required": "手机号码必须填写!"
            }
        }


    def clean(self):
        # 验证用户名
        user_phone = self.cleaned_data.get("user_phone")
        password = self.cleaned_data.get('password')
        # 到数据库去查询
        try:
            user = User.objects.get(user_phone=user_phone)
        except User.DoesNotExist:
            raise forms.ValidationError({"user_phone": "号码错误"})
        # 验证密码
        if user.user_password != set_password(password):
            raise forms.ValidationError({"password": "密码错误!"})
        self.cleaned_data['user'] = user
        return self.cleaned_data




