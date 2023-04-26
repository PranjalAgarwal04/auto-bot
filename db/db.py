from firebase import firebase

config = {
    'apiKey': "AIzaSyAfv3-Y-l-ZuIuDE6Crp0OB0yhq44Vlmlw",
    'authDomain': "auto-bot-2559f.firebaseapp.com",
    'databaseURL': "https://auto-bot-2559f-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "auto-bot-2559f",
    'storageBucket': "auto-bot-2559f.appspot.com",
    'messagingSenderId': "733562449081",
    'appId': "1:733562449081:web:d74bf36adb19715cfc3f68",
    'measurementId': "G-Z0VB4P9PXZ"
}

firebase = firebase.FirebaseApplication(
    "https://auto-bot-2559f-default-rtdb.asia-southeast1.firebasedatabase.app")

db = firebase.p

data = {
    "name": "Pranjal"
}

db.set(data)
