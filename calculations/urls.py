from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('1/', views.matches_per_year, name='matches_per_year'),
    path('2/', views.matches_won_per_team, name='matches_won_per_team'),
    path('3/' ,views.extra_runs_per_team, name='extra_runs_per_team'),
    path('4/', views.top_ten_econ_bowlers, name='top_ten_econ_bowlers')
]