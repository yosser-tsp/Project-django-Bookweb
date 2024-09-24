# la liste des chemins URL

## api

### Auteurs (`authors`)

- `GET api/authors/` - Lister tous les auteurs
- `POST api/authors/` - Créer un nouvel auteur
- `GET api/authors/<id>/` - Récupérer un auteur spécifique
- `PUT api/authors/<id>/` - Mettre à jour un auteur spécifique
- `DELETE api/authors/<id>/` - Supprimer un auteur spécifique

### Livres (`books`)

- `GET api/books/` - Lister tous les livres
- `POST api/books/` - Créer un nouveau livre
- `GET api/books/<id>/` - Récupérer un livre spécifique
- `PUT api/books/<id>/` - Mettre à jour un livre spécifique
- `DELETE api/books/<id>/` - Supprimer un livre spécifique

### Critiques (`reviews`)

- `GET api/reviews/` - Lister toutes les critiques
- `POST api/reviews/` - Créer une nouvelle critique
- `GET api/reviews/<id>/` - Récupérer une critique spécifique
- `PUT api/reviews/<id>/` - Mettre à jour une critique spécifique
- `DELETE api/reviews/<id>/` - Supprimer une critique spécifique

## public

### Index
   - `GET public/` - Afficher la page d'accueil (vue `index`).
   
### livre détails
   - `GET public/<int:id>/` - Afficher les détails d'un livre spécifique (vue `detail`), où `<int:id>` est l'identifiant de livre.


# Réponses aux questions sur le fonctionnement de Django

## 1. Affichage d'une page HTML `index.html` à l'URL `/`

Pour afficher une page HTML `index.html` à l'URL globale `/` via une application publique dans un projet Django, voici les étapes à suivre :

### a. Création de l'application
Exécutez la commande suivante pour créer une application nommée `public` :

 ```bash
     python manage.py startapp public
 ```

### b. Arborescence des répertoires

L'arborescence des répertoires devrait ressembler à ceci :

```
 myproject/
         ├── manage.py
         ├── myproject/
         │   ├── __init__.py
         │   ├── settings.py
         │   ├── urls.py
         │   └── wsgi.py
         └── public/
             ├── __init__.py
             ├── admin.py
             ├── apps.py
             ├── migrations/
             ├── models.py
             ├── tests.py
             ├── views.py
             └── templates/
                 └── public/
                     └── index.html
```

### c. Création de la vue

Création d'une vue dans `public/views.py` :

   ```python
   from django.shortcuts import render

   def index(request):
       return render(request, 'public/index.html')
   ```

### d. Configuration des URL

   Créez un fichier `urls.py` dans le dossier `public` si ce n'est pas déjà fait :
   ```python
   from django.urls import path
   from .views import index

   urlpatterns = [
       path('', index, name='index'),
   ]
   ```

### e. Inclusion des URLs dans le projet

   Modifiez `urls.py` dans le répertoire principal du projet :
   ```python
   from django.contrib import admin
   from django.urls import include, path

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('public.urls')),  
   ]
   ```

## 2. Configuration de la base de données

La configuration de la base de données dans un projet Django se fait dans le fichier suivant :

- **Fichier** : `mon_projet/settings.py`

### Exemple de configuration :

Dans le fichier `settings.py`, vous trouverez une section appelée `DATABASES` :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bookdb',  # Name of your PostgreSQL database
        'USER': 'yosser',  # PostgreSQL username
        'PASSWORD': '2021',  # PostgreSQL password
        'HOST': 'db',  # Database host
        'PORT': '5432',  # Port number (default PostgreSQL port)
    }
}
```

## 3. Configuration du fichier de paramètres

Les fichiers qui peuvent être utilisés pour configurer les paramètres d'un projet Django comprennent :

- **Fichier principal** : `mon_projet/settings.py`
  - Ce fichier contient la configuration générale du projet, y compris la base de données, les applications installées, les middleware, les URL, etc.

## 4. Exécution des commandes `makemigrations` et `migrate`

### a. `python manage.py makemigrations`

- **Effet** : Cette commande crée des fichiers de migration dans le dossier `migrations` de chaque application. Ces fichiers contiennent les instructions nécessaires pour appliquer les modifications des modèles à la base de données.

- **Fichiers concernés** : Les fichiers générés se trouvent dans le répertoire `migrations` de votre application (par exemple, `public/migrations/0001_initial.py`).

### b. `python manage.py migrate`

- **Effet** : Cette commande applique les migrations à la base de données. Elle crée ou modifie les tables et les colonnes en fonction des modèles définis dans vos fichiers `models.py`.

- **Fichiers concernés** : Les fichiers de migration précédemment générés, ainsi que `mon_projet/settings.py` (qui contient la configuration de la base de données).


# Réponses aux questions sur le fonctionnement de Docker

## Commandes Dockerfile

### 1. FROM
- **Effet** : Indique l'image de base à partir de laquelle construire le conteneur.
- **Syntaxe** :
  ```dockerfile
  FROM <image>[:<tag>]
  ```
- **Exemple** :
  ```dockerfile
  FROM python:3.12

  ```

### 2. RUN
- **Effet** : Exécute des commandes dans le conteneur pendant le processus de construction.
- **Syntaxe** :
  ```dockerfile
  RUN <command>
  ```
- **Exemple** :
  ```dockerfile
  RUN pip install --no-cache-dir -r requirements.txt
  ```

### 3. WORKDIR
- **Effet** : Définit le répertoire de travail pour les instructions suivantes.
- **Syntaxe** :
  ```dockerfile
  WORKDIR <path>
  ```
- **Exemple** :
  ```dockerfile
  WORKDIR /app
  ```

### 4. EXPOSE
- **Effet** : Indique que le conteneur écoute sur le port spécifié.
- **Syntaxe** :
  ```dockerfile
  EXPOSE <port> [<port>/<protocol>...]
  ```
- **Exemple** :
  ```dockerfile
  EXPOSE 8000
  ```

### 5. CMD
- **Effet** : Définit la commande par défaut à exécuter lorsque le conteneur démarre.
- **Syntaxe** :
  ```dockerfile
  CMD ["executable","param1","param2"]
  ```
- **Exemple** :
  ```dockerfile
  CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
  ```

## Directives dans docker-compose.yml

### 1. ports: - "80:80"
- **Effet** : Mappe le port 80 de l'hôte au port 80 du conteneur.

### 2. build:
- **context: .**
  - **Effet** : Définit le contexte de construction.
- **dockerfile: Dockerfile.api**
  - **Effet** : Spécifie le nom du fichier `Dockerfile` à utiliser.
- **Exemple** :
  ```yaml
  build:
    context: .
    dockerfile: Dockerfile.api
  ```

### 3. depends_on:
- **Effet** : Indique que le service dépend des autres services listés.
- **Exemple** :
  ```yaml
  depends_on:
    - web
    - api
  ```

### 4. environment:
- **Effet** : Définit les variables d'environnement pour le conteneur.
- **Exemple** :
  ```yaml
  environment:
    POSTGRES_DB: ${POSTGRES_DB}
    POSTGRES_USER: ${POSTGRES_USER}
    POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
  ```

## Méthode pour définir des variables d'environnement dans un conteneur
Utiliser la section `environment` dans le fichier `docker-compose.yml` .

## Accès à un serveur web dans un réseau Docker
Pour adresser le serveur web depuis le conteneur nginx, utiliser le nom de service :

### Exemple de configuration Nginx :
```nginx
server {
    listen 80;
    location / {
        proxy_pass http://web:8000;  # "web" est le nom du service
    }
}
```
