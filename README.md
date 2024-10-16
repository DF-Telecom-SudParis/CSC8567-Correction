<p align="center">
    <img src="https://github.com/user-attachments/assets/3ba5a526-c617-49c7-8165-30c3f3505d5c" width="300" alt="TSP logo">
</p>

# CSC 8567 - Architectures distribuées et applications web - Correction

Auteurs : Timothée Mathubert, Gatien Roujanski, Arthur Jovart

## Emails

- timothee.mathubert@telecom-sudparis.eu
- gatien.roujanski@telecom-sudparis.eu
- arthur.jovart@telecom-sudparis.eu

## Schéma de la base de données

<p align="center">
    <img src="https://github.com/user-attachments/assets/4cd224f5-5f64-48b7-bd6f-c25f301275ca" alt="BDD">
</p>

## Schéma de l'infrastructure

<p align="center">
    <img src="https://github.com/user-attachments/assets/e8c0254e-05b6-4f0b-a41b-c41dc3fefab3" alt="Infra">
</p>

## Arbre des pages selon leur URL

### URLs globaux

- Page d'accueil : `/` – Dirigé vers public.urls (vue public_home).
- Page d'accueil de l'API : `/api/` – Dirigé vers api.urls (vue api_home).

### URLs de l'application Public

- `/voitures/` – Liste des voitures.
- `/users/` – Liste des utilisateurs.
- `/cles/` – Liste des clés.
- `/garages/` – Liste des garages.

### URLs de l'application API

- `/api/voitures/` – Point de terminaison de l'API pour les voitures.
- `/api/users/` – Point de terminaison de l'API pour les utilisateurs.
- `/api/cles/` – Point de terminaison de l'API pour les clés.
- `/api/garages/` – Point de terminaison de l'API pour les garages.

### URLs fournis par Django :

- `/admin/` – Interface d'administration Django.

## Questions

Format :

- Question ?
    - Réponse.

### Fonctionnement de Django

- Vous disposez d'un projet Django dans lequel une application `public` a été créée. Décrivez la suite de requêtes et d'exécutions permettant l'affichage d'une page HTML `index.html` à l'URL global `/` via une application `public`, ne nécessitant pas de contexte de données. Vous décrirez la position exacte dans l'arborescence des répertoires des différents fichiers utiles à cette exécution.

    - On place le fichier `index.html` dans l'arboresence suivante, en partant de la racine du projet : `public/templates/public/index.html`. Ensuite, on définit une fonction `index` dans le ficher `views.py` du répertoire `public` telle que :
```py
from django.shortcuts import render

def index(request):
    return render(request,'public/index.html')
```
Dans le fichier `urls.py` de l'application `public` :
```py
from django.urls import path
from public.views import index

urlpatterns = [
    path('',index,name='index'),
]
```
Et dans le fichier `urls.py` principal :

```py
from django.urls import path, include

urlpatterns = [
    path('',include('public.urls')),
]
```
A la réception de la requête au chemin `/` sur l'interface où écoute le serveur web, l'application Django va examiner le fichier `urls.py` principal et reconnaître l'URL indiqué, puis va exécuter la fonction `index`, qui a été programmée pour retourner le contenu du fichier `index.html`. 
L'exécution est ainsi complétée.
- Dans quelle(s) section(s) de quel(s) fichier(s) peut-on configurer la base de données que l'on souhaite utiliser pour un projet Django ?
    - On peut configurer la base de données que l'on souhaite utiliser pour un projet Django dans le champ `DATABASES` du fichier cible de la variable d'environnement `DJANGO_SETTINGS_MODULE` du projet Django.
- Dans quel(s) fichier(s) peut-on configurer le fichier de paramètres que l'on souhaite faire utiliser par le projet Django ? Si plusieurs fichers sont à mentionner, expliquez le rôle de chaque fichier.
    - Les fichiers `manage.py` et `wsgi.py` permettent d'utiliser des fichiers de paramètres différents, via la définition dans ces fichiers de la variable d'environnement `DJANGO_SETTINGS_MODULE`. `manage.py` utilise des paramètres différents pour l'exécution des commandes (`migrate`, `makemigrations`, `runserver` notamment) et `wsgi.py` les utilise pour gérer les requêtes faites au serveur web.
- Nous nous plaçons à la racine de votre projet Django. Quel effet a l'exécution `python manage.py makemigrations` ? Et l'exécution `python manage.py migrate` ? Quel(s) fichier(s) sont mis en oeuvre pendant ces exécutions ?
    - `python manage.py makemigrations` : Cette commande crée des fichiers de migration à partir des changements effectués dans les fichiers models.py des applications listées dans `INSTALLED_APPS` du fichier de paramètres (`settings.py`). Ces fichiers de migration sont stockés dans un répertoire migrations propre à chaque application et récapitulent les modifications à appliquer à la base de données.

    - `python manage.py migrate` : Cette commande applique les migrations en les traduisant en requêtes SQL qui sont ensuite exécutées sur la base de données. Les fichiers de migration créés précédemment sont utilisés pour cette opération. Les migrations sont appliquées dans l'ordre dans lequel elles ont été créées pour assurer la cohérence de la base de données.

    - Fichiers impliqués :

        - `models.py` : Contient les définitions des modèles (tables de la base de données).
        - `migrations/` : Répertoire généré automatiquement pour chaque application, contenant les fichiers de migration.
        - `settings.py` : Spécifie les paramètres de la base de données et les applications installées.
        - `manage.py` : Permet d'exécuter les commandes de gestion Django, y compris `makemigrations` et `migrate`.


