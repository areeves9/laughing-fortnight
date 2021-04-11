from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


from django.urls import reverse_lazy

from companies.models import Experience

# Create your views here.


class ExperienceCreateView(
    SuccessMessageMixin,
    LoginRequiredMixin,
    CreateView,
):
    '''
    Creates an experience instance with FK relation to a User.
    '''
    model = Experience
    fields = (
        'company',
        'title',
        'date_from',
        'date_to',
        'description',
        'headline',
        'employment_type',
        'is_current',
    )
    success_message = 'Expereince Added!'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'accounts:profile',
            kwargs={
                'unique_id': self.request.user.unique_id
            }
        )


class ExperienceDetailView(
    LoginRequiredMixin,
    DetailView
):
    '''
    Retrieves an Experience instance.
    '''
    model = Experience


class ExperienceDeleteView(
    SuccessMessageMixin,
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView
):
    '''
    Retrieves an Experience instance.
    '''
    model = Experience
    context_object_name = 'experience'
    success_message = 'Expereince Deleted!'
    template_name = 'companies/experience_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy(
            'accounts:profile',
            kwargs={
                'unique_id': self.request.user.unique_id
            }
        )

    def test_func(self):
        return self.request.user.experience_set.filter(pk=self.get_object().pk).exists()


class ExperienceUpdateView(
    SuccessMessageMixin,
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView
):
    '''
    Edits fields for a given SiteUser instance.
    '''
    fields = (
        'company',
        'title',
        'date_from',
        'date_to',
        'description',
        'headline',
        'employment_type',
        'is_current',
    )

    model = Experience
    context_object_name = 'experience'
    slug_field = 'company'
    slug_url_kwarg = 'company'
    success_message = 'Expereince Updated!'

    def get_success_url(self):
        return reverse_lazy(
            'accounts:profile',
            kwargs={
                'unique_id': self.request.user.unique_id
            }
        )

    def test_func(self):
        return self.request.user.experience_set.filter(pk=self.get_object().pk).exists()
