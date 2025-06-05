from mongoengine import Document, StringField, IntField, EmailField

class User(Document):
    username = StringField(required=True, unique=True, max_length=150)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)

class GamePiece(Document):
    name = StringField(required=True, choices=["ship", "soldier", "elephant"])
    movement = IntField(required=True)