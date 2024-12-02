import os 
GOOGLE_CLIENT_ID = os.environ.get('gclient_id')
GOOGLE_CLIENT_SECRET = os.environ.get('gclient_secret') 
SECRET_KEY = os.urandom(24)
