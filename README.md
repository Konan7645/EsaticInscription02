# Application d'inscription au concours ESATIC

Application web Django permettant aux étudiants de s'inscrire au concours d'entrée de l'École Supérieure Africaine des TIC (ESATIC).

## Fonctionnalités

- Enregistrement des données des étudiants
- Upload de documents (extrait de naissance, certificat, lettre de motivation, diplôme, photo)
- Génération d'une fiche d'inscription au format PDF
- Interface d'administration pour gérer les inscriptions

## Technologies utilisées

- Django 5.2
- Bootstrap 5
- xhtml2pdf

## Installation

1. Clonez ce dépôt
   ```bash
   git clone https://github.com/votre-username/concours-esatic.git
   cd concours-esatic
   ```

2. Créez un environnement virtuel et installez les dépendances
   ```bash
   python -m venv env
   source env/bin/activate  # ou env\Scripts\activate sur Windows
   pip install -r requirements.txt
   ```

3. Appliquez les migrations
   ```bash
   python manage.py migrate
   ```

4. Créez un superutilisateur
   ```bash
   python manage.py createsuperuser
   ```

5. Lancez le serveur de développement
   ```bash
   python manage.py runserver
   ```

6. Accédez à l'application à l'adresse http://127.0.0.1:8000/

## Structure du projet

- `inscription/` : Application principale pour gérer les inscriptions
- `templates/` : Templates HTML
- `static/` : Fichiers statiques (CSS, JS, images)
- `media/` : Dossier pour stocker les documents uploadés

## Auteur

Votre Nom#django_projet
