from django.conf.urls import url, include
from howdy import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]