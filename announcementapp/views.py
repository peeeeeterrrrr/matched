from django.contrib.auth.models import User
from django.views.generic import ListView


class AnnouncementListView(ListView):
    model = User
    context_object_name = 'announcementlist'
    template_name = 'announcementapp/announcementbanner.html'