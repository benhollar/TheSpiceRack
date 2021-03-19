from .models import Ingredient, Recipe, Measurement
from .serializers import RecipeSerializer, IngredientSerializer, MeasurementSerializer
from django.shortcuts import render, redirect

#WHAT HAPPENS WHEN THEY WANT TO VIEW A SPECIFIC RECIPE
def view_recipe(request, recipe_id):
    #Search for specific recipe based on ID
    query = Recipe.objects.all().filter(id=recipe_id)
    results = query.values()
    recipe = RecipeSerializer(results[0], many=False)

    filename = '/media/' + results[0].get('picture')

    recipe_model = Recipe(picture=recipe.data.get('picture'), id=recipe.data.get('id'), user_id=recipe.data.get('user_id'), title=recipe.data.get('title'), steps=recipe.data.get('steps'), servings=recipe.data.get('servings'))
    query_i = Ingredient.objects.all().filter(recipe_used=recipe_model)
    results_i = query_i.values()
    ingredients = []
    measurements = []


    for thing in results_i:
        ingredient = IngredientSerializer(thing, many=False)
        ingredients.append(ingredient.data)
        query_m = Measurement.objects.all().filter(id=ingredient.data.get('measurement_id'))
        results_m = query_m.values()
        measurement = MeasurementSerializer(results_m[0], many=False)
        measurements.append(measurement.data.get('type'))

    print(measurements)

    fullsteps = recipe.data.get('steps')

    splitsteps = fullsteps.split('/n')
    splitsteps.remove('')

    zipped_data = zip(ingredients, measurements)

    context = {'recipe':recipe.data, 'steps' : splitsteps, 'filename' : filename, 'zipped': zipped_data}


    return render(request, 'recipe_info.html', context)

def submit_recipe(request):
    #Get values from html
    if request.method == 'POST':
        title = request.POST.get('title')
        servings = request.POST.get('servings')

        picture = request.FILES['picture']
        print(picture)
        #new_path = settings.MEDIA_URL + picture

        all_steps = ""
        count_steps = 1
        for key in request.POST:
            #Condense step inputs into single input?
            if "step" in key:
                step = request.POST.get("step_"+str(count_steps))
                all_steps+=step+"/n"
                count_steps+=1

        id_r = Recipe.objects.all().count()
        print(id_r)

        testing = Recipe.objects.create(id=id_r+3, username=request.user.username, title=title, servings=servings, steps=all_steps, picture=picture)

        ##Create Ingredient objects for each
        id_i = Ingredient.objects.all().count()

        for key in request.POST:
            #Create ingriedent object for all ingredients
            if "amount" in key:
                count = 0
                id_i += 1
                ingredients_amount=request.POST.get("amount_"+str(count))
                ingredients_measurement=request.POST.get("measurement_"+str(count))
                ingredients_name=request.POST.get("name_"+str(count))

                # Get all measurement objects to be put into Ingredient
                query_m = Measurement.objects.all().filter(type=ingredients_measurement)
                results_m = query_m.values()
                measurement = MeasurementSerializer(results_m[0], many=False)

                Ingredient.objects.create(id=id_i+5, name=ingredients_name, amount=ingredients_amount, measurement_id=measurement.data.get('id'), recipe_used=testing)
    return redirect('/users/')


def add_recipe(request):
    return render(request, 'add_recipe.html')


def edit_recipe(request, recipe_id):
    query = Recipe.objects.all().filter(id=recipe_id)
    results = query.values()
    recipe = RecipeSerializer(results[0], many=False)

    filename = '/media/' + results[0].get('picture')

    recipe_data = recipe.data
    recipe = Recipe(picture=recipe_data.get('picture'), id=recipe_data.get('id'), title=recipe_data.get('title'), servings=recipe_data.get('servings'), steps=recipe_data.get('steps'))
    query_i = Ingredient.objects.all().filter(recipe_used=recipe)
    results_i = query_i.values()
    ingredients = []

    for thing in results_i:
        ingredient = IngredientSerializer(thing, many=False)
        ingredients.append(ingredient)

    fullsteps = recipe_data.get('steps')

    splitsteps = fullsteps.split('/n')

    splitsteps.remove('')

    context = {'recipe': recipe_data, 'ingredients': ingredients, 'steps': splitsteps, 'filename' : filename}
    #Upload results[0] into html values

    return render(request, 'edit_recipe.html', context)

def save_recipe(request, recipe_id):
    if request.method == 'POST':
        picture = request.FILES['picture']
        title = request.POST.get('title')
        servings = request.POST.get('servings')
        all_steps = ""
        count_steps = 1
        for key in request.POST:
            # Condense step inputs into single input?
            if "step" in key:
                step = request.POST.get("step_" + str(count_steps))
                all_steps += step + "/n"
                count_steps += 1

        query_r = Recipe.objects.all().filter(id=recipe_id)
        results_r = query_r.values()
        recipe_preedit = RecipeSerializer(results_r[0], many=False)
        recipe_pre = Recipe(picture=recipe_preedit.data.get('picture'), id=recipe_preedit.data.get('id'), user_id=recipe_preedit.data.get('user_id'), title=recipe_preedit.data.get('title'), servings=recipe_preedit.data.get('servings'), steps=recipe_preedit.data.get('steps'))

        recipe = Recipe(picture=picture, username= request.user.username, id=recipe_id, user_id=0, title=title, servings=servings, steps=all_steps)
        recipe.save()

        query_i = Ingredient.objects.all().filter(recipe_used=recipe_pre)
        results_i = query_i.values()
        measurements = []

        for thing in results_i:
            ingredient = IngredientSerializer(thing, many=False)
            ingred = Ingredient(id=ingredient.data.get('id'), name=ingredient.data.get('name'), amount=ingredient.data.get('amount'), measurement_id=ingredient.data.get('measurement_id'), recipe_used=recipe)
            query_m = Measurement.objects.all().filter(id=ingredient.data.get('measurement_id'))
            results_m = query_m.values()
            measurement = MeasurementSerializer(results_m[0], many=False)
            measurements.append(measurement.data.get('type'))
            ingred.save()

    return redirect('/users/')


def delete_recipe(request, recipe_id):
    instance = Recipe.objects.get(id=recipe_id)
    instance.delete()
    return redirect('/users/')

def upload_recipe(request):
    return render(request, 'upload_recipe.html')

def parse_recipe(request):
    #URL should be the only input
    request.GET.get('url')


    #TODO: The Machine Learning things

    #TODO: Put machine learning output into this context boy



    context = {'recipe': recipe_data, 'ingredients': ingredients, 'steps': splitsteps}

    return render(request, 'edit_recipe.html', context)
