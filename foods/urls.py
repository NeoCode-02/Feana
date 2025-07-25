from django.urls import path
from .views import IndexView, MenuView, BookView, AboutView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
    path("book/", BookView.as_view(), name="book"),
    path("menu/", MenuView.as_view(), name="menu"),
]
