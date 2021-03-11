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
    # find and sort shrink top 5
    shrink = list(mongo.db.shrinkDB.find().limit(20).sort(
        "amount_lost_value", -1,))
    # Find shrink that has been resolved
    shrinkrs = list(mongo.db.shrinkDB.find().limit(20).sort(
        "amount_lost_value", -1,))
    return render_template(
        "shrink.html", shrinkDB=shrink, shrinkrs=shrinkrs)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # See if manager is registered
        present_user = mongo.db.userDb.find_one(
            {"username": request.form.get("username").lower()})

        if present_user:
            flash("Already a User")
            return redirect(url_for("register"))

        # Register user to userDb
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "department": request.form.get("department")
        }
        mongo.db.userDb.insert_one(register)

        # Make user in session
        session["user"] = request.form.get("username").lower()
        flash("Welcome!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        present_user = mongo.db.userDb.find_one(
            {"username": request.form.get("username").lower()})
        # Password check
        if present_user:
            if check_password_hash(
                    present_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Thank you {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session[
                    "user"]))
            else:
                flash("Username Or Password Is Incorrect")
                return redirect(url_for("login"))

        else:
            flash("Username Or Password Is Incorrect")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Unpack MongoDb for profile find the user
    user = mongo.db.userDb.find_one({"username": username})
    # find the user department
    user_department = user["department"]
    # filter the results to be users department only
    filtered_results = list(mongo.db.shrinkDB.find(
        {"department": user_department}).limit(20).sort(
        "amount_lost_value", -1,))
    if session["user"]:
        return render_template(
            "profile.html", username=username,
            filtered_results=filtered_results)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Log user out on request
    flash("Logout Successful")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/addshrink", methods=["GET", "POST"])
def addshrink():
    # Submit form
    if request.method == "POST":
        resolved = True if request.form.get("resolved") else False
        shrink = {
            "department": request.form.get("department"),
            "product_name": request.form.get("product_name"),
            "product_location": request.form.get("product_location"),
            "amount_lost_value": int(request.form.get(
                "amount_lost_value")),
            "amount_lost_singles": int(request.form.get(
                "amount_lost_singles")),
            "additional_info": request.form.get("additional_info"),
            "date": request.form.get("date"),
            "resolved": resolved,
            "employee": session["user"]
        }
        mongo.db.shrinkDB.insert_one(shrink)
        flash("Shrink Added")
        return redirect(url_for("get_shrink"))
    # Get department categories
    department = mongo.db.shrinkDb.find().sort("department", 1)
    return render_template("add-shrink.html", department=department)


@app.route("/edit_shrink/<shrink_id>", methods=["GET", "POST"])
def edit_shrink(shrink_id):
    # Submit form, Get the information to edit
    if request.method == "POST":
        resolved = True if request.form.get("resolved") else False
        edit = {
            "department": request.form.get("department"),
            "product_name": request.form.get("product_name"),
            "product_location": request.form.get("product_location"),
            "amount_lost_value": int(request.form.get(
                "amount_lost_value")),
            "amount_lost_singles": int(request.form.get(
                "amount_lost_singles")),
            "additional_info": request.form.get("additional_info"),
            "date": request.form.get("date"),
            "resolved": resolved,
            "employee": session["user"]
        }
        mongo.db.shrinkDB.update({"_id": ObjectId(shrink_id)}, (edit))
        flash("Shrink Updated")

    shrink = mongo.db.shrinkDB.find_one({"_id": ObjectId(shrink_id)})
    department = mongo.db.shrinkDb.find().sort("department", 1)
    return render_template(
        "edit-shrink.html", shrink=shrink, department=department)


@app.route("/delete_shrink/<shrink_id>")
def delete_shrink(shrink_id):
    # Delete Shrink when clicked
    mongo.db.shrinkDB.remove({"_id": ObjectId(shrink_id)})
    flash("Shrink Deleted")
    return redirect(url_for("get_shrink"))


@app.route("/search_shrink", methods=["GET", "POST"])
def search_shrink():
    # Get the shrink to search
    shrink = mongo.db.shrinkDB.find()
    # Post the search method using the index
    if request.method == "POST":
        search = request.form.get("search")
        shrinksearch = list(mongo.db.shrinkDB.find(
            {"$text": {"$search": search}}))
        return render_template(
            "search-shrink.html", shrinksearch=shrinksearch, shrink=shrink)
    return render_template("search-shrink.html")


@app.route("/contact")
def contact():
    # Render contact page
    return render_template("contact.html")


# Dont forget to remove debug
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
