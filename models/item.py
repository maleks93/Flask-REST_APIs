from db import db

class ItemModel(db.Model):

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80)) # max size of name is 80 chars
    price = db.Column(db.Float(precision=2)) # price is float with precision 2 e.g. 97.89

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {"name" : self.name, "price" : self.price}

    def save_to_db(self): # Used for both create and update operations
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return ItemModel.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name LIMIT 1;
