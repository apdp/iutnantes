TP #2
=====
cf. GITHUB => https://github.com/apdp/iutnantes

cf. aussi le readme.md sur le github de Sébastien Prunier :
https://github.com/sebprunier/installations-sportives-pdl

## EXCEPTIONS
  . regarder comment utiliser les exceptions
     => cf. [librairie Python §exceptions](https://docs.python.org/3.3/library/exceptions.html)

## TESTS et DOCUMENTATION
  . regarder comment ajouter de la [documentation de code (dostring)](https://docs.python.org/3/library/doctest.html#module-doctest)
  . utiliser des [Tests Unitaires](https://docs.python.org/3/library/unittest.html)

## CSV des Installations Sportives des Pays de la Loire
  1. telecharger les 3 fichiers CSV jeux de données, au format CSV : 
    * [Installations](http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-fiches-installations)
    * [Equipements](http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-fiches-equipements)
  	* [Activités](http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-activites-des-fiches-equ)
  2. manipuler les fichiers CSV comme au TP #1 avec l'aide du module 'csv'

## Base de Données
  1. mettre en place une base de données alimentée par ces fichiers CSV
  2. manipuler la Base de données via le module 'sqlite3' dans un 1er temps
     RQ : vous pouvez utiliser par exemple [SQL Lite Browser](http://www.sqllitebrowser.sourceforge.net)
  3. dans un 2nd temps, installer le connecteur MySQL pour utiliser une BD MySQL
  http://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html

