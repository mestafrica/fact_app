from models.base_model import *
from peewee import CharField, BooleanField, TextField, DateTimeField

from datetime import datetime

class FactModel(BaseModel):
    user = CharField(40)
    fact = TextField(20)
    is_true = BooleanField()
    timestamp = DateTimeField(default=datetime.now)
