from django.views.generic import DetailView

from accountapp.models import CustomUser


class MyclassListView(DetailView):
    model = CustomUser
    context_object_name = 'target_user'
    template_name = 'studymanageapp/myclasslist.html'