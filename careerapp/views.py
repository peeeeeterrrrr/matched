from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from careerapp.forms import CareerCreateForm
from careerapp.models import Career
from scholarshipapp.forms import ScholarshipCreateForm


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class CareerCreateView(CreateView):
    model = Career
    form_class = CareerCreateForm
    template_name = 'careerapp/create.html'
    success_url = reverse_lazy('homescreenapp:homescreen')

    def form_valid(self, form):
        temp_career= form.save(commit = False)
        temp_career.customuser = self.request.user
        temp_career.save()
        return super().form_valid(form)