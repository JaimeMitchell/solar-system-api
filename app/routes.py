from flask import Blueprint, jsonify, abort, make_response
import json


class Planet:
    def __init__(self, id, name, description, temperature):
        self.id = id
        self.name = name
        self.description = description
        self.temperature = temperature

    def to_planet_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            temperature=self.temperature
        )


planets = [
    Planet(1, "Venus", "yellow-white", "1000F"),
    Planet(2, "Earth", "blue-green", "70F"),
    Planet(3, "Mars", "red", "300F")
]

bp = Blueprint("planets", __name__, url_prefix="/planets")


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} not valid"}, 400))
    for planet in planets:
        if planet.id == planet_id:
            return planet
    abort(make_response({"message": f"planet {planet_id} not found"}, 404))


@bp.route("", methods=["GET"])
def handle_planets():
    results_list = []
    for planet in planets:
        results_list.append(planet.to_planet_dict())
    return jsonify(results_list)


@bp.route("/<planet_id>", methods=["GET"])
def get_planet(planet_id):
    planet = validate_planet(planet_id)
    return jsonify(planet.to_planet_dict())
