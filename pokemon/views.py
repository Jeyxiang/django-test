from functools import partial
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from pokemon import serializers
from .serializers import PokemonSerializers
from rest_framework import status, generics 
from rest_framework.generics import get_object_or_404 
from rest_framework.response import Response 
from rest_framework.views import APIView
from pokemon.models import Pokemon
import random


#APIView: Requests passed to the handler methods will be REST framework's Request instances
class PokemonView(APIView):

    #Get method handler
    class GetAllPokemon(generics.ListAPIView):
        serializer_class = PokemonSerializers
        queryset = Pokemon.objects.all()
        def get(self,request):
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
       
    
    class GetMyPokemon(generics.ListAPIView):
        serializer_class = PokemonSerializers
        queryset = Pokemon.objects.all()
        def get(self,request):
            queryset = self.get_queryset()
            currUser = self.request.user
            filtered = queryset.filter(user = currUser)
            serializer = self.serializer_class(filtered, many=True)
            return Response(serializer.data)
        
    class GetUnknownPokemon(generics.ListAPIView):
        serializer_class = PokemonSerializers
        queryset = Pokemon.objects.all()
        def get(self,request):
            queryset = self.get_queryset()
            currUser = self.request.user
            filtered = queryset.exclude(user = currUser)
            serializer = self.serializer_class(filtered, many=True)
            return Response(serializer.data)

    #Post Method Handler  
    class AddPokemon(generics.CreateAPIView):
        serializer_class = PokemonSerializers
        def post(self,request):
            pokemon_object = get_object_or_404(Pokemon, id = request.data['id'])
            rand_num = random.randrange(1,100)
            rq = {
                'user':  request.data['user'], #placeholder 
                'level': rand_num
            }
            serializer = self.serializer_class(pokemon_object,data=rq,partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    class RemovePokemon(generics.CreateAPIView):
        serializer_class = PokemonSerializers
        def post(self,request):
            pokemon_object = get_object_or_404(Pokemon, id = request.data['id'])
            rq = {
                'user': None,
                'level': None
            }
            serializer = self.serializer_class(pokemon_object,data=rq,partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
