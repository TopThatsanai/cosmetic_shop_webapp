from django.urls import path, include
from . import views
from cosmetic import views as cosmetic_views
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register", view=views.register, name="register"),

]