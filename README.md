# The Spice Rack User Documentation

> **NOTICE:** This project is being actively developed as a Senior Capstone project by students at the University of
> Cincinnati, advised by Dr. Chia Han. For more details on the University of Cincinnati class requirements, see the
> [UC Senior Design folder](https://github.com/benhollar/TheSpiceRack/tree/master/UC%20Senior%20Design) of this
> repository.

Finding, collecting, and cooking recipes can be a daunting task. There are numerous hurdles for people to effectively
manage their recipes. The Spice Rack aims to make the following effortless for users:

1. Parsing a variety of sources of recipes (websites, handwritten recipes) into a common, easy-to-read format.
2. Storing user recipes, including automatically imported recipes from the previously mentioned parser.
3. Presenting an effective user-interface for navigating stored recipes.

## Table of Contents

* [Getting Started](#getting-started)
	* [Application](#application)
	* [Content Recognition](#content-recognition)
* [FAQ](#faq)

## Getting Started

The Spice Rack is designed to be a user-friendly web application, but we have listed directions for troubleshooting and setup.

This project is, currently, divided in to two main sections:

1. **Application**: A Django web-application, providing the app's user-interface and server logic.
2. **Content Recogition**: A set of utilities leveraging the [dragnet](https://github.com/dragnet-org/dragnet) ML
   library for developing a content extraction model tailored to retrieving recipes from websites.
   [Training data](https://github.com/benhollar/TheSpiceRack/tree/master/Code/Content%20Recognition/content_data)
   gathered by The Spice Rack contributors can also be found in this section.

Detailed instructions for getting set up with each section of the repository are enumerated below.

### Application

### How to install for development/personal use
1.	Install Python version 3.8.8 or higher
2.	Install Django using Django provided documentation 
3.	Install Other django packages needed: 
	* Run: `pip install django-allauth`
	* Run: `pip install django-rest-auth`
	* Run: `pip install socialdjango`
4.	Set up database for the website to store and pull data from
	* Run `python manage.py makemigrations`
	* Run: `python manage.py migrate`
5.	Create User to log in with to use the website: 
	* Run: `python manage.py createsuperuser`
6.	Fill in required table
	* Run: `Python manage.py runserver`
	* Go to "127.0.0.1:8000/admin" in a web browser
	* Log in using account created in step 5
	* Click on 'Measurements' under the Recipe header
	* Add the following values manually to the table: 
		1. ID: 1 Type: Teaspoon 
		2. ID: 2 Type: Tablespoon
		3. ID: 3 Type: Ounces
		4. ID: 4 Type: Cup
		5. ID: 5 Type: Pint
		6. ID: 6 Type: Quart
		8. ID: 7 Type: Gallon
		9. ID: 8 Type: Milliliter
		10. ID: 9 Type: Liter
		11. ID: 10 Type: Pound
		12. ID: 11 Type: Gram
		13. ID: 12 Type: Kilogram
		* Note: The 'is fluid' and 'is metric' check boxes are optional, but do not need to be checked.
7.	Use website!
	* Navigate to 127.0.0.1:8000/
	* Log in with user created in step 5

To see examples of our pages, head over to our [UI Design](https://github.com/benhollar/TheSpiceRack/tree/master/UC%20Senior%20Design/UI%20Design) folder!

#### Logging In

![Login](https://github.com/benhollar/TheSpiceRack/blob/master/UC%20Senior%20Design/UI%20Design/Login.png)

After entering the website URL, you will be prompted to our Login page. 

To create an account, navigate to **Create Account** at the bottom. From there, you can enter the data necessary to register the account.

Once your account is ready, you may login and begin your cooking journey!

![Home](https://github.com/benhollar/TheSpiceRack/blob/master/UC%20Senior%20Design/UI%20Design/Home.png)


You will be prompted to our homepage, which will display any existing recipes.


#### Adding a Recipe

![Add](https://github.com/benhollar/TheSpiceRack/blob/master/UC%20Senior%20Design/UI%20Design/Add.png)

To add a recipe, head over to our navigation bar and select **Add Recipe**. A dropdown will appear, and you can choose to add a recipe manually, or via URL. From there, you will be able to enter all of your recipe needs. To add an extra ingredient or step, you can hit the **Add Ingredient/Step** button. Our ingredients portion also allows for you to change the measurements as well! Once you are done, click submit and your recipe will be saved and displayed for all to see.

![URL](https://github.com/benhollar/TheSpiceRack/blob/master/UC%20Senior%20Design/UI%20Design/URL.png)
To add a recipe via URL, you can paste your favorite recipe from any recipe site, and hit **Upload Recipe**!


#### Editing a Recipe

![Edit](https://github.com/benhollar/TheSpiceRack/blob/master/UC%20Senior%20Design/UI%20Design/Edit.png)

To edit a recipe, you can hover over an existing recipe and click **Edit**. You should be able to select a recipe that you want to edit, and modify any changes. 

![Recipe](https://github.com/benhollar/TheSpiceRack/blob/master/UC%20Senior%20Design/UI%20Design/Recipe.png)

Or you can view a recipe, and hit **Edit Recipe**. Hit submit and you're good to go!

### Content Recognition

#### Requirements

* Python 3
  * Note: this project was developed using version 3.7.3, and versions 3.8.x and newer may require modified installation
    steps (the `dragnet` library, which this work relies on, only apparently supports versions 3.7 and earlier)
* The `Content Recognition/` directory of this repo cloned to your system

To get started, ensure you have all required packages for this project installed. You can do so via the
`requirements.txt` file provided under `Content Recognition/`.

```bash
pip install -r "Content Recognition/requirements.txt"
```

#### Usage

As a simple test that everything is working correctly, consider training a model based on the data provided by The Spice
Rack under `Content Recognition/content_data/`. The following snippet trains a model and returns a
[dragnet](https://github.com/dragnet-org/dragnet) `Extractor`, which can then be used to extract recipe content from
any web page.

```python
import recipe_extraction
import requests

# Train a default model using The Spice Rack data
extractor = recipe_extraction.models.train()

# See how the model performs on a given webpage
url = 'https://www.some-recipe-website.com/recipe/some-really-good-recipe'
request = requests.get(url)
extracted_content = extractor.extract(request.content)
print(extracted_content)
```

An ideal model is one with high precision; that is, it returns only exact recipe information, and avoids instances of
returning content that is _not_ part of a recipe. Of course, it would be ideal to have both high recall _and_ precision,
but one must usually be optimized for over the other.

Once you're happy with a model, you might want to save it for reuse. To do so:

```python
recipe_extraction.models.save(extractor)

# At some future point in time / different function, load the model
extractor = recipe_extraction.models.load('path-to-saved-model.gz')
```
## Frequently Asked Questions (FAQ)

### Q. How is this different than a typical recipe website?

A. Unlike most recipe websites, The Spice Rack can parse recipes that fit your need, without the hassle of pop-ups and ads!

### Q. How do I make an account?

A. On the navigation bar, there is User tab. Once you click that, there should be a dropdown option for creating an account.

### Q. Can I input a recipe manually?

A. Yes! The web page has a page that will allow users to manually add recipes.

See [Adding a Recipe](#adding-a-recipe)

### Q. Is there an option to share saved recipes?

A. Currently no, but that's something we would like to add later on!

### Q. Can I upload handwritten recipes?

A. We currently do not have a feature that will transform handwritten recipes digitally, however that is something that we would like to work on!

### Q. Is the Spice Rack Safe?

A. The Spice Rack is open source, and a safe application. You can view our source code in [The Spick Rack Github Page](https://github.com/benhollar/TheSpiceRack/tree/master/Code) to verify the integrity of our software.

***If you have additional questions, feel free to contact our team found in our [Project Abstract](https://github.com/benhollar/TheSpiceRack/blob/master/UC%20Senior%20Design/Project%20Description.md)***
