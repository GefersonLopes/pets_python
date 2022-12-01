from django.urls import path
from pets.views import PetView, IDPetView;

urlpatterns = [
    path('pets/', PetView.as_view()),
    path('pets/<int:id>/', IDPetView.as_view()),
]