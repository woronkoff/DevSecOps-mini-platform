from flask import Blueprint, jsonify

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
def api_info():
    return jsonify({
        "name": "DevSecOps Mini Platform",
        "version": "0.1.0",
        "description": "development"
        })