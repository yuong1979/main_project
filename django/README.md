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