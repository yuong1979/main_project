## Flask

### Deployment

Deploy

```bash
gcloud app deploy flask_app.yaml
```

## Celery

### Deployment

Deploy

```bash
gcloud beta app deploy celery_flask_app.yaml
```

## Secrets

Update secrets

```bash
gcloud secrets versions add flask_settings --data-file=.env.gcloud
```