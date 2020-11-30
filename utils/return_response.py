from flask import make_response, jsonify

def return_error_json(status=400, json={}):
    return make_response(
        jsonify(json),
        status
    )

def return_json(json):
    return make_response(
        jsonify(json),
        200
    )