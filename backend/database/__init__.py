"""Database Endpoints"""

from flask import Blueprint, request, jsonify
from bson.json_util import dumps
from backend.embed import embed
from .db_utils import insert, get_all, get_search

db = Blueprint("db", __name__)


@db.post("/insert")
def insert_url():
    url = request.json["url"]
    inserted_id = insert(url)

    if not inserted_id:
        return jsonify({"message": "Could not insert into the database"})

    return jsonify({"inserted_id": str(inserted_id)})


@db.route("/bookmarks", methods=["GET"])
def get_all_bookmarks():
    bookmarks = get_all()
    return jsonify(dumps(bookmarks))


@db.post("/search")
def search_bookmarks():
    search_criteria = request.json["search"]
    search_embedding = embed(search_criteria)
    bookmarks = get_search(search_embedding)
    return jsonify(dumps(bookmarks))
