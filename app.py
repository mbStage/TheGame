from flask import Flask, render_template, request, redirect, session, url_for
import os
from src.log import log
from src.points import points

log_instance = log()
points_instance = points()

app = Flask(__name__)
app.secret_key = "super_secret_key"  # change in production

# CTF Levels (question + correct flag)

number_of_levels = os.listdir('levels')

LEVELS = {}
for dirs in os.listdir('levels'):
    with open(f'levels/{dirs}', 'r',encoding='utf-8') as f:
        content = f.read().split('####')
        header = content[0].strip().splitlines()
        question = content[1].strip()[8:]
        answer = content[2].strip().replace('\n', '')[6:]
        hint = content[3].strip()[4:] if len(content) > 3 else "No hints available."
        level_id  = int(dirs[-5:][0])

    LEVELS[level_id] = {
        "question": question,
        "flag": answer,
        "header": header[0] if header else f"Level {level_id}",
        "hint": hint
    }   


##Store username as session variable upon login

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Simple login (for demo purposes)
        if username.lower() in ['pressi','cfo','hop','pp'] and password == "1967":
            session["logged_in"] = True
            session["level"] = 1
            session["username"] = username
            log_instance.log_log(username, f"User logged in!")
            points_instance.add_points(username, 10, 0)
            points_instance.update_maxlevel(username, 0)
            return redirect(url_for("level", level_id=1))

    return render_template("login.html")


@app.route("/level/<int:level_id>", methods=["GET", "POST"])
def level(level_id):
    session_username = session.get("username", "UnknownUser")
    print('user:', session_username)
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    if level_id != session.get("level"):
        return redirect(url_for("level", level_id=session.get("level")))

    level_data = LEVELS.get(level_id)
    if not level_data:
        return redirect(url_for("success"))

    if request.method == "POST":
        answer = request.form["flag"].lower()
        if answer == level_data["flag"].lower():
            session["level"] += 1
            log_instance.log_log(session_username, f"Level {level_id} completed.")
            points_instance.add_points(session_username, 10, level_id)
            points_instance.update_maxlevel(session_username, level_id)
            #log_instance.log_log(session_username, f"Level {level_id} completed.")
            return redirect(url_for("level", level_id=session["level"]))
        else:
            log_instance.log_log(session_username, f"Failed attempt on Level {level_id} with flag: {answer}")
            points_instance.add_points(session_username, -5, level_id)

    return render_template(
        "level.html",
        level=level_id,
        question=level_data["question"],
        header=level_data["header"],
        hint=level_data["hint"],
        logs=log_instance.print_log(session_username),
        number_of_players=points_instance.get_number_of_players(),
        user_points=points_instance.get_points(session_username),
        user_rank=points_instance.get_rank(session_username),
        scoreboard=points_instance.get_scoreboard()
    )


@app.route("/success")
def success():
    if session.get("level") == 6:
        return render_template("success.html")
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
