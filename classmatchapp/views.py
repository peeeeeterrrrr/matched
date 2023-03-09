from django.views.generic import TemplateView, DetailView

from accountapp.models import CustomUser


class MatchingListView(DetailView):
    model = CustomUser
    context_object_name = 'target_user'
    template_name = 'classmatchapp/matchinglist.html'

