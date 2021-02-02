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
    print(serializer)
    context = {'recipes':serializer.data}
    return render(request, 'home.html', context)

#USERPROFILE
def profile(request, username):
    queryset = models.CustomUser.objects.all()
    #seralizers = seralizers.UserSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, )
    search_fields = ('full_name', 'email', )
    ordering_fields = ('full_name',)

    @action(detail=True, methods=['get'])
    def recipes(self, request, pk=None):
        user = models.CustomUser = self.get_object()
        recipe = Recipe.objects.filter(user_id_full_name=user)
        serializer = RecipeSerializer(recipe, many=True)
        return Response(serializer.data)


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