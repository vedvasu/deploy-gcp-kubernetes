## Containerized Django Application for ML Model Deployment
Deploying gpt2-medium model for Text Generation from the Hugging Face library.

### Technology used
- ML model and get the prediction code - **Hugging Face, gpt2-medium**
- Service to expose APIs - **Django**
- Database to store input and predictions - **Sqlite3**
- Containerized application - **Docker**
- Deploy the containerized application - **Kubernetes**
  - [Blog to deploy the service on Kubernetes Cluster](https://medium.com/p/26e2b16426cd/edit)

### Directory Structure
```commandline
.
├── README.md
├── django_app                         # Django Application
│   ├── db.sqlite3
│   ├── gpt2                           # GPT2 Application
│   │   ├── __pycache__
│   │   │   ├── admin.cpython-39.pyc
│   │   │   ├── apps.cpython-39.pyc
│   │   │   ├── models.cpython-39.pyc
│   │   │   └── views.cpython-39.pyc
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   ├── models.py                  # Database Schema
│   │   ├── templates
│   │   │   ├── index.html
│   │   │   └── jsonrender.html
│   │   ├── tests.py
│   │   └── views.py                   # Text Generation API
│   ├── manage.py
│   ├── requirements.txt
│   └── service                        # Django API Service
│       ├── asgi.py
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
└── docker                             # Docker Image
    └── Dockerfile
```

### Project Setup (API Service)

- **Clone the repository:**
  - `git clone https://github.com/vedvasu/deploy-gcp-kubernetes.git`
  

- **Create Virtual Environment:**
  - `cd deploy-gcp-kubernetes`
  - `python3 -m pip install --user virtualenv`
  - `python3 -m venv venv`
  - `source venv/bin/activate`


- **Install Requirements:**
  - `cd django_app`
  - `pip install --upgrade pip`
  - `pip install -r requirements.txt`


- **Run DB Migrations:**
  - `python manage.py makemigrations gpt2`
  - `python manage.py migrate`


- **Create a django superuser for access explorer:**
  - `export DJANGO_SUPERUSER_USERNAME "username"`
  - `export DJANGO_SUPERUSER_PASSWORD "password"`
  - `export DJANGO_SUPERUSER_EMAIL "email@gmail.com"`
  - `python manage.py createsuperuser --noinput`
  

### Test the APIs

- **Test API on localhost**
  - `python manage.py runserver` 
  - Try the model API - http://127.0.0.1:8000/generate/
  - Try the explorer API - http://127.0.0.1:8000/explorer/play
    - SELECT * from gpt2_GeneratedText

- **Test the docker application**
  - Install the docker from here and launch the docker on your local machine. 
  - Running `docker ps` would confirm the installation.  
  - From inside the `django_app` directory build the docker image 
    - `docker build -f ../docker/Dockerfile -t django-app:latest .`
    - `docker images`
  - Run application
    - `docker run -p 8000:8000 django-app`
  - Try the model API - http://127.0.0.1:8000/generate/
