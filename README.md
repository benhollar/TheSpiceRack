# The Spice Rack

A planning-phase project for a Senior Capstone at the University of Cincinnati. For more details on the University of Cincinnati class requirements, see the `UC Senior Design` folder of this repository.

## Basic Idea

Finding, collecting, and cooking recipes can be a daunting task. There are numerous hurdles for people to effectively manage their recipes. In this project, we'd like to create an effective way of:

1. Parsing a variety of sources of recipes (websites, handwritten recipes) into a common, easy-to-read format.
2. Storing user recipes, including automatically imported recipes from the previously mentioned parser.
3. Presenting an effective user-interface for navigating stored recipes

## Potential Technologies

For parsing recipes, we want to avoid instances in which we must have custom behavior for each input source. A general solution that works broadly is a key goal of this project. As such, we envision the parser will entail using some combination of the following:

1. Machine learning
2. Optical character recognition (for handwriting)
3. Simple HTML parsing

The rest of the intended project (storage and display of user recipes) will likely involve:

1. A relational database
2. REST API to retrieve DB info
3. Web frontend
