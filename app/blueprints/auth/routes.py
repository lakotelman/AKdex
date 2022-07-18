from app.blueprints.auth.forms import RegistrationForm
from . import bp as app
from app import login_manager
from flask import render_template, redirect, url_for, request, flash
from app.database import db
from flask_login import login_user, logout_user, current_user
from app.models.user import User


@app.route("login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.my_dex"))
    if request.method == "POST":
        user = User.query.filter_by(email=request.form["inputEmail"]).first()

        if user is None:
            flash(
                f"The user with email {request.form['inputEmail']} doesn't exist",
                "danger",
            )
        elif not user.check_my_pass(request.form["inputPassword"]):
            flash("Password is incorrect", "danger")
        else:
            login_user(user)
            flash(f"Welcome back, {user.first_name}.", "success")
            return redirect(url_for("main.my_dex"))
        return render_template("login.html")
    else:
        return render_template("login.html")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("register", methods=["GET", "POST"])
def register():
    rform = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    try:
        if request.method == "POST" and rform.validate():
            email = rform.email.data
            check_user = User.query.filter_by(email=email).first()

            if check_user is not None:
                flash("User with this email already exists.", "danger")

            else:
                email = rform.email.data
                first_name = rform.first_name.data
                last_name = rform.last_name.data
                username = rform.username.data
                password = rform.password.data
                confirm_password = rform.confirm_password.data

                if password == confirm_password:
                    new_user = User(
                        email=email,
                        password="",
                        username=username,
                        first_name=first_name,
                        last_name=last_name,
                    )
                    new_user.hash_my_pass(password)
                    db.session.add(new_user)
                    db.session.commit()
                    flash("Welcome, new user. Please log in.", "success")
                    return redirect(url_for("auth.login"))
                else:
                    flash("Your passwords don't match.", "danger")
                # sends them back to registration page if they don't successfully register a user.
                return render_template("register.html")
        else:
            return render_template("register.html", form=rform)
    except Exception as err:
        print(err)
        flash("Please enter all data correctly. Try again", "danger")

    return render_template("register.html", form=rform)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
