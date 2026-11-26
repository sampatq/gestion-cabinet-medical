

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

L
