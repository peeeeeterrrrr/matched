from django.contrib.auth.models import User
from django.views.generic import ListView


class HomeScreenListView(ListView):
    model = User
    context_object_name = 'target_user'
    template_name = 'homescreenapp/homescreen.html'
