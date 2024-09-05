<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/fr/thumb/1/1d/Logo_T%C3%A9l%C3%A9com_SudParis.svg/153px-Logo_T%C3%A9l%C3%A9com_SudParis.svg.png" alt="TSP logo">
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
    <img src="https://github.com/user-attachments/assets/877dfc8f-ae0b-41e0-a934-19480d839d0c" alt="Infra à reproduire">
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