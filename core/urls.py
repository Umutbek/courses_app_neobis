from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('categories/', views.CategoryView.as_view(), name='categories'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('courses/', views.CourseView.as_view(), name='courses'),
    path('courses/<int:pk>/', views.CourseDetail.as_view(), name='courses_id'),
    path('branch/', views.BranchView.as_view()),
    path('branch/<int:pk>/', views.BranchDetail.as_view()),
    path('contact/', views.ContactView.as_view()),
    path('contact/<int:pk>/', views.ContactDetail.as_view()),
]
