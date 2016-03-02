### Mettez en place toute la gestion de tests unitaires
1. vous utiliserez les tests unitaires proposés nativement par Python
    https://docs.python.org/3/library/unittest.html

### Documenter et renforcer la gestion d'erreurs de votre application
2. utilisez des exceptions à chaque fois qu'une erreur peut se déclencher
     => cf. [librairie Python §exceptions](https://docs.python.org/3.3/library/exceptions.html)
3. ajoutez la documentation de code (dostring) :
    (https://docs.python.org/3/library/doctest.html#module-doctest)

### Realiser une application web pour fournir des API REST (services)
4. vous utiliserez pour cela le framework BOTTLE
     http://bottlepy.org/docs/dev/index.html
5. vous fournirez les réponses pour chaque ressource dans le format de représentation
   qui vous convient (XML ou JSON par exemple)
6. vos API permettront de récupérer et modifier toutes les informations
   d'installations, équipements, et activités et d'effectuer quelques recherches
     => vous définirez pour cela au préalable les URI de vos ressources

### Realiser une 2nde application web pour interroger vos API
7. C'est une application web simple qui pourra s'exécuter dans un navigateur
   (en HTML / Javascript / JQuery)
   Cette application offre une interface à l'utilisateur pour lui faciliter la saisie
   et l'affichage des résultats.
8. lorsque vous aurez des API qui fonctionnent avec un client de test,
   vous pourrez fournir vos services pour que d'autres binomes les testent

+ voir aussi le github de Sebastien Prunier (enseignant d'un autre groupe de TP) :
    https://github.com/sebprunier/installations-sportives-pdl
