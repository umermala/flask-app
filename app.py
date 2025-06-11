import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    db_password = os.getenv("DB_PASSWORD", "Not Set")
    api_key = os.getenv("API_KEY", "Not Set")
    return (
        f"Success! Your app is running inside Docker.<br>"
        f"DB_PASSWORD: {db_password}<br>"
        f"API_KEY: {api_key}"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)