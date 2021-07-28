from django.urls import path

from .views import ProjectsListView, ProjectsDetailsView

urlpatterns = [
    path('', ProjectsListView.as_view(), name='projects_api'),
    path('<int:pk>', ProjectsDetailsView.as_view(), name='projects_details_api'), 
]