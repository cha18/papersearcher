from flask import Blueprint, request, jsonify
from .db import *

sort = Blueprint('sort', __name__)


@sort.route('/')
def home():
    return "<h1> Pastpaper API </h1> <h3> /search - find papers that match query </h3> <h3> /paper - find paper that matches paper code </h3>"

@sort.route('/search')
def q_results():
    #example: 127.0.0.1:5000/search?order=-1&field=content&query=growth&subject=economics
    sort = request.args.get('order') #-1 => ascending, -1 => descending
    field = request.args.get('field') #content, subject_code, qno
    query = request.args.get('query') #search term
    subject = request.args.get('subject') #subject can be a subject OR will return all subjects if not mentioned
    ptype = request.args.get('type') 

    if ptype in ['false', '0', 'false']:
        ptype = False
    else:
        ptype = None

    if sort is None: sort = -1
    result = jsonify(search_table("papers", paperstable, field, query, sort, subject, ptype))
    return result

@sort.route('/paper')
def get_paper():
    #example: 127.0.0.1:5000/
    pcode = request.args.get('pcode') #papercode

    result = jsonify(find_paper("papers", paperstable, pcode))
    return result