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

Or how many are black

````
>>> from demographics import us_demographics
>>> me = us_demographics('adam', 'deprince)
>>> pop = 313.9 * 1000 ** 2 # Current population of the US
>>> me.popularity * me.black * pop


Installation
============

````
    pip install demographics
````

Sources
=======

[https://www.census.gov/genealogy/www/data/2000surnames/]
[http://www.census.gov/genealogy/www/data/1990surnames/names_files.html]

