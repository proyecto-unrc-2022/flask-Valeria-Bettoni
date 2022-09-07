from flask import Flask, jsonify, request, Response

app = Flask(__name__)

USERS = {}

@app.route('/')
def index():
    return 'Index Page'

@app.route("/users/<username>", methods=['GET'])
def access_users(username):
    if request.method == 'GET':
        user_details = USERS.get(username)
        if user_details:
            return jsonify(user_details)
        else:
            return Response(status=404)

#New user scenario -----------------------------------
@app.route("/users/newuser", methods=['POST'])
def newuser():
    if request.method == 'POST':
        USERS.update(request.json)
        return jsonify(USERS)
    else:
        return Response(status=404)

#Update a user from USERS scenario --------------------
@app.route("/users/update/<username>", methods=['PUT'])
def updateuser(username):
    if request.method == 'PUT':
        USERS.update({username : request.json})
        return jsonify(USERS.get(username))
    else:
        return Response(status=404)

#Delete a existing user scenario -----------------------
@app.route("/users/delete/<username>", methods=['DELETE'])
def deleteuser(username):
    if request.method == 'DELETE':
        user_info = USERS.get(username)
        USERS.pop(username)
        return jsonify(USERS)
    else:
        return Response(status=404)

#List all users escenario
@app.route("/users/all/<allusers>", methods=['GET'])
def all_users(allusers):
    if request.method == 'GET':
        return jsonify(allusers)
    else:
        return Response(status=404)





if __name__ == "__main__":
    app.run()
