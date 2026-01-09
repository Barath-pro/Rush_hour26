from flask import Flask, render_template, request, redirect, session, jsonify
import json
from datetime import datetime, timedelta
import os
from flask import send_from_directory


app = Flask(__name__)
app.secret_key = "kutta_hunt_secret"

# ---- JSON DB HANDLERS ----
def load_db():
    if not os.path.exists("db.json"):
        default_db = {
            "teams": [],
            "scores": {},
            "hunt_start_time": "",
            "official_qr_code": "SIET-RUSH-HUNT-2026"
        }
        save_db(default_db)
        return default_db

    with open("db.json", "r", encoding="utf-8") as f:
        return json.load(f)

def save_db(db):
    with open("db.json", "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2)
 
# ---- HOME ----
@app.route("/")
def home():
    return redirect("/index")

@app.route("/index")
def index_page():
    if "team" not in session:
        return redirect("/login")
    return render_template("index.html", team=session["team"])

# ---- LEVEL ROUTES ----
@app.route("/level1")
def level1():
    if "team" not in session: return redirect("/login")
    return render_template("level1.html", team=session["team"])

@app.route("/level2")
def level2():
    if "team" not in session: return redirect("/login")
    return render_template("level2.html", team=session["team"])

@app.route("/level3")
def level3():
    if "team" not in session: return redirect("/login")
    return render_template("level3.html", team=session["team"])

@app.route("/level4")
def level4():
    if "team" not in session: return redirect("/login")
    return render_template("level4.html", team=session["team"])

@app.route("/level5")
def level5():
    if "team" not in session: return redirect("/login")
    return render_template("level5.html", team=session["team"])

@app.route("/level6")
def level6():
    if "team" not in session: return redirect("/login")
    return render_template("level6.html", team=session["team"])

@app.route("/final")
def final_page():
    if "team" not in session: return redirect("/login")
    return render_template("final.html", team=session["team"])


# ---- VERIFY QR (NOT CHANGED OR TOUCHED) ----
@app.route("/verify_qr", methods=["POST"])
def verify_qr():
    db = load_db()
    qr_text = request.json.get("qr", "")

    if qr_text == db["official_qr_code"]:
        session["verified"] = True
        return jsonify({"valid": True, "clue": "QR verified! \n Level 2 clue unlocked! \n When the bell rings,noses lead the way,Follow the small where snacks hold sway"})
    return jsonify({"valid": False})


   
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
