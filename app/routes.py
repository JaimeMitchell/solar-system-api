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
def read_planets():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "temperature": planet.temperature
        })
    return jsonify(planets_response)
