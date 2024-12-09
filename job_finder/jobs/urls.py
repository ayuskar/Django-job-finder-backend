from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.JobListView.as_view(), name='job_list'),
    path('jobs/<int:job_id>/apply/', views.applyforjob, name='apply_for_job'),
    path('admin/jobs/create/', views.JobCreateView.as_view(), name='job_create'),
    path('admin/jobs/<int:pk>/update/', views.JobUpdateView.as_view(), name='job_update'),
    path('admin/jobs/<int:pk>/delete/', views.JobDeleteView.as_view(), name='job_delete'),
    path('admin/jobs/<int:job_id>/applications/', views.viewapplications, name='view_applications'),
]

