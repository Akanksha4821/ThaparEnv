print("routes.py is being imported")
import sys
import os

from flask import Blueprint, request, jsonify
import sys
try:
    from ThaparEnv.ThaparGpt import ThaparAssistant
    print("ThaparGpt imported successfully.")
except ImportError as e:
    print(f"Error importing ThaparGpt: {e}")


api_bp = Blueprint("api", __name__)
print("Creating ThaparAssistant instance...")

assistant = ThaparAssistant()

@api_bp.route("/query", methods=["POST"])
def handle_query():
    try:
        data = request.get_json()
        query = data.get("query", "")
        response = assistant.ask(query)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
