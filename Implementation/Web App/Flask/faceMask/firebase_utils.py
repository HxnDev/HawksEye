import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    cred = credentials.Certificate("firebase-adminsdk.json")
    firebase_admin.initialize_app(cred)

def add_data(type, time=firestore.SERVER_TIMESTAMP):

    db = firestore.client()

    data = {
        u'time': time,
        u'type': type
    }

    doc_ref = db.collection('detections')
    doc_ref.add(data)
