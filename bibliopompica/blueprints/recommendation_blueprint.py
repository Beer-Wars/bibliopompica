from flask import Blueprint

recommendation_blueprint = Blueprint('recommendation_blueprint', __name__)

@recommendation_blueprint.route('/recommendations')
def recommendations():
    return "recommendations list"

@recommendation_blueprint.route('/recommend/<int:book>', methods=['PUT'])
def recommendation_create():
    return "new recommendation"

@recommendation_blueprint.route('/recommend/<int:book>', methods=['DELETE'])
def recommendation_delete():
    return "delete recommendation"
