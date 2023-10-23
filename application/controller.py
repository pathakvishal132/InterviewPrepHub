from flask import Flask, redirect, request
from flask import render_template, request, session, redirect, jsonify, url_for, flash
from flask import current_app as app
from application.database import db
from application.model import *
from flask_login import LoginManager, login_user, UserMixin, login_required, logout_user
from passlib.hash import sha256_crypt
from passlib.hash import sha256_crypt
from flask_login import login_user, logout_user, login_required, current_user

login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@login_manager.user_loader
def load_manager(id):
    return Manager.query.get(int(id))


@app.route("/")
def home():
    return render_template("index.html", answered=False)


@app.route("/register_user", methods=["GET", "POST"])
def register_user():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if user:
            flash("Username already exists", "error")
        else:
            new_user = User(
                username=username, email=email, password=sha256_crypt.hash(password)
            )
            db.session.add(new_user)
            db.session.commit()
            flash("User registered successfully", "success")
            return redirect(url_for("home"))
    return render_template("register.html")


@app.route("/register_manager", methods=["GET", "POST"])
def register_manager():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        manager = Manager.query.filter_by(name=username).first()
        if manager:
            flash("Username already exists", "error")
        else:
            new_manager = Manager(
                name=username, email=email, password=sha256_crypt.hash(password)
            )
            db.session.add(new_manager)
            db.session.commit()
            flash("Manager registered successfully", "success")
            return redirect(url_for("home"))
    return render_template("managerregister.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        f_email = request.form.get("email")
        f_password = request.form.get("password")
        check_user = User.query.filter_by(email=f_email).first()
        check_manager = Manager.query.filter_by(email=f_email).first()
        if check_user and check_user.check_password_correction(
            attempted_password=f_password
        ):
            login_user(check_user)
            flash(
                f"Success! You are logged in as: {check_user.username}",
                category="success",
            )
            return redirect(url_for("user_dashboard"))
        if check_manager and check_manager.check_password_correction(f_password):
            login_user(check_manager)
            flash(
                f"Success! You are logged in as: {check_manager.name}",
                category="success",
            )
            return redirect(url_for("manager_dashboard"))
        else:
            flash(
                "Username and password do not match! Please try again",
                category="danger",
            )

    return render_template("login.html")


@app.route("/user_dashboard", methods=["GET", "POST"])
@login_required
def user_dashboard():
    return render_template("userdashboard.html")


@app.route("/manager_dashboard", methods=["GET", "POST"])
@login_required
def manager_dashboard():
    return render_template("managerdashboard.html")


@app.route("/webdev", methods=["POST", "GET"])
def webdev():
    if request.method == "POST":
        title = request.form.get("title")
        questions = request.form.get("questions")
        answer = request.form.get("answer")
        t_check = Webdev.query.filter_by(name=title).first()
        if t_check:
            flash("Question already exists")
        else:
            add_q = Webdev(name=title, questions=questions, ans=answer)
            db.session.add(add_q)
            db.session.commit()
            return redirect(url_for("manager_dashboard"))

    return redirect(url_for("manager_dashboard"))


@app.route("/mlai", methods=["POST", "GET"])
def mlai():
    if request.method == "POST":
        title = request.form.get("title")
        questions = request.form.get("questions")
        answer = request.form.get("answer")
        t_check = MlAi.query.filter_by(name=title).first()
        if t_check:
            flash("Question already exists")
        else:
            add_q = MlAi(name=title, questions=questions, ans=answer)
            db.session.add(add_q)
            db.session.commit()
            return redirect(url_for("manager_dashboard"))

    return redirect(url_for("manager_dashboard"))


@app.route("/android", methods=["POST", "GET"])
def android():
    if request.method == "POST":
        title = request.form.get("title")
        questions = request.form.get("questions")
        answer = request.form.get("answer")
        t_check = Android.query.filter_by(name=title).first()
        if t_check:
            flash("Question already exists")
        else:
            add_q = Android(name=title, questions=questions, ans=answer)
            db.session.add(add_q)
            db.session.commit()
            return redirect(url_for("manager_dashboard"))

    return redirect(url_for("manager_dashboard"))


@app.route("/blockchain", methods=["POST", "GET"])
def blockchanin():
    if request.method == "POST":
        title = request.form.get("title")
        questions = request.form.get("questions")
        answer = request.form.get("answer")
        t_check = Blockchain.query.filter_by(name=title).first()
        if t_check:
            flash("Question already exists")
        else:
            add_q = Blockchain(name=title, questions=questions, ans=answer)
            db.session.add(add_q)
            db.session.commit()
            return redirect(url_for("manager_dashboard"))

    return redirect(url_for("manager_dashboard"))


@app.route("/mechanical", methods=["POST", "GET"])
def mechanical():
    if request.method == "POST":
        title = request.form.get("title")
        questions = request.form.get("questions")
        answer = request.form.get("answer")
        t_check = Mechanical.query.filter_by(name=title).first()
        if t_check:
            flash("Question already exists")
        else:
            add_q = Mechanical(name=title, questions=questions, ans=answer)
            db.session.add(add_q)
            db.session.commit()
            return redirect(url_for("manager_dashboard"))

    return redirect(url_for("manager_dashboard"))


@app.route("/dsa", methods=["POST", "GET"])
def dsa():
    if request.method == "POST":
        title = request.form.get("title")
        questions = request.form.get("questions")
        answer = request.form.get("answer")
        t_check = Dsa.query.filter_by(name=title).first()
        if t_check:
            flash("Question already exists")
        else:
            add_q = Dsa(name=title, questions=questions, ans=answer)
            db.session.add(add_q)
            db.session.commit()
            return redirect(url_for("manager_dashboard"))

    return redirect(url_for("manager_dashboard"))


@app.route("/electrical", methods=["POST", "GET"])
def electrical():
    if request.method == "POST":
        title = request.form.get("title")
        questions = request.form.get("questions")
        answer = request.form.get("answer")
        t_check = Electrical.query.filter_by(name=title).first()
        if t_check:
            flash("Question already exists")
        else:
            add_q = Electrical(name=title, questions=questions, ans=answer)
            db.session.add(add_q)
            db.session.commit()
            return redirect(url_for("manager_dashboard"))

    return redirect(url_for("manager_dashboard"))


@app.route("/civil", methods=["POST", "GET"])
def civil():
    if request.method == "POST":
        title = request.form.get("title")
        questions = request.form.get("questions")
        answer = request.form.get("answer")
        t_check = Civil.query.filter_by(name=title).first()
        if t_check:
            flash("Question already exists")
        else:
            add_q = Civil(name=title, questions=questions, ans=answer)
            db.session.add(add_q)
            db.session.commit()
            return redirect(url_for("manager_dashboard"))

    return redirect(url_for("manager_dashboard"))


@app.route("/subcategory", methods=["GET", "POST"])
def subcategory():
    if request.method == "POST":
        domain = request.form.get("domain")
        subcategory = request.form.get("subcategory")
        if domain == "cs":
            if subcategory == "web-development":
                all_webdev_data = Webdev.query.all()
                webdev_data = [
                    {"name": entry.name, "questions": entry.questions, "ans": entry.ans}
                    for entry in all_webdev_data
                ]
                session["webdev_data"] = webdev_data
                session["current_question_index"] = 0
                current_question_index = session["current_question_index"]
                webdev_data = session["webdev_data"]
                if current_question_index < len(webdev_data):
                    current_question = webdev_data[current_question_index]
                    question = current_question["questions"]
                    title = current_question["name"]
                else:
                    question = title = "No more questions."

                return render_template(
                    "userdashboard.html", question=question, title=title, answered=True
                )
            if subcategory == "android-development":
                pass
            if subcategory == "machine-learning-and-artificial-intelligence":
                pass
            if subcategory == "blockchain-development":
                pass
            if subcategory == "data-structure":
                pass
            pass
        if domain == "ee":
            pass
        if domain == "me":
            pass
        if domain == "ce":
            pass
    return redirect(url_for("home", answered=False))


@app.route("/handleans", methods=["POST"])
def handleans():
    if request.method == "POST":
        user_answer = request.form.get("user_answer")
        current_question_index = session["current_question_index"]
        webdev_data = session["webdev_data"]

        current_question = webdev_data[current_question_index]
        expected_answer = current_question["ans"]
        feedback = (
            "Correct!"
            if user_answer.strip() == expected_answer.strip()
            else "Incorrect."
        )
        question = current_question["questions"]
        title = current_question["name"]
        # Increment the current question index

        session["current_question_index"] = current_question_index

        return render_template(
            "userdashboard.html", feedback=feedback, question=question, title=title
        )
    return redirect(url_for("home", answered=True))


@app.route("/next", methods=["POST"])
def next_question():
    if request.method == "POST":
        current_question_index = session.get("current_question_index", 0)
        webdev_data = session.get("webdev_data", [])

        if current_question_index < len(webdev_data) - 1:
            current_question_index += 1
            current_question = webdev_data[current_question_index]
            question = current_question.get("questions", "")
            title = current_question.get("name", "")
        else:
            # Handle the case where there are no more questions
            question = "No more questions available."
            title = "End of questions"

        session["current_question_index"] = current_question_index
        return render_template("userdashboard.html", question=question, title=title)


@app.route("/previous", methods=["POST"])
def previous_question():
    if request.method == "POST":
        current_question_index = session.get("current_question_index", 0)
        webdev_data = session.get("webdev_data", [])

        if current_question_index > 0:
            current_question_index -= 1

        current_question = webdev_data[current_question_index]
        question = current_question.get("questions", "")
        title = current_question.get("name", "")

        session["current_question_index"] = current_question_index
        return render_template("userdashboard.html", question=question, title=title)


@app.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out!", category="info")
    return redirect(url_for("home"))
