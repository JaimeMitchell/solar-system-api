from flask import Blueprint, jsonify


class Planet:
    def __init__(self, id, name, description, temperature):
        self.id = id
        self.name = name
        self.description = description
        self.temperature = temperature


planets = [
    Planet(1, "Venus", "yellow-white", "1000F"),
    Planet(2, "Earth", "blue-green", "70F"),
    Planet(3, "Mars", "red", "300F")
]

bp = Blueprint("planets", __name__, url_prefix="/planets")  # ENDPOINT


# CRUD METHOD created a new endpoint that catches requests going to "" (assumed
@bp.route("", methods=["GET"])
# "/books") with the HTTP method GET
# RESPONSE BODY
def handle_planets():
    results_list = []
    for planet in planets:
        results_list.append(dict(
            id=planet.id,
            name=planet.name,
            temperature=planet.temperature
        ))
    return jsonify(results_list)

@bp.route("/<planet_id>", methods=['GET'])
def handle_planet(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "temperature": planet.temperature
            }
    pass
