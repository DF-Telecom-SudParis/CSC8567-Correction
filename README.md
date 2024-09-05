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

### Fonctionnement de Django

- Vous disposez d'un projet Django dans lequel une application `public` a été créée. Décrivez la suite de requêtes et d'exécutions permettant l'affichage d'une page HTML `index.html` à l'URL global `/` via une application `public`, ne nécessitant pas de contexte de données. Vous décrirez la position exacte dans l'arborescence des répertoires des différents fichiers utiles à cette exécution.
- Dans quelle(s) section(s) de quel(s) fichier(s) peut-on configurer la base de données que l'on souhaite utiliser pour un projet Django ?
- Dans quel(s) fichier(s) peut-on configurer le fichier de paramètres que l'on souhaite utiliser pour le projet Django ? S'il y a plusieurs fichers, expliquez le rôle de chaque fichier dans le projet.
- Nous nous plaçons à la racine de votre projet Django. Quel effet a l'exécution `python manage.py makemigrations` ? Et l'exécution `python manage.py migrate` ? Quel(s) fichier(s) sont mis en oeuvre pendant ces exécutions ?

### Fonctionnement de Docker

- Expliquez l'effet de ces commandes, communément vues dans des fichiers `Dockerfile` : `FROM`, `RUN`, `WORKDIR`, `EXPOSE`, `CMD`, `ENTRYPOINT`.
- Dans la définition d'un service dans le fichier `docker-compose.yml`, expliquez l'effet des mentions :
1.
```
ports:
    - "80:80"
```
2.
```
build: 
    context: .
    dockerfile: Dockerfile.api
```
3.
```
depends_on:
    - web
    - api
```
4.
```
environment:
    POSTGRES_DB: ${POSTGRES_DB}
    POSTGRES_USER: ${POSTGRES_USER}
    POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
```
- Citez une méthode pour définir des variables d'environnement dans un conteneur.
- Dans un même réseau Docker, nous disposons d'un conteneur `nginx` (utilisant l'image `nginx:latest`) et d'un conteneur `web` (utilisant une image contenant un projet web Django, ayant la commande `python manage.py runserver 0.0.0.0:8000` de lancée au démarrage du conteneur). Comment adresser le conteneur `web` depuis le conteneur `nginx` ?

## Notation du CC (NON FIXE, 20 pts)

### Application web Django **(6 pts+)**

#### Frontend (app `public`) **(4 pts+)**

- Une page par table pour afficher l'ensemble des données (toutes les entrées, toutes les colonnes, toutes les tables) **(2 pts)**
- Une page d'accueil pour naviguer sur les différentes listes **(1 pt)**
- La page d'administration est disponible à l'URL `/admin` **(1 pt)**
- Fonctionnalités supplémentaires (création d'objets, utilisateurs/connexion, pages pour avoir les détails d'un objet dans la liste) **(+1 pt/fonctionnalité)**

#### API (app `api`) **(2 pts+)**

- Une page par table pour récupérer au format JSON l'ensemble des données de la table **(2 pts)**
- Fonctionnalités supplémentaires (pages pour avoir les détails d'un objet) **(+1 pt)**

### Conteneurisation avec Docker **(6 pts)**

- La configuration du proxy est correcte (écoute sur `localhost:80`, répartition du trafic selon l'URL) **(1 pt)**
- La séparation entre les applications `public` et `api` dans leurs deux conteneurs respectifs est correcte (`settings.py` séparés, `urls.py` séparés, chargement correct des modules `settings` dans `manage.py` et `wsgi.py`, construction des images avec des `Dockerfile` corrects) **(3 pts)**
- La base de données (conteneur `db`) est correctement utilisée (`DATABASES` correctement configuré dans `settings.py`, des migrations et des chargements de fixtures sont effectués au lancement de l'un des conteneurs `public` ou `api`, chaque conteneur peut accéder aux données) **(2 pts)**

### Schémas & Questions **(8 pts)**

- Schéma de la base de données correspondant aux `models.py` **(1 pt)**
- Schéma de l'infrastructure précisant le fonctionnement de la conteneurisation Docker **(4 pts)**
- Réponses aux questions **(3 pts)**
