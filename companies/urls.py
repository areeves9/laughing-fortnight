from companies import views
from django.urls import path

app_name = 'companies'

urlpatterns = [
    path(
        'experience/<int:pk>/update',
        views.ExperienceUpdateView.as_view(
            template_name='companies/user_experience_update_form.html'
        ), name='experience_update'
    ),
]