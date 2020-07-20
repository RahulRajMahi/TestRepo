from django.urls import path, include
from testapp import views

urlpatterns = [
    path('', views.home_page_view),
    path('java/', views.java_page_view),
    path('python/', views.python_page_view),
    path('aptitude/', views.aptitude_page_view),
    path('logout/', views.logout_view),
    path('signup/', views.signup_view),
    path('accounts/', include('django.contrib.auth.urls'))
]
