# Senior Design Project Idea

Members:

1. Ben Hollar (hollarbl@mail.uc.edu), Computer Science
2. Erin Graska (graskaen@mail.uc.edu), Computer Science
3. Stephanie Tam (tamse@mail.uc.edu), Computer Science

Faculty Advisor:

1. Dr. Chia Han (han@ucmail.uc.edu)

## Final Abstract

Finding and collecting recipes can be a daunting task, and many online recipe sources distract users with unnecessary
blogs or advertisements. The Spice Rack aims to reduce that problem by providing a web application where users can store
their recipes without distractions and import recipes from online sources using a machine-learning driven content
extraction process.

## Detailed Description

The Spice Rack is a web-application dedicated to allowing users to import and collect their recipes in a central,
persistent, and accessible hub. Key to enabling this was the implementation of a machine-learning (ML) backed algorithm
that can, given a URL, automatically collect recipe information and populate our web forms without any user
intervention. As such, the project was divided into 3 distinct pieces, worked on independently by one team member each,
then combined to produce our final result. Those three pieces were:

1. (Ben Hollar) Machine-learning recipe parsing, leveraging `dragnet` for content extraction and `BERT` for text
   classification.
2. (Erin Graska) Backend web development, leveraging the `Django` web-development framework for Python
3. (Stephanie Tam) Frontend web development and design, leveraging `Django`, HTML, and CSS to create an effective UI

When combined, these pieces form a complete web application, backed by a database which serves data via a REST API, and
can ingest data using ML models -- fulfilling our original project goals.
