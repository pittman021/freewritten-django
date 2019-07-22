from django.urls import include, path
from pages.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
]