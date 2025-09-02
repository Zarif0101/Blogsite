first create a virtual environment :

```
python -m venv venv
```

then activate it :

```
venv\Scripts\Activate
```

then these packages :

```
pip install django
```
```
pip install django-crispy-forms
```
```
pip install pillow
```
```
pip install crispy-bootstrap5
```
You also need to make migrations :

```
py manage.py makemigrations
```
```
py manage.py migrate
```
