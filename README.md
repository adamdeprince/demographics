Demographics
============

A simple python library to return basic demographic given a first and last name. 


To compute approximately how many people in the US have your name: 

````
>>> from demographics import us_demographics
>>> me = us_demographics('adam', 'deprince') 
>>> pop = 313.9 * 1000 ** 2  # Current population of the US
>>> me.popularity * pop
57.129799999999996
````

Or how people with your name are black. 

````
>>> me = us_demographics('david','smith')
>>> me.popularity * pop
1020280.6273500001
>>> me.popularity * pop * me.black
226706.35539717003
````

Or not your gender

````
>>> me.popularity * pop * me.female
16589.928900000003
````





Installation
============

````
    pip install demographics
````

Sources
=======

[https://www.census.gov/genealogy/www/data/2000surnames/]
[http://www.census.gov/genealogy/www/data/1990surnames/names_files.html]

