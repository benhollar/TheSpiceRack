# The Spice Rack Test Plan Results

## Database Test 1

**Create a new User for the system**

* User can create account in login page (prompted at the start)
* Fill in all fields required and submit
* After creation, user can log in and add recipes

## Database Test 2

**View Recipe Information**

* User is logged in
* Hover over recipes in home or profile
* Click View
* Redirect to recipe page which will display information

## Database Test 3

**Delete a Recipe**

* User is logged in
* Hover over recipes in home or profile
* Click View
* Redirect to recipe page which will display information
* Click Delete
* Recipe will be removed from database and from pages

## Input Test 1

**Edit Recipe Information**

* User is logged in
* Hover over recipes in home or profile
* Click Edit
* Redirect to edit page, where fields are filled in with recipe information
* User can change, add/remove steps or ingredients
* Click Submit button at the bottom
* Database is updated with information

## Input Test 2

**Add new Recipe manually**

* User is logged in
* Hover over Add Recipes in navigation
* Click Add Manually
* Redirect to recipe form
* User adds image, information to fields, selects measurement, etc.
* Click Add Recipe to Database button at the bottom
* Database is saved with information, and will populate on home and profile page with image

## Input Test 3

**Manually change passwords for user**

* User is logged in
* Hover over Profile in navigation
* Click Change password
* User enters a password that contains valid characters, and must not match current password
* Submit
* Password is changed and redirected to confirmation page

## Server Test 1

**Parse recipe portions from URL**

* User navigates to Add Recipe, and Add via URL
* User pastes url from recipe website
* Server parses recipe information
* Webpage displays recipe with photo and informations in its corresponding sections

## User Interface Test 1

**Existing user can log in**

* Entering link directs user to login page
* User enters credentials of existing user in database
* Click Login
* User is redirected to homepage with existing recipes, and username displayed

## User Interface Test 2

**User can view a list of all recipes in database**

* User is logged in
* The home page will display all existing recipes, as well as the profile page

## User Interface Test 3

**Add recipe via URL**

* User navigates to Add Recipe, and Add via URL
* User pastes url from recipe website
* Webpage is redirected and will display recipe with photo and informations in its corresponding sections
* Recipe will also be displayed in home/profile page

