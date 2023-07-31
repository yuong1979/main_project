###########################################
######### Running django ##################
###########################################

###### Running local ###### 

On terminal 1 cmd:
1. `git clone xxx`
2. `cd main_project/django`
3. `source venv/bin/activate`
4. `pip install -r requirements.txt`
5. Change debug to TRUE in settings.py in Django
6. `python3 manage.py makemigrations`
7. `python3 manage.py migrate`
8. `python3 manage.py createsuperuser`
9. `python3 manage.py runserver`

On terminal 2 cmd:
1. `sudo systemctl enable rabbitmq-server`
2. `sudo systemctl start rabbitmq-server`
3. `sudo systemctl status rabbitmq-server`

On terminal 3 cmd:
1. `celery -A core worker -B -l INFO` (If you want to run both separately, the code is `celery -A core worker -l info --pool=solo` and `celery -A core beat -l info`)

On URL: http://127.0.0.1:8000/reviews - test send of email




###### Running production ###### 

On terminal 1 cmd:
1. `git clone xxx`
2. `cd main_project/django`
3. `source venv/bin/activate`
4. `pip install -r requirements.txt`

### deploy app and celery both together - create secrets/sql/cloud storage (BELOW) if not yet created
deploy app
```bash
gcloud app deploy app.yaml celery_app.yaml
```


## Update Secrets - if no secrets set up yet
```bash
gcloud secrets versions add django_settings --data-file=.env.gcloud
```
Secret Manager
1. search for secret manager and create a new version
2. paste all the .env details into the secret manager and enable it



## Create a new sql instance / database on cloud sql - if no sql set up yet
https://cloud.google.com/sql/docs/mysql/connect-app-engine
Cloud sql
1. search for "cloud sql" and create a new instance
2. for each new instance - public ip - django settings sql - HOST
3. Go to 'Users' and create a new user and password - USER - django settings sql - PASSWORD
4. Go to 'Connections' - networking and "add a network" 0.0.0.0/0 so it can be access from public
5. Go to 'Databases' and create a new database - django settings sql - NAME
6. Make changes to the .env to update the SQL connections, PORT - 5432




## Create and set up Google Cloud Storage  -  https://cloud.google.com/appengine/docs/flexible/serving-static-files?tab=custom#serving_files_from

## avoid setting up the new bucket on the GUI, just do it via command line(Below), I tried GUI and it doesnt work
create a new bucket
```bash
gsutil mb gs://dj-static-19236
or 
gsutil mb gs://<NAME>
```

grant access to items in bucket
```bash
gsutil defacl set public-read gs://dj-static-19236
or 
gsutil defacl set public-read gs://<NAME>
```
upload items to bucket
```bash
gsutil -m rsync -r ./static gs://dj-static-19236/static
or
gsutil -m rsync -r ./static gs://<NAME>
```










