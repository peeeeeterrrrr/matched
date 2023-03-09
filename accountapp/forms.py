
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField
from django import forms

from accountapp.models import CustomUser



class AccountLoginForm(AuthenticationForm):
    username = UsernameField(
        label=(""),
        widget=forms.TextInput(attrs={
            'placeholder': '전화번호',
            'class': 'InputfieldBox',
            'autofocus': True
        })
    )
    password = forms.CharField(
        label=(""),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': '비밀번호',
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
        fields = ('username', 'userrealname', 'email', 'password1', 'password2')
        labels = {
            'username': '전화번호',
            'userrealname': '이름',
            'email': '이메일',
        }

        widgets = {
            'username': forms.NumberInput(attrs={'placeholder': '- 제외 전화번호 11자','class': 'InputfieldBox',}),
            'userrealname': forms.TextInput(attrs={'placeholder': '사용자 실명', 'class': 'InputfieldBox',}),
            'email': forms.EmailInput(attrs={'placeholder': '비밀번호 찾기를 위해 정확한 주소를 입력해 주세요', 'class': 'InputfieldBox',}),
        }




class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True
        self.fields['userrealname'].disabled = True
        self.fields['email'].disabled = True
        self.fields['phone_number'].disabled = True
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
        fields = ('username', 'userrealname', 'email', 'password1', 'password2')
        labels = {
            'username': '전화번호',
            'userrealname': '이름',
            'email': '이메일',
        }

        widgets = {
            'username': forms.NumberInput(attrs={'placeholder': '- 제외 전화번호 11자','class': 'InputfieldBox',}),
            'userrealname': forms.TextInput(attrs={'placeholder': '사용자 실명', 'class': 'InputfieldBox',}),
            'email': forms.EmailInput(attrs={'placeholder': '비밀번호 찾기를 위해 정확한 주소를 입력해 주세요', 'class': 'InputfieldBox',}),
        }