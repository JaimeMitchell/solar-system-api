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


@bp.route("", methods=["GET"])  # CRUD METHOD created a new endpoint that catches requests going to "" (assumed
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

#from flask import Blueprint, jsonify

# class Cat:
#     def __init__(self, id, name, color, personality):
#         self.id = id
#         self.name = name
#         self.color = color
#         self.personality = personality

# cats = [
#     Cat(1, "Luna", "grey", "naughty"),
#     Cat(2, "Orange Cat", "orange", "antagonistic"),
#     Cat(3, "Big Ears", "grey and white", "sleepy")
# ]

# bp = Blueprint("cats", __name__, url_prefix="/cats")

# @bp.route("", methods=["GET"])
# def handle_cats():
#     results_list = []
#     for cat in cats:
#         results_list.append(dict(
#             id=cat.id,
#             name=cat.name,
#             color=cat.color,
#             personality=cat.personality
#         ))
#     return jsonify(results_list)
