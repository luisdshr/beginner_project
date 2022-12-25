from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    PythonPageView,
    FsharpPageView,
    RacketPageView,
)

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
    path("python/", PythonPageView.as_view(), name="python"),
    path("fsharp/", FsharpPageView.as_view(), name="fsharp"),
    path("racket/", RacketPageView.as_view(), name="racket"),
]
