from flask import Blueprint
from app.controllers import book_controller

book_bp = Blueprint("books", __name__)

@book_bp.route("/books", methods=["POST"])
def add_book():
    """
    Adiciona um novo livro
    ---
    tags:
      - Livros
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - author
            - genre
            - year
            - title
          properties:
            author:
              type: string
              example: "George Orwell"
            genre:
              type: string
              example: "Ficção"
            year:
              type: integer
              example: 1949
            title:
              type: string
              example: "1984"
    responses:
      201:
        description: Livro adicionado com sucesso
      400:
        description: Erro de validação
    """
    return book_controller.add_book()

@book_bp.route("/books", methods=["GET"])
def get_books():
    """
    Lista todos os livros
    ---
    tags:
      - Livros
    responses:
      200:
        description: Lista de livros
    """
    return book_controller.get_books()

@book_bp.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    """
    Retorna um livro específico pelo ID
    ---
    tags:
      - Livros
    parameters:
      - in: path
        name: book_id
        type: integer
        required: true
        description: ID do livro a ser consultado
    responses:
      200:
        description: Livro encontrado com sucesso
      404:
        description: Livro não encontrado
    """
    return book_controller.get_book(book_id)

@book_bp.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    """
    Atualiza os dados de um livro
    ---
    tags:
      - Livros
    parameters:
      - in: path
        name: book_id
        type: integer
        required: true
        description: ID do livro a ser atualizado
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              example: "Novo título"
            author:
              type: string
              example: "Novo autor"
            year:
              type: integer
              example: 2024
            genre:
              type: string
              example: "Novo gênero"
    responses:
      200:
        description: Livro atualizado com sucesso
      404:
        description: Livro não encontrado
    """
    return book_controller.update_book(book_id)

@book_bp.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    """
    Remove um livro pelo ID
    ---
    tags:
      - Livros
    parameters:
      - in: path
        name: book_id
        type: integer
        required: true
        description: ID do livro a ser removido
    responses:
      200:
        description: Livro removido com sucesso
      404:
        description: Livro não encontrado
    """
    return book_controller.delete_book(book_id)