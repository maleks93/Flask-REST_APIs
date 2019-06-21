from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        return {'message' : 'Store not found'}, 404

    def post(self,name):
        store = StoreModel.find_by_name(name)
        if store is None:
            store = StoreModel(name)
            try:
                store.save_to_db()
            except:
                return {'message' : 'Error occured while creating the store'}, 500

            return store.json(), 201

        return {'message' : "Store already exists with name '{}'".format(name)}, 400

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message' : 'Store deleted' }

class StoreList(Resource):

    def get(self):
        stores = [store.json() for store in StoreModel.query.all()]

        return {'stores' : stores}
