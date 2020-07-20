from django.urls import path
from django.conf.urls import url
from testapp import views

urlpatterns = [
    path('', views.HelloWorldView.as_view(), name = 'HelloWorldView'),
    #url(r'^templateView/', views.HelloWorldTemplateView.as_view()),
    path('templateView/', views.HelloWorldTemplateView.as_view(), name = 'HelloWorldTemplateView'),
]
