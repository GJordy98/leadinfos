# leadinfos

Leadinfos est une application web de blog de voyage développée avec Django. Elle permet aux utilisateurs de partager leurs expériences de voyage à travers des articles et des images. ## Fonctionnalités
 - Création de compte utilisateur et authentification 
- Publication d'articles de blog avec texte et images 
- Page d'accueil affichant les articles récents
 - Page de profil utilisateur 
- Formulaire de contact 
- Design responsive utilisant Bootstrap 
## Technologies utilisées 
- Django 
- Python 
- HTML 
- CSS 
- Bootstrap 
- SQLite (base de données par défaut)

  
1.	Créez un environnement virtuel et activez-le :
python -m venv venv source venv/bin/activate # Sur Windows, utilisez venv\Scripts\activate
2.	Installez les dépendances :
pip install -r requirements.txt
3.	Effectuez les migrations :
python manage.py migrate
4.	Créez un superutilisateur :
python manage.py createsuperuser
5.	Lancez le serveur de développement :
python manage.py runserver
L'application sera accessible à l'adresse `http://127.0.0.1:8000/`.
## Structure du projet
- `travelblog/` - Configuration principale du projet Django
- `blog/` - Application Django pour la gestion des articles
- `users/` - Application Django pour la gestion des utilisateurs
- `templates/` - Templates HTML
- `static/` - Fichiers statiques (CSS, JS, images)
## Contribution :
Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.
## Licence :
Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.


