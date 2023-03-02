from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField
from django import forms

from accountapp.models import CustomUser



class AccountLoginForm(AuthenticationForm):
    username = UsernameField(
        label=("아이디"),
        widget=forms.TextInput(attrs={
            'placeholder': '사용자 아이디',
            'class': 'InputfieldBox',
            'autofocus': True
        })
    )
    password = forms.CharField(
        label=("비밀번호"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': '사용자 아이디',
            'class': 'InputfieldBox',
            'autocomplete': 'current-password'
        })
    )

class AccountCreateForm(UserCreationForm):
    password1 = forms.CharField(
        label=("비밀번호"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': '영문/숫자/특수문자 혼합 8~20자',
            'class': 'InputfieldBox',
            'autocomplete': 'new-password',
        }),
    )

    password2 = forms.CharField(
        label=(""),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': "확인을 위해 위와 동일한 비밀번호를 입력해 주세요",
            'class': 'InputfieldBox',
            'autocomplete': 'new-password'
        }),
    )


    class Meta:
        model = CustomUser
        fields = ('username', 'userrealname', 'email', 'phone_number', 'password1', 'password2')
        labels = {
            'username': '아이디',
            'userrealname': '이름',
            'email': '이메일',
            'phone_number': '전화 번호',
        }

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': '10자 이하 사용자 아이디', 'class': 'InputfieldBox',}),
            'userrealname': forms.TextInput(attrs={'placeholder': '사용자 실명', 'class': 'InputfieldBox',}),
            'email': forms.EmailInput(attrs={'placeholder': '비밀번호 찾기를 위해 정확한 주소를 입력해 주세요', 'class': 'InputfieldBox',}),
            'phone_number': forms.TextInput(attrs={'placeholder': '알림 수신을 위해 정확한 전화 번호를 입력해 주세요','class': 'InputfieldBox',}),
        }




class AccountUpdateForm(UserCreationForm):
    password1 = forms.CharField(
        label=("비밀번호"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': '영문/숫자/특수문자 혼합 8~20자',
            'class': 'InputfieldBox',
            'autocomplete': 'new-password',
        }),
    )

    password2 = forms.CharField(
        label=(""),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': "확인을 위해 위와 동일한 비밀번호를 입력해 주세요",
            'class': 'InputfieldBox',
            'autocomplete': 'new-password'
        }),
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True
        self.fields['userrealname'].disabled = True
        self.fields['email'].disabled = True
        self.fields['phone_number'].disabled = True

    class Meta:
        model = CustomUser
        fields = ('username', 'userrealname', 'email', 'phone_number', 'password1', 'password2')
        labels = {
            'username': '아이디',
            'userrealname': '이름',
            'email': '이메일',
            'phone_number': '전화 번호',
        }

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': '10자 이하 사용자 아이디', 'class': 'InputfieldBox',}),
            'userrealname': forms.TextInput(attrs={'placeholder': '사용자 실명', 'class': 'InputfieldBox',}),
            'email': forms.EmailInput(attrs={'placeholder': '비밀번호 찾기를 위해 정확한 주소를 입력해 주세요', 'class': 'InputfieldBox',}),
            'phone_number': forms.TextInput(attrs={'placeholder': '-를 제외한 정확한 전화 번호를 입력해 주세요','class': 'InputfieldBox',}),
        }