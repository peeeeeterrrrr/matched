from django import forms
from django.forms import ModelForm, DateInput
from django.utils.dateparse import parse_date
from scholarshipapp.models import Scholarship



class YearMonthWidget(DateInput):
    format = '%Y-%m'
    input_type = 'month'

    def format_value(self, value):
        if value is None:
            return ''
        return value.strftime(self.format)

    def value_from_datadict(self, data, files, name):
        value = data.get(name)
        if value:
            return parse_date(value + '-01')
        return None

class ScholarshipCreateForm(ModelForm):

    class Meta:
        model = Scholarship
        fields = ('school', 'major', 'startdate','enddate' , 'state','schoolverificationimage')
        labels = {
            'school':'학교',
            'major':'전공',
            'startdate':'시작기간',
            'enddate':'종료기간 (지속중이면 공백)',
            'state':'구분',
            'schoolverificationimage':'재학 증명'
        }

        widgets = {
            'schoolverificationimage': forms.FileInput(attrs={'placeholder': '재학증명', 'class': 'InputfieldBox_Image'}),
            'school': forms.TextInput(attrs={'placeholder': 'oo대학교', 'class': 'InputfieldBox'}),
            'major': forms.TextInput(attrs={'placeholder': 'oo과', 'class': 'InputfieldBox'}),
            'startdate':YearMonthWidget(attrs={'placeholder': '시작', 'class': 'InputfieldBox_date'}),
            'enddate':YearMonthWidget(attrs={'placeholder': '끝', 'class': 'InputfieldBox_date'}),
            'state': forms.Select(attrs={'class': 'InputfieldBox'}),
        }
