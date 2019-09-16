# Happy Elastic Search
Dit voorbeeld beschrijft hoe data geschreven kan worden in Elastic Search en gevisualiseerd kan worden.

### Aanmaken Python virtual omgeving
```
$ virtualenv -p `which python3` venv --always-copy
$ source venv/bin/activate
$ pip install -r requirements.txt
````

### Packages installeren
```
$ pip install <name-of-package>
$ pip freeze > requirements.txt
```

### Starten webserver op poort 8080
```
$ uvicorn app.main:app --reload --port 8080
```

### Checken codestyle
```
$ pylint app
```

### Uitvoeren unit tests
```
$ pytest
```
