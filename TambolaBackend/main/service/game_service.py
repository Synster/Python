"""
Game Service

ask (c) 2020. All rights reserved.
"""
from flask_socketio import SocketIO
from flask import Flask, jsonify, abort, make_response, Response
from flask_httpauth import HTTPBasicAuth
from flask_restful import Api, Resource, reqparse, fields, marshal

app = Flask(__name__, static_url_path="")
api = Api(app)
auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    if username == 'admin':
        return 'admin'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'message': 'Unauthorized access'}), 403)


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

task_fields = {
    'title': fields.String,
    'description': fields.String,
    'done': fields.Boolean,
    'uri': fields.Url('task')
}


class TicketsAPI(Resource):
    #decorators = [auth.login_required]

    def __init__(self):
        self.req_parser = reqparse.RequestParser()
        self.req_parser.add_argument('title', type=str, required=True,
                                     help='No task title provided',
                                     location='json')
        self.req_parser.add_argument('description', type=str, default="",
                                     location='json')
        super(TaskListAPI, self).__init__()

    def get(self):
        return {'tasks': [marshal(task, task_fields) for task in tasks]}

    def post(self):
        args = self.req_parser.parse_args()
        task = {
            'id': tasks[-1]['id'] + 1 if len(tasks) > 0 else 1,
            'title': args['title'],
            'description': args['description'],
            'done': False
        }
        tasks.append(task)
        return {'task': marshal(task, task_fields)}, 201


class TicketAPI(Resource):
    #decorators = [auth.login_required]

    def __init__(self):
        self.req_parse = reqparse.RequestParser()
        self.req_parse.add_argument('name', type=str, location='json')
        self.req_parse.add_argument('type', type=str, location='json')
        self.req_parse.add_argument('status', type=str, location='json')
        self.req_parse.add_argument('price', type=int, location='json')
        super(TicketAPI, self).__init__()

    def get_ticket(self, ticket_no):
        ticket = [ticket for ticket in self.get_tickets() if ticket.get_ticket_no() == ticket_no]
        if ticket:
            return ticket[0]
        else:
            return abort(Response("Ticket not found"))

    def put(self, id):
        task = [task for task in tasks if task['id'] == id]
        if len(task) == 0:
            abort(404)
        task = task[0]
        args = self.req_parse.parse_args()
        for k, v in args.items():
            if v is not None:
                task[k] = v
        return {'task': marshal(task, task_fields)}

    def delete(self, id):
        task = [task for task in tasks if task['id'] == id]
        if len(task) == 0:
            abort(404)
        tasks.remove(task[0])
        return {'result': True}


# api.add_resource(WelcomeAPI, '/', endpoint='')
api.add_resource(TaskListAPI, '/todo/api/v1.0/tasks', endpoint='tasks')
api.add_resource(GameAPI, '/todo/api/v1.0/tasks/<int:id>', endpoint='task')

if __name__ == '__main__':
    app.run()