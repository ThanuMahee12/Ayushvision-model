import firebase_admin
from firebase_admin import credentials,firestore,storage
import os
import sys

sys.path.append("D:\\Research\\ayush-vision\\Util")
import Variable

cred = credentials.Certificate(Variable.firebaseKey)
firebase_admin.initialize_app(cred,{
            'storageBucket': 'ayush-vision-9z8kha.appspot.com'  # Update with your Firebase project ID
        })
store=firestore.client()
storageBudget=storage.bucket()
