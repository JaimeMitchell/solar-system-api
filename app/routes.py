from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

# INSTANIATE BLUEPRINT FOR ROUTES
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("/", strict_slashes=False, methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name=request_body["name"], description=request_body["description"], temperature=request_body["temperature"])
    db.session.add(new_planet)
    db.session.commit()
    return make_response(f"Planet #{new_planet.name} successfully created", 200)


@planets_bp.route("/", strict_slashes=False, methods=["GET"])
def read_all_planets():
    planets = Planet.query.all()
    planets_response = [planet.to_dict() for planet in planets]
    return jsonify(planets_response)
    # for planet in planets:
    #     planets_response.append({
    #         "id": planet.id,
    #         "name": planet.name,
    #         "description": planet.description,
    #         "temperature": planet.temperature
    #     })
    # NEED JSONIFY FOR LISTS (BUT NOT DICTIONARIES)


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"{planet_id} is not valid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message": f"{planet_id} can't be found"}, 404))
    return planet


@planets_bp.route("/<planet_id>", strict_slashes=False, methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return planet.to_dict(), 200


@planets_bp.route("/<planet_id>", strict_slashes=False, methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.temperature = request_body["temperature"]
    db.session.commit()
    return make_response(f"Planet #{planet.id} successfully updated", 200)


@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)
    db.session.delete(planet)
    db.session.commit()
    return make_response(f"Planet #{planet.id} successfully deleted", 200)
