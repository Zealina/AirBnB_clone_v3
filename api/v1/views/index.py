#!/usr/bin/python3
"""Contains the index endpoints"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def index():
    """Return api status"""
    return jsonify({'status': 'OK'})
