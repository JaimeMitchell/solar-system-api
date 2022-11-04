from app import db
from app.models.moon import Moon
from app.planet_routes import validate_model
from flask import Blueprint, jsonify, abort, make_response, request

moon_bp = Blueprint("moon", __name__, url_prefix="/moons")

def validate_moon(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response(
            {"message": f"{cls.__name__} {model_id} invalid"}, 400))

    moon = cls.query.get(model_id)

    if not moon:
        abort(make_response(
            {"message": f"{cls.__name__} {model_id} can't be found"}, 404))

    return moon

@moon_bp.route("/", strict_slashes=False, methods=["GET"])
def read_all_planet():

    moons = Moon.query.all()

    moons_response = []
    for moon in moons:
        moons_response.append(
            {
            "name" : moon.name,
            "description": moon.description,
            "temperature": moon.temperature
            }
        )
    return jsonify(moons_response)

@moon_bp.route("/", strict_slashes=False, methods=["POST"])
def create_moon():

    request_body = request.get_json()
    new_moon = Moon.from_dict(request_body)

    db.session.add(new_moon)
    db.session.commit()

    return make_response(jsonify(f"Moon {new_moon.name} successfully created"), 201)

@moon_bp.route("/<moon_id>/planets", methods=["POST"])
def create_book(moon_id):
    request_body = request.get_json()
    new_moon = Moon.from_dict(request_body)

    db.session.add(new_moon)
    db.session.commit()

    return make_response(jsonify(f"Book {new_moon.title} by {new_moon.author.name} successfully created"), 201)