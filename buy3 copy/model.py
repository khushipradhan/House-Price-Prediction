from database import db


class houses(db.Model):
    __tablename__ = 'houses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    area= db.Column(db.Integer, nullable=False)
    bhk= db.Column(db.Integer, nullable=False)
    bathroom= db.Column(db.Integer, nullable=False)
    furnishing= db.Column(db.String(50), nullable=False)
    locality= db.Column(db.String(50), nullable=False)
    parking= db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    transaction = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)

