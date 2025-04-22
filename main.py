print("Starting Flask App...")
from flask import Flask

from ThaparEnv.App.routes import api_bp  


app = Flask(__name__)

app.register_blueprint(api_bp, url_prefix="/api")

@app.route("/", methods=["GET"])
def home():
    return "🎓 Thapar PG Bot is running!"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
