#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.web import create_blueprint

__blueprint__name = __name__.split('.')[1:]
blueprint = create_blueprint('.'.join(__blueprint__name), __name__, static_url_path='', url_prefix='/{}'.format('/'.join(__blueprint__name[:-1])))

from utils.web import get
from utils.web.decorators import player_required
from utils.web.exceptions import PlayerRequired

def get_page():
	from flask import request
	return ' '.join([blueprint.name, request.url_rule.rule])

@blueprint.route('/', methods=['GET'])
def root_handler(error=None):
	"""Homepage route."""
	return get_page()

@blueprint.route('/rank', methods=['GET'], strict_slashes=False)
@player_required
def rank_handler():
	return get_page()
