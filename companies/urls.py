from companies import views
from django.urls import path


app_name = 'companies'

urlpatterns = [
    path(
        'experience/<int:pk>/detail',
        views.ExperienceDetailView.as_view(), name='experience-detail'
    ),
    path(
        'experience/create',
        views.ExperienceCreateView.as_view(), name='experience-create'
    ),
    path(
        'experience/<int:pk>/update',
        views.ExperienceUpdateView.as_view(), name='experience-update'
    ),
]
