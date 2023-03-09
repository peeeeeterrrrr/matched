from django import forms
from django.forms import DateInput, ModelForm
from django.utils.dateparse import parse_date

from careerapp.models import Career


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


class CareerCreateForm(ModelForm):

    class Meta:
        model = Career
        fields = ('startdate','enddate','careercontent','careertype','careerinstitute')
        labels = {
            'startdate':'시작기간',
            'enddate':'종료기간 (지속중이면 공백)',
            'careercontent':'활동 내용',
            'careertype':'활동 구분',
            'careerinstitute':'기관 및 장소'
        }

        widgets = {
            'startdate':YearMonthWidget(attrs={'placeholder': '시작', 'class': 'InputfieldBox_date'}),
            'enddate':YearMonthWidget(attrs={'placeholder': '끝', 'class': 'InputfieldBox_date'}),
            'careercontent': forms.TextInput(attrs={'placeholder': '활동 내용', 'class': 'InputfieldBox'}),
            'careertype': forms.TextInput(attrs={'placeholder': '활동 구분', 'class': 'InputfieldBox'}),
            'careerinstitute': forms.TextInput(attrs={'placeholder': '기관 및 장소', 'class': 'InputfieldBox'}),
        }
