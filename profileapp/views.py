from django.db.models import F
from django.views.generic import DetailView

from accountapp.models import CustomUser
from careerapp.models import Career
from scholarshipapp.models import Scholarship


class ProfileView(DetailView):
    model = CustomUser
    context_object_name = 'target_user'
    template_name = 'profileapp/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        career_list = Career.objects.filter(customuser=self.request.user).order_by(F('startdate').asc())
        scholarship_list = Scholarship.objects.filter(customuser=self.request.user).order_by(F('startdate').asc())
        context['career_list'] = career_list
        context['scholarship_list'] = scholarship_list
        return context