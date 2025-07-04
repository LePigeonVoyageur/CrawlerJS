# CrawlerJS
Un crawler en Javascript accompagné d'un programme en python qui fait presque tout.
## Prérequis  
#### *Discalmer :  Si vous avez Python et Flask d'installés, allez directement à la partie [Lancement](#Lancement).*  
Tout d'abord, il vous faut Python. Vérifiez la version avec : 
```shell script
$ python3 --version
Python 3.x.x
 ou
$ python3 -V
Python 3.x.x
```
Sinon, il faudra télécharger Python sur [le site officiel](https://www.python.org/downloads/).
Une fois que c'est fait, tapez 
```shell script
$ pip install Flask
 ou
$ pip3 install Flask # Si vous avez une version antérieure à Python 3
```
Maintenant (si l'intallation à réusi), on va passer à la partie suivante.  
## Lancement
Il faudra ensuite installer le fichier si ce n'est pas déjà fait et entrer cette commande :
```shell script
cd /Votre/chemin/de/dossier/CrawlerJS
python3 app.py
```
En remplaçant bien par le chemin vers le fichier CrawlerJS.  
La console devrait vous renvoyer ce message
```shell script
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://xxx.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: xxx-xxx-xxx
```
Copiez l'adresse créée (4e ligne : http://<i></i>xxx.0.0.1:5000) et collez-là dans la barre de recherche d'un navigateur.  
Le site devrait normalement fonctionner.
## Pourquoi les requêtes peuvent-elles prendre du temps ?
Les requêtes peuvent prendre du temps à cause de (ou grâce à) la 38e ligne du code en python :
```python
time.sleep(random.uniform(0.5, 1))
```
Cette ligne attends un temps aléatoire entre 0.5s et 1s avant d'envoyer chaque requête.  
Elle vous protège des attaques [DDoS](https://fr.wikipedia.org/wiki/Attaque_par_d%C3%A9ni_de_service) qui sont passibles de  
> jusqu'à cinq ans d'emprisonnement et 150 000 euros d'amende.  

Bref, à éviter.
