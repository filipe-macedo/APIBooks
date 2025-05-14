from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from flask import request, jsonify

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

#model
class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]

class Books(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]
    genre: Mapped[str]
    year: Mapped[int]

    

#criação da tabela no banco
with app.app_context():
    db.create_all()

app = Flask(__name__)

#POST
@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    new_book = Books(
        author=data["author"], 
        genre=data["genre"], 
        year=data["year"], 
        title=data["title"])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Livro adicionado com sucesso!"}), 201


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/teste")
def rota_teste():
    return "<p>Rota de teste</p>"