from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

# Best Practice: Factory Pattern : TO create all objects at one placed and use it
def create_app(config=None):
    app = Flask(__name__)
    app.config.from_pyfile(config)
    db = SQLAlchemy(app)
    ma = Marshmallow(app)
    api = Api(app)

    return (app,db,ma,api)

app,db,ma,api = create_app(config="config.py")
db.create_all()

#MODEL FILE - In prod grade project this should go under model folder
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    
    def __repr__(self):
        return '<Employee %s>' % self.name

## DB Serialization Schema
class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email')

Employee_schema = EmployeeSchema()
Employees_schema = EmployeeSchema(many=True)

#  Resources : In prod grade project this should go under model folder
class EmployeeListResource(Resource):
    
    def get(self):
        Employees = Employee.query.all()
        return Employees_schema.dump(Employees)
    
    def post(self):
        new_Employee = Employee(
            name=request.json['name'],
            email=request.json['email'],
        )
        db.session.add(new_Employee)
        db.session.commit()
        return Employee_schema.dump(new_Employee)

class EmployeeResource(Resource):
    def get(self, Employee_id):
        Employee = Employee.query.get_or_404(Employee_id)
        return Employee_schema.dump(Employee)
    def patch(self, Employee_id):
        Employee = Employee.query.get_or_404(Employee_id)
        if 'name' in request.json:
            Employee.name = request.json['name']
        if 'email' in request.json:
            Employee.email = request.json['email']
            
        db.session.commit()
        return Employee_schema.dump(Employee)
    def delete(self, Employee_id):
        Employee = Employee.query.get_or_404(Employee_id)
        db.session.delete(Employee)
        db.session.commit()
        return '', 204
class HealthCheck(Resource):  
    def get(self):
        return "Helath:OK"
    
# add resource to flask app
api.add_resource(EmployeeListResource, '/Employees')
api.add_resource(EmployeeResource, '/Employees/<int:Employee_id>')
api.add_resource(HealthCheck, '/health')
