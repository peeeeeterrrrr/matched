from django.contrib.auth.models import User
from django.views.generic import ListView

from accountapp.models import CustomUser


class AnnouncementListView(ListView):
    model = CustomUser

    context_object_name = 'announcementlist'
    template_name = 'announcementapp/announcementbanner.html'

class AnnouncementDetailListView(ListView):
    model = CustomUser
    context_object_name = 'announcementlist'
    template_name = 'announcementapp/announcementbanner.html'