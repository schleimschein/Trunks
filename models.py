from peewee import SqliteDatabase, Model, TextField, DateTimeField, ForeignKeyField, BooleanField
from datetime import datetime
import os

database = SqliteDatabase(os.environ["POSTGRES_URL"])

class User(Model):
    name = TextField(unique=True)
    admin = BooleanField(default=False)
    password = TextField()
    active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

    def get_id(self):
        return str(self.id)

    def is_active(self):
        return self.active

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

class Post(Model):
    title = TextField()
    description = TextField()
    content = TextField()
    tags = TextField()
    posted_by = ForeignKeyField(User, related_name='posts')
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)