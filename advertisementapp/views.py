from django.contrib.auth.models import User
from django.views.generic import ListView


class AdvertisementListView(ListView):
    model = User
    context_object_name = 'advertisement_list'
    template_name = 'advertisementapp/advertisementbanner.html'