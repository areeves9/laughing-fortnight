from companies import views
from django.urls import path


app_name = 'companies'

urlpatterns = [
    path(
        '',
        views.CompanyListView.as_view(), name='company-list'
    ),
    path(
        'company/<int:pk>/detail',
        views.CompanyDetailView.as_view(), name='company-detail'
    ),
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
    path(
        'experience/<int:pk>/delete',
        views.ExperienceDeleteView.as_view(), name='experience-delete'
    ),
]
