from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.app_context().push()

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_todolist.db"
db.init_app(app)

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