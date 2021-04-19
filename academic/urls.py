from django.urls import path

from . import views

app_name = 'academic'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('talks/', views.TalksView.as_view(), name='talk_index'),
    path('talks/<int:pk>/', views.TalkDetailView.as_view(), name='talk_detail'),
    path('teaching/', views.TeachingView.as_view(), name='teaching'),
]