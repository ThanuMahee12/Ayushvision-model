import firebase_admin
from firebase_admin import credentials
import os


cred = credentials.Certificate('D:\\Research\\ayush-vision\\config\\serviceAccountKey.json')
firebase_admin.initialize_app(cred)
