from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///our_own.db'
db = SQLAlchemy(app)

class FormData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text)

@app.route('/App/views/form.py', methods=['POST'])
def handle_form_data():
    data = request.get_json()
    function_name = data.get('function_name')
  
    if function_name == "submitForm":
        form_data = FormData(data=json.dumps(data))
        db.session.add(form_data)
        db.session.commit()

        return jsonify({'message': 'Data received successfully!'})
    else:
        return jsonify({'error': 'Invalid function name'})
