from django.views.generic import ListView, TemplateView

from accountapp.models import CustomUser


class HomeScreenView(TemplateView):
    template_name = 'homescreenapp/homescreen.html'


class UserGuideView(TemplateView):
    template_name = 'homescreenapp/userguide.html'


class ContactView(TemplateView):
    template_name = 'homescreenapp/contact.html'

class AboutUsView(TemplateView):
    template_name = 'homescreenapp/aboutus.html'

class TeacherEmployeeView(TemplateView):
    template_name = 'homescreenapp/teacheremployee.html'



