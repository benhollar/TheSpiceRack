from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from recipe.models import Recipe
from recipe.serializers import RecipeSerializer
from . import models
from .forms import CustomUserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import login


#HOMEPAGE
def home(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    context = {'recipes':serializer.data}
    return render(request, 'home.html', context)

#USERPROFILE
def profile(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    recipes = Recipe.objects.all().filter(username=username)
    serializer = RecipeSerializer(recipes, many=True)
    context = {'recipes': serializer.data}
    return render(request, 'profile.html', context)




def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("home"))