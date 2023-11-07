
## Creation of a Route
from application import app, db
from flask import request, jsonify
from application.models import FriendsCharacter

def format_character(character):

    return {
        "id": character.id,
        "name": character.name,
        "age": character.age,
        "catch_phrase": character.catch_phrase
    }

@app.route("/")
def hello_world():
    return "<h1>Hello World!</h1>"

@app.route("/characters", methods=["POST"])
def create_character():

    #retrieve the body - req.body
    data = request.json
    #data -> {name: , age: } etc.
    character = FriendsCharacter(data["name"], data["age"], data["catch_phrase"])
    db.session.add(character) # -> Adds the character to a temporary queue
    db.session.commit() # -> Commits the character to the database
    ##Send back a json response. jsonify turns a JSON output into a Response object
    return jsonify(id=character.id,
                   name=character.name,
                   age=character.age,
                   catch_phrase=character.catch_phrase)

## GET Route
@app.route("/characters")
def get_characters():

    characters = FriendsCharacter.query.all()
    character_list = []
    for character in characters:
        character_list.append(format_character(character))

    return {"characters": character_list}

@app.route("/characters/<id>")
def get_character_by_id(id):
    character = FriendsCharacter.query.filter_by(id=id).first()  ##.all() is another possible query here
    return jsonify(id=character.id,
                   name=character.name,
                   age=character.age,
                   catch_phrase=character.catch_phrase)

@app.route("/characters/<id>", methods=["DELETE"])
def delete_character(id):
    character = FriendsCharacter.query.filter_by(id=id).first()  ##.all() is another possible query here
    db.session.delete(character)
    db.session.commit()
    return "Character deleted!"

@app.route("/characters/<id>", methods=["PATCH"])
def update_character(id):
    
    data = request.json
    character = FriendsCharacter.query.filter_by(id=id)  ##.all() is another possible query here
    character.update(dict(name=data["name"],
                          age=data["age"],
                          catch_phrase=data["catch_phrase"]))
    db.session.commit()
    updated_character = character.first()

    return jsonify(id=updated_character.id,
                   name=updated_character.name,
                   age=updated_character.age,
                   catch_phrase=updated_character.catch_phrase)