### Fonctionnement de Docker

- Expliquez l'effet et la syntaxe de ces commandes, communément vues dans des fichiers `Dockerfile` : `FROM`, `RUN`, `WORKDIR`, `EXPOSE`, `CMD`.
    - `FROM image` permet d'indiquer quelle image de conteneur de base on va utiliser. Cette image doit être disponible sur [Docker Hub](https://hub.docker.com).
    - `RUN commande à exécuter` permet d'exécuter une commande shell au sein du conteneur pendant la phase de construction de l'image.
    - `WORKDIR /répertoire` crée un dossier `répertoire` dans le conteneur et le définit comme le répertoire courant pendant la phase de construction de l'image.
    - `EXPOSE port` permet de documenter les ports sur lesquels le conteneur souhaite communiquer avec l’extérieur.
    - `CMD ["commande","à","exécuter"]` permet d'exécuter une commande au sein du conteneur à la fin de la phase de construction, au moment du démarrage du conteneur.
- Dans la définition d'un service dans le fichier `docker-compose.yml`, expliquez l'effet des mentions :

    -   ```
        ports:
            - "80:80"
        ```
        - Cela établit une correspondace entre le port 80 du conteneur et le port 80 de l’hôte via une règle NAT, ce qui rend le service accessible depuis l'extérieur du conteneur.
    -   ```
        build: 
            context: .
            dockerfile: Dockerfile.api
        ```
        - Ceci permet de spécifier le `Dockerfile` à utiliser pour la création du conteneur.
    -   ```
        depends_on:
            - web
            - api
        ```
        - Cela signifie que le service ne démarrera qu'après que les conteneurs `web` et `api` ont démarré. Cependant, cela ne garantit pas que ces services seront entièrement prêts. Il est recommandé d'utiliser des "healthchecks" pour s'en assurer.
    -   ```
        environment:
            POSTGRES_DB: ${POSTGRES_DB}
            POSTGRES_USER: ${POSTGRES_USER}
            POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
        ```
        - Cela définit des variables d'environnement dans le conteneur à partir du fichier `.env` dans le répertoire courant.

- Citez une méthode pour définir des variables d'environnement dans un conteneur.
    - La réponse au quatrième point de la question précédente propose une méthode. Ces variables peuvent également être passées dans le conteneur directement dans un Dockerfile avec l'instruction `ENV`. Une autre possibilité, peu applicable à ce cours, serait de préciser ces variables directement à l'exécution de `docker run -e DATABASE_USER=myuser -e DATABASE_PASSWORD=mypassword mycontainer`. Comme nous utilisons un fichier `docker-compose.yml`, nous ne créons pas de conteneurs via la commande `docker run`. Il peut être utile tout de même de savoir que cette possibilité existe.
- Dans un même réseau Docker, nous disposons d'un conteneur `nginx` (utilisant l'image `nginx:latest`) et d'un conteneur `web` (utilisant une image contenant un projet web Django, ayant la commande `python manage.py runserver 0.0.0.0:8000` de lancée au démarrage du conteneur). Comment adresser le serveur web tournant dans le conteneur `web` depuis le conteneur `nginx`, sans utiliser les adresses IP des conteneurs ?
    - Docker offre un serveur DNS, qui ajoute des entrées DNS par défaut qui sont le nom des conteneurs. Ce serveur DNS est accessible par tous les conteneurs. Ainsi, on peut adresser le serveur web du conteneur `web` directement via `web:8000` depuis le conteneur `nginx`.

## Notation du CC (20 pts)

### Application web Django **(6 pts+)**

#### Frontend (app `public`) **(4 pts+)**

- Une page par table pour afficher l'ensemble des données (toutes les entrées, toutes les colonnes, toutes les tables) **(2 pts)**
- Une page d'accueil pour naviguer sur les différentes listes **(1 pt)**
- La page d'administration est disponible à l'URL `/admin` **(1 pt)**
- Fonctionnalités supplémentaires (création d'objets, utilisateurs/connexion, pages pour avoir les détails d'un objet dans la liste, REST framework) **(+1 pt/fonctionnalité)**

#### API (app `api`) **(2 pts+)**

- Une page par table pour récupérer au format JSON l'ensemble des données de la table **(2 pts)**
- Fonctionnalités supplémentaires (pages pour avoir les détails d'un objet) **(+1 pt)**

### Conteneurisation avec Docker **(6 pts)**

- Q1 La configuration du proxy est correcte (correspondance sur `localhost:80`, répartition du trafic selon l'URL) **(1 pt)**
- Q2 La séparation entre les applications `public` et `api` dans leurs deux conteneurs respectifs est correcte (`settings.py` séparés, `urls.py` séparés, chargement correct des modules `settings` dans `manage.py` et `wsgi.py`, construction des images avec des `Dockerfile` corrects) **(3 pts)**
- Q3 La base de données (conteneur `db`) est correctement utilisée (`DATABASES` correctement configuré dans `settings.py`, des migrations et des chargements de fixtures sont effectués au lancement de l'un des conteneurs `public` ou `api`, chaque conteneur peut accéder aux données) **(2 pts)** 

### Schémas & Questions **(8 pts)**

- Q1 Schéma de la base de données correspondant aux `models.py` **(1 pt)**
- Q2 Schéma de l'infrastructure précisant le fonctionnement de la conteneurisation Docker **(4 pts)**
- Q3 Réponses aux questions **(3 pts)**
