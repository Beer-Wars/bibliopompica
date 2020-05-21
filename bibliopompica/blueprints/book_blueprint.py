from flask import Blueprint

book_blueprint = Blueprint('book_blueprint', __name__)

@book_blueprint.route('/books')
def books():
    return "books list"

@book_blueprint.route('/books', methods=['PUT'])
def book_create():
    return "new book"

@book_blueprint.route('/books/<int:identifier>', methods=['GET'])
def book(identifier):
    return identifier

@book_blueprint.route('/book/<int:identifier>', methods=['POST'])
def book_update(identifier):
    return identifier

@book_blueprint.route('/book/<int:identifier>', methods=['DELETE'])
def book_delete(identifier):
    return identifier
