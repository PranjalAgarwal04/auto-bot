import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate(
    'auto-bot-2559f-firebase-adminsdk-emjq1-43937ff21c.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://auto-bot-2559f-default-rtdb.asia-southeast1.firebasedatabase.app'
})

userRef = db.reference('Users/')
userRef.set({
    'name': 'Pranjal',
})
