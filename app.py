#!/usr/bin/env python
"""
mascot: a microservice for serving mascot data
"""
import json
from flask import Flask, jsonify, abort, make_response

APP = Flask(__name__)

# Load the data using a with block and specifying encoding
with open('data.json', 'r', encoding='utf-8') as file:
    MASCOTS = json.load(file)


@APP.route('/', methods=['GET'])
def get_mascots():
    """
    Function: get_mascots
    Input: none
    Returns: A list of mascot objects
    """
    return jsonify(MASCOTS)


@APP.route('/<guid>', methods=['GET'])
def get_mascot(guid):
    """
    Function: get_mascot
    Input: a mascot GUID
    Returns: The mascot object with GUID matching the input
    """
    mascot = next((m for m in MASCOTS if m['guid'] == guid), None)
    if mascot:
        return jsonify(mascot)
    abort(404)


@APP.errorhandler(404)
def not_found(error):
    """
    Function: not_found
    Input: The error
    Returns: HTTP 404 with error details
    """
    return make_response(jsonify({'error': 'Resource not found', 'details': str(error)}), 404)


if __name__ == '__main__':
    APP.run("0.0.0.0", port=8080, debug=True)
