import os
from flask import (
    Flask, flash, render_template,
     redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONOG_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_shrink")
def get_shrink():
    shrinkrs = mongo.db.resolvedDb.find().limit(5).sort(
        "amount_lost_value"
    )
    shrink = mongo.db.shrinkDB.find().limit(5).sort(
        "amount_lost_value", -1,)
    return render_template(
        "shrink.html", shrinkDB=shrink, shrinkresolved=shrinkrs)


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


# Dont forget to remove debug


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
