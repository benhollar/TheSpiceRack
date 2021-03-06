# Generated by Django 3.1.3 on 2021-01-19 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('Teaspoon', 'Teaspoon'), ('Tablespoon', 'Tablespoon'), ('Ounces', 'Ounces'), ('Cup', 'Cup'), ('Pint', 'Pint'), ('Quart', 'Quart'), ('Gallon', 'Gallon'), ('Milliliter', 'Milliliter'), ('Liter', 'Liter'), ('Pound', 'Pound'), ('Gram', 'Gram'), ('Kilogram', 'Kilogram')], default='Teaspoon', max_length=200)),
                ('is_fluid', models.BooleanField()),
                ('is_metric', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('steps', models.CharField(max_length=200)),
                ('servings', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RecipeStep',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('RecipeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('measurement_id', models.IntegerField()),
                ('recipe_used', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
            ],
        ),
    ]
