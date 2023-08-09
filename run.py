from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.app_context().push()

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_todolist.db"
db.init_app(app)

class Tarea(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    descripcion = db.Column(db.String(200),nullable=False)
    estado = db.Column(db.String(100),nullable=False)
    
    def __init__(self,descripcion,estado):
        self.descripcion = descripcion
        self.estado = estado
        
#esquema
ma = Marshmallow(app)
class TareaSchema(ma.Schema):
    class Meta:
        fields = ('id','descripcion','estado')
        

db.create_all()

@app.route('/')
def index():
    context = {
        'status':True,
        'content':'sevidor activo'
    }
    return jsonify(context)

@app.route('/tarea',methods=['POST'])
def set_tarea():
    descripcion = request.json['descripcion']
    estado = request.json['estado']
    
    nueva_tarea = Tarea(descripcion,estado)
    db.session.add(nueva_tarea)
    db.session.commit()
    
    context = {
        'status':True,
        'content':'registro exitoso'
    }
    
    return jsonify(context)

@app.route('/tarea',methods=['GET'])
def get_tarea():
    data = Tarea.query.all() #select * from tarea
    #serializar
    data_schema = TareaSchema(many=True)
    
    context = {
        'status':True,
        'content':data_schema.dump(data)
    }
    
    return jsonify(context)


if __name__ == "__main__":
    app.run(debug=True)
    

