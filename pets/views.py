from rest_framework.views import APIView, Request, status; 
from rest_framework.response import Response; 

from .serializers import PetSerializer;
from .models import Pet;

from django.shortcuts import get_object_or_404


class PetView(APIView):
    def post(self, request: Request) -> Response:
        serialize = PetSerializer(data=request.data);
        
        if not serialize.is_valid():
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST);
        
        serialize.save();

        return Response(serialize.data, status.HTTP_201_CREATED);


    def get(self, request: Request) -> Response:
        pets = Pet.objects.all();
        serialize = PetSerializer(pets, many=True);

        return Response(serialize.data, status=status.HTTP_200_OK);    
  

class IDPetView(APIView):
    def get(self, request: Request, id: int) -> Response:
        pet = get_object_or_404(Pet, id=id);
        serialize = PetSerializer(pet);

        return Response(serialize.data, status=status.HTTP_200_OK);

    def patch(self, request: Request, id: int) -> Response:
        pet = get_object_or_404(Pet, id=id);
        serialize = PetSerializer(pet, request.data, partial=True);
        
        if not serialize.is_valid():
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST);
        
        serialize.save();


        return Response(serialize.data, status=status.HTTP_200_OK);

    
    def delete(self, request: Request, id: int) -> Response:
        pet = get_object_or_404(Pet, id=id);
        pet.delete();

        return Response(status=status.HTTP_204_NO_CONTENT);

        