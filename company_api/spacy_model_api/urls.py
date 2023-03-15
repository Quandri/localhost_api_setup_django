from django.urls import path, re_path
from . import views


urlpatterns = [
    path("en_spacy_model/", views.download_from),
]
