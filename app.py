from flask import Flask, request, render_template, redirect, url_for, send_from_directory, flash
import os
from dotenv import load_dotenv
from flask import session
from datetime import timedelta

# Load password from secrets.env
load_dotenv("secrets.env")
ACCESS_PASSWORD = os.getenv("ACCESS_PASSWORD")

app = Flask(__name__)

# 🔐 Secret key and session settings
app.secret_key = os.getenv("FLASK_SECRET_KEY")
app.permanent_session_lifetime = timedelta(minutes=5)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# In-memory access control (no session for now)
authorized_clients = set()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        password = request.form.get("password")
        if password == ACCESS_PASSWORD:
            session.permanent = True
            session["authenticated"] = True
            return redirect(url_for("upload"))
        else:
            flash("❌ Invalid password")
            return redirect(url_for("index"))

    return render_template("index.html")


import math
from urllib.parse import quote

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if not session.get("authenticated"):
        return redirect(url_for("index"))

    if request.method == "POST":
        file = request.files.get("file")
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            flash(f"✅ File '{file.filename}' uploaded successfully.")
            return redirect(url_for("upload", uploaded=quote(file.filename)))

    # Prepare file list with size
    file_entries = []
    for fname in os.listdir(UPLOAD_FOLDER):
        path = os.path.join(UPLOAD_FOLDER, fname)
        size_bytes = os.path.getsize(path)
        size_kb = math.ceil(size_bytes / 1024)
        file_entries.append({"name": fname, "size_kb": size_kb})

    uploaded_filename = request.args.get("uploaded")
    return render_template("upload.html", files=file_entries, uploaded_filename=uploaded_filename)


@app.route("/download/<filename>")
def download(filename):
    if not session.get("authenticated"):
        return redirect(url_for("index"))
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)


@app.route("/delete/<filename>", methods=["POST"])
def delete_file(filename):
    if not session.get("authenticated"):
        return redirect(url_for("index"))

    try:
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            flash(f"🗑️ File '{filename}' deleted.")
        else:
            flash(f"❌ File not found.")
    except Exception as e:
        flash(f"❌ Error deleting file: {e}")
    return redirect(url_for("upload"))


from flask import jsonify

@app.route("/files")
def list_files():
    if not session.get("authenticated"):
        return jsonify([])

    file_entries = []
    for fname in os.listdir(UPLOAD_FOLDER):
        path = os.path.join(UPLOAD_FOLDER, fname)
        size_bytes = os.path.getsize(path)
        size_kb = math.ceil(size_bytes / 1024)
        file_entries.append({"name": fname, "size_kb": size_kb})

    return jsonify(file_entries)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
