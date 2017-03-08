from django.views import generic
from .forms import UserProfileForm


class IndexView(generic.FormView):
    form_class = UserProfileForm
    template_name = 'demo_app/user-form.html'
