from datetime import date
from app import db

class Assessment(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100))
  code = db.Column(db.String(10))
  deadline = db.Column(db.Date())
  description = db.Column(db.String(500))
  status = db.Column(db.Boolean())
  