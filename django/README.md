# Project configuration

## Setting up necessary services

## Cloud Storage

https://cloud.google.com/appengine/docs/flexible/serving-static-files?tab=custom#serving_files_from


## Cloud SQL

https://cloud.google.com/sql/docs/mysql/connect-app-engine

> Note: Since app engine uses IPs from a pool of GCP IPs, you need to open up the firewall to allow all IPs to access the database.

## Secret Manager

1. Create a secret named `django_settings`
2. In the permissions tab, add the service account `main-project-393402@appspot.gserviceaccount.com` with the role `Secret Manager Secret Accessor`

## Django

### Deployment

Push to Google Cloud Storage

```bash
gsutil -m rsync -r ./static gs://dj-static-19234/static
```

Deploy

```bash
gcloud app deploy
```

## Celery

### Deployment

Deploy

```bash
gcloud beta app deploy celery_app.yaml
```

## Secrets

Update secrets

```bash
gcloud secrets versions add django_settings --data-file=.env.gcloud
```
