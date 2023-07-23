# Django

## Deployment

Push to Google Cloud Storage

```bash
gsutil -m rsync -r ./static gs://dj-static-19234/static
```

Deploy

```bash
gcloud app deploy
```