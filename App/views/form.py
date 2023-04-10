from flask import Flask, request, jsonify
from App.database import db
from App.models import document
from maker.py import *


app = Flask(__name__)

@app.route('/App/views/form', methods=['POST'])
def handle_form_data():
    data = request.get_json()
    function_name = data.get('function_name')
  
    if function_name == "submitForm":
        formdata = writeDoc(data)
        doc = document(binary_data=formdata)
        db.session.add(doc)
        db.session.commit()

        return jsonify({'message': 'Data received successfully!'})
    else:
        return jsonify({'error': 'Invalid function name'})