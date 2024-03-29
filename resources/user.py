from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field is mandatory!"
    )

    parser.add_argument('password',
        type=str,
        required=True,
        help="This field is mandatory!"
    )

    def post(self):

        data = self.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message" : "User already exists!"}, 400

        user = UserModel(data['username'], data['password']) #UserModel(**data)
        user.save_to_db()

        return {"message" : "User created successfully!"}, 201
