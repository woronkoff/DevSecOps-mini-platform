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

@main.get("/app/info")
def app_info():
    return jsonify({
        "app_name": "DevSecOps Mini Platform",
        "version": "0.1.0",
        "environment": "development"
    })