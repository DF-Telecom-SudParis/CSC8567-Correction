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