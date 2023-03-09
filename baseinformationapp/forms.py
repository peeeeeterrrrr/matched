from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from baseinformationapp.models import Baseinformation


class BaseinformationCreateForm(ModelForm):
    class Meta:
        model = Baseinformation
        fields = ('profileimage','sex', 'age', 'military', 'location', 'introduction')
        labels = {
            'profileimage':'프로필 사진',
            'sex': '성별',
            'age': '나이',
            'military':'병역사항',
            'location':'주소',
            'introduction':'자기소개',
        }

        widgets = {
            'profileimage': forms.FileInput(attrs={'placeholder': '프로필 이미지', 'class': 'InputfieldBox_Image'}),
            'age': forms.NumberInput(attrs={'placeholder': '나이', 'class': 'InputfieldBox'}),
            'sex': forms.Select(attrs={'placeholder': '성별', 'class': 'InputfieldBox'}),
            'military':forms.Select(attrs={'class': 'InputfieldBox'}),
            'location':forms.TextInput(attrs={'placeholder': '대전 oo구 oo동', 'class': 'InputfieldBox'}),
            'introduction':forms.Textarea(attrs={'placeholder': '자기소개', 'class': 'InputfieldBox_textarea'}),
        }

