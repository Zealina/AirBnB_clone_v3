#!/usr/bin/python3
"""Contains the index endpoints"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def index():
    """Return api status"""
    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def count_objs():
    """Return the count of objects in db"""
    count_dict = {
            'amenities': storage.count("Amenity"),
            'cities': storage.count("City"),
            'places': storage.count("Place"),
            'reviews': storage.count('Review'),
            'states': storage.count('State'),
            'users': storage.count('User')
            }
    return jsonify(count_dict)
