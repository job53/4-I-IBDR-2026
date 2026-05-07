from flask import Flask, request
from flask_restful import Api, Resource
from flasgger import Swagger, swag_from

from MyDataBase import MyDatabase
from Constants import Constants
from CRUD import CRUD

app = Flask(__name__)
api = Api(app)

# Configuring Swagger
app.config['SWAGGER'] = {
    'title': 'My First REST API',
    'uiversion': 3
}
swagger = Swagger(app)

class Welcome(Resource):
    @swag_from({
        'responses': {
            200: {
                'description': 'A status code 200 means successful and returns a message.',
                'content': {
                    'application/json': {
                        'examples': {
                            'example1': {
                                'summary': 'Successful response',
                                'value': {'message': 'Welcome GeeksforGeeks!!'}
                            }
                        }
                    }
                }
            }
        }
    })
    def get(self):
        """
        This is an example endpoint which returns a simple message.
        """
        return {'message': 'Welcome Database Implementators!!'}

class Items(Resource):
    @swag_from({
        'responses': {
            200: {
                'description': 'A status code 200 means successful and returns a list of items.',
                'content': {
                    'application/json': {
                        'examples': {
                            'example1': {
                                'summary': 'Successful response',
                                'value': {'items': ['Item 1', 'Item 2', 'Item 3']}
                            }
                        }
                    }
                }
            }
        }
    })
    def get(self):
        """
        This endpoint returns a list of items.
        """
        crud = CRUD()
        #print(test.query("INSERT INTO mytest (id) VALUES (3)"))
        items = crud.testing()
        return {'items': items}

class Profile(Resource):
    @swag_from({
        'parameters':[
            {
                'name' : 'email',
                'in' : 'query',
                'type': 'string',
                'required' : True
            },
            {
                'name' : 'token',
                'in' : 'query',
                'type': 'string',
                'required' : True
            }
                      
                      ],
        'responses': {
            200: {
                'description': 'A status code 200 means successful and returns a list of items.',
                'content': {
                    'application/json': {
                        'examples': {
                            'example1': {
                                'summary': 'Successful response',
                                'value': {'items': ['Item 1', 'Item 2', 'Item 3', 'Item 4']}
                            }
                        }
                    }
                }
            }
        }
    })
    def get(self, email, token):
        """
        This endpoint returns a list of items.
        """
        email = request.args.get('email')
        token = request.args.get('token')
        print (email)
        print(token)
        crud = CRUD()
        #print(test.query("INSERT INTO mytest (id) VALUES (3)"))
        items = crud.get_profile(email,token)
        return {'items': items}

class Profile1(Resource):
    
    @swag_from({
        'parameters': [
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'name': {'type': 'string', 'example': 'juan antonio ortega sandoval'},
                        'alias': {'type': 'string', 'example': 'jaos'},
                        'token': {'type': 'string', 'example': 'jaos2026'},
                        'birthdate': {'type': 'string', 'format': 'date', 'example': '1987-06-03'},
                        'email': {'type': 'string', 'example': 'antonio.ortega@cbtis.edu.mx'},
                        'lang_code': {'type': 'string', 'example': 'ES'},
                        'routine': {'type': 'integer', 'example': '1'},
                        'alarm': {'type': 'integer', 'example': '1'},
                        'inactivity_time': {'type': 'integer', 'example': '1'},
                        'name': {'type': 'string', 'example': '1'},
                    }
                
                }
            }
        ],
        'responses': {
            200: {
                'description': 'A status code 200 means successful and returns a list of items.',
                'content': {
                    'application/json': {
                        'examples': {
                            'example1': {
                                'summary': 'Successful response',
                                'value': {'items': ['Item 1', 'Item 2', 'Item 3']}
                            }
                        }
                    }
                }
            }
        }
    })
    def get(self):
        """
        This endpoint returns a list of items.
        """
        crud = CRUD()
        #print(test.query("INSERT INTO mytest (id) VALUES (3)"))
        items = crud.testing()
        return {'Profile1': Profile1}


api.add_resource(Welcome, '/')
api.add_resource(Items, '/items')
api.add_resource(Profile, '/profile/<string:email>/<string:token>')

if __name__ == '__main__':
    app.run(debug=True)