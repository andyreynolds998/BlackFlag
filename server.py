from flask import Flask, abort, request, render_template
from classData import classData
from faqData import faq
import json
from flask_cors import CORS
from config import db, parse_json

app = Flask(__name__)
CORS(app)

if __name__ == '__main__':
    app.run()

@app.route("/api/classes")
def get_curriculum():
    cursor = db.classes.find({})
    curriculum = [item for item in cursor]
    return parse_json(curriculum)

@app.route("/api/faq")
def get_faq():
    cursor = db.faq.find({})
    faq = [item for item in cursor]
    return parse_json(faq)