from flask import Blueprint, request, jsonify
from .db import *

sort = Blueprint('sort', __name__)

@sort.route('/search')
def q_results():
    #example: 127.0.0.1:5000/search?order=-1&field=content&query=growth&subject=economics
    sort = request.args.get('order') #-1 => ascending, -1 => descending
    field = request.args.get('field') #content, papercode, qno
    query = request.args.get('query') #search term
    subject = request.args.get('subject') #subject can be a subject OR will return all subjects if not mentioned
    ptype = request.args.get('type') #subject can be a subject OR will return all subjects if not mentioned

    if sort is None: sort = -1
    result = jsonify(search_table("questions", questionstable, field, query, sort, subject, ptype))
    return result

@sort.route('/paper')
def get_paper():
    #example: 127.0.0.1:5000/
    pcode = request.args.get('pcode') #papercode

    result = jsonify(find_paper("questions", questionstable, pcode))
    return result