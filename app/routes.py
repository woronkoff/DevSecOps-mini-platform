from flask import Blueprint, jsonify, current_app

main = Blueprint('main', __name__)

@main.get("/")
def home():
    return jsonify({
        "message": "DevSecOps Mini Platform is running",
        "status": "ok"
    })

@main.get("/health")
def health_check():
    return jsonify({
        "status": "healthy"
    })

@main.get("/api/info")
def app_info():
    return jsonify({
        "name": current_app.config.get("APP_NAME"),
        "version": current_app.config.get("APP_VERSION"),
        "environment": current_app.config.get("APP_ENV")
    })