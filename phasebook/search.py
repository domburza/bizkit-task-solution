from flask import Blueprint, request

from .data.search_data import USERS

import re

bp = Blueprint("search", __name__, url_prefix="/search")


# @bp.route("<query>")
@bp.route("")
def search():
    
    id = request.args.get('id',0)
    name = request.args.get('name',0)
    age = request.args.get('age',0)
    occupation = request.args.get('occupation',0)

    return search_users(request.args.to_dict(),id,name,age,occupation), 200


def search_users(args, id, name, age, occupation):
    """Search users database
    
    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    searchres = []
    temp = request.args

    for itemlol in USERS:
        for keyval in temp.keys():

            if keyval == 'age':
                if abs(int(temp[keyval])-int(itemlol[keyval])) == 1:
                    searchres.append(itemlol)
                    break

            if str(temp[keyval]) in str(itemlol[keyval]):
               searchres.append(itemlol)
               break
    
    ############ BONUS CHALLENGE SEARCH CODE ########################

    for keyval in temp.keys():
        for itemlol in USERS: 

            if keyval == 'age':
                if abs(int(temp[keyval])-int(itemlol[keyval])) == 1:
                    if itemlol not in searchres:
                        searchres.append(itemlol)
                        continue

            if str(temp[keyval]) in str(itemlol[keyval]):
               if itemlol not in searchres:
                        searchres.append(itemlol)
                        continue

    return searchres
