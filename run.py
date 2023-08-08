from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy

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

db.create_all()

@app.route('/')
def index():
    context = {
        'status':True,
        'content':'sevidor activo'
    }
    return jsonify(context)

if __name__ == "__main__":
    app.run(debug=True)