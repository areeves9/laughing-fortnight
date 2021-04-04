from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import UpdateView

from django.urls import reverse_lazy


from companies.forms import ExperienceUpdateForm
from companies.models import Experience

# Create your views here.


class ExperienceUpdateView(
    SuccessMessageMixin,
    UserPassesTestMixin,
    UpdateView
):
    '''
    Edits fields for a given SiteUser instance.
    '''
    model = Experience
    context_object_name = 'experience'
    form_class = ExperienceUpdateForm
    slug_field = 'comapny'
    slug_url_kwarg = 'comapny'
    success_message = 'Expereince Updated!'
    template_name = 'companies/user_experience_update_form.html'

    def get_success_url(self):
        return reverse_lazy(
            'accounts:profile',
            kwargs={
                'unique_id': self.request.user.unique_id
            }
        )

    def test_func(self):
        return self.request.user.experience_set.filter(pk=self.get_object().pk).exists()
