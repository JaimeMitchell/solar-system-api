from flask import Blueprint, jsonify, abort, make_response


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


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response(
            {"message": f"planet {planet_id} is not valid"}, 400))
    for planet in planets:
        if planet.id == planet_id:
            return(planet)
    abort(make_response(
        {"message": f"planet {planet_id} does not exist"}, 404))


@bp.route("/<planet_id>", methods=['GET'])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)
    return dict(id=planet.id, name=planet.name, temperature=planet.temperature)
