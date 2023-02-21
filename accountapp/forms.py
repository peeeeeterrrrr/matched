from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AccountUpdateForm(UserCreationForm):
    password1 = forms.CharField(
        label=("새 비밀번호"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=("* 8글자 이상 입력하세요 / 전과 다른 비밀번호를 사용하세요 / 비밀번호가 숫자로만 구성되지 않게 하세요"),
    )
    password2 = forms.CharField(
        label=("비밀번호 확인"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=("확인을 위해 비밀번호를 한번 더 입력해주세요."),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True

    class Meta:
        model = User
        fields = ("username",)
        labels={
            'username': '이름'
        }
        help_texts = {'username': (' 실명을 사용하세요 '), }