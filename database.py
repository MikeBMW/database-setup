import mysql.connector

config = {
    'user': 'root',
    'password': 'Nix19789',
    'host': 'localhost',
    'database': 'mike'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

