from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# ("/",strict_slashes=False,methods=["POST"])
# strict_slashes can use (or not) slash after endpoint!


@planets_bp.route("/", strict_slashes=False, methods=["POST"])
def create_planets():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        temperature=request_body["temperature"])
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successful", 201)


@planets_bp.route("/", strict_slashes=False, methods=["GET"])
def handle_planets():
    planets = Planet.query.all()  # response body from request
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "temperature": planet.temperature
        })
    return jsonify(planets_response)


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"{planet_id} is not valid"}, 400))
    planet = Planet.query.get(planet_id)
    if not planet:
        abort(make_response({"message": f"{planet_id} can't be found"}, 404))
    return planet  # this returns the query response body


@planets_bp.route("/<planet_id>", strict_slashes=False, methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "temperature": planet.temperature
    }
