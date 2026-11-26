# Gestion Cabinet Médical

Projet Django 5.2 de gestion des rendez-vous d'un cabinet médical. Les modèles métier se trouvent dans `AccountApp` (User, Doctor, Patient et Specialty) et `AppointmentApp` (Appointment). L'administration Django est configurée dans les deux applications.

## Installation locale

Python 3.12 est requis.

```powershell
py -3.12 -m venv env
.\env\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Ouvrir ensuite http://127.0.0.1:8000/admin/.

La base SQLite locale, l'environnement virtuel et les fichiers médias ne sont pas versionnés. Les migrations versionnées reconstruisent le schéma.

Pour un déploiement, définir une clé privée dans la variable d'environnement `DJANGO_SECRET_KEY` et configurer `DEBUG`, `ALLOWED_HOSTS` et les paramètres de base de données pour l'environnement ciblé.

