import os

from dotenv import load_dotenv
import io
from google.cloud import secretmanager

if os.environ.get("GOOGLE_CLOUD_PROJECT", None):
    print("Loading secrets from Secret Manager")
    # Pull secrets from Secret Manager
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")

    client = secretmanager.SecretManagerServiceClient()
    settings_name = os.environ.get("SETTINGS_NAME", "flask_settings")
    name = f"projects/{project_id}/secrets/{settings_name}/versions/latest"
    payload = client.access_secret_version(name=name).payload.data.decode("UTF-8")

    load_dotenv(stream=io.StringIO(payload))

else:
    load_dotenv()
class Config:
    DEBUG = os.environ.get('DEBUG', False)
    SECRET_KEY = 'very_very_secure_and_secret'
    # CELERY_BROKER_URL = os.getenv("CELERY_BROKER")
    # CELERY_RESULT_BACKEND = os.getenv("CELERY_BACKEND")

    if DEBUG:
        print ('debug is true')
        #### rabbit mq ####
        CELERY_BROKER_URL = os.getenv("CELERY_BROKER", 'pyamqp://guest:guest@localhost:5672//')
        CELERY_RESULT_BACKEND = os.getenv("CELERY_BACKEND", 'rpc://guest:guest@localhost:5672//')

    else:
        print ('debug is false')
        ### redis ####
        CELERY_BROKER_URL = os.getenv("CELERY_BROKER", 'redis://localhost:6379/0')
        CELERY_RESULT_BACKEND = os.getenv("CELERY_BACKEND", 'redis://localhost:6379/0')
