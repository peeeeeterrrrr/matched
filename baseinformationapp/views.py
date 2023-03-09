from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from baseinformationapp.forms import BaseinformationCreateForm
from baseinformationapp.models import Baseinformation


# Create your views here.
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class BaseinformationCreateView(CreateView):
    model = Baseinformation
    form_class = BaseinformationCreateForm
    template_name = 'baseinformationapp/create.html'
    success_url = reverse_lazy('homescreenapp:homescreen')

    def form_valid(self, form):
        temp_baseinformation= form.save(commit = False)
        temp_baseinformation.customuser = self.request.user
        temp_baseinformation.save()
        return super().form_valid(form)

