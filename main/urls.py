from django.urls import path
from main.views import home_page

urlpatterns = [
    path('', home_page, name = "scraper"),
]