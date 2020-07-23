from django.urls import path
from IPLteam import views

urlpatterns = [
    path('', views.home_view),
    path('add/', views.addTeam_view),
    path('display/', views.displayTeam_view)

]
