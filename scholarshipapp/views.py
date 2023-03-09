from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.dateparse import parse_date
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from scholarshipapp.forms import ScholarshipCreateForm
from scholarshipapp.models import Scholarship


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ScholarshipCreateView(CreateView):
    model = Scholarship
    form_class = ScholarshipCreateForm
    template_name = 'scholarshipapp/create.html'
    success_url = reverse_lazy('homescreenapp:homescreen')



    def form_valid(self, form):
        temp_scholarship= form.save(commit = False)
        temp_scholarship.customuser = self.request.user
        temp_scholarship.save()
        return super().form_valid(form)


