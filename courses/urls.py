from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('instructor/<int:pk>/', views.instructor_detail, name='instructor_detail'),
    path('course/<int:pk>/enroll/', views.enroll_course, name='enroll_course'),
    path('enrollment/<int:pk>/edit/', views.edit_enrollment, name='edit_enrollment'),
    path('enrollment/<int:pk>/cancel/', views.cancel_enrollment, name='cancel_enrollment'),
]