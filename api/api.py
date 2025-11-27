from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from dotenv import load_dotenv
import os
import sys

load_dotenv()

app = Flask(__name__)
CORS(app)

#Set up the database
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DATABASE_URI = (f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Create the class needed to submit information to the users table
class Submission(db.Model):
    __tablename__ = 'users'
    userID   = db.Column(db.Integer, primary_key =True )
    name     = db.Column(db.String(255), nullable=False)
    email    = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password
        }

    def __repr__(self):
        return f'<UserSubmission {self.name}>'

#Route made for the insecure submission, this does NOT protect against SQLInjection
@app.route('/submitInsec', methods=['POST'])
def submitInsec():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    query = (f"INSERT INTO users (name, email, password) "
             f"VALUES ('{name}', '{email}', '{password}')"
            )

    try:
        #Exeute the query, return the most recent addition
        db.session.execute(text(query))
        db.session.commit()
        recentUser = db.session.execute(db.select(Submission).order_by(Submission.userID.desc()).limit(1)).scalar_one_or_none()
        print(f"Executed Query: {query}", file = sys.stdout)

        return jsonify({"message":f"Registered new user! Welcome to the database, {recentUser.name}"})
    except Exception as e:
        print(f"Query not executed??? Here's why: {e}", file = sys.stdout)
        db.session.rollback()
        return jsonify({"message":"No query executed... sorry!"})


#Route for the secure submission, this protects against SQLInjection
@app.route('/submitSec', methods=['POST'])
def submitSec():
    try:
        if request.is_json:
            data = request.get_json()
            name = data.get('name')
            email = data.get('email')
            password = data.get('password')

            new_submission = Submission(name=name, email=email, password = password)
            db.session.add(new_submission)
            db.session.commit()
            recentUser = db.session.execute(db.select(Submission).order_by(Submission.userID.desc()).limit(1)).scalar_one_or_none()

            return jsonify({"message":f"Registered new user! Welcome to the database, {recentUser.name}"})
        else:
            return jsonify({"message": "Data error, wtf?!"}), 400
    except Exception as e:
        print(f"Database Error: {e}")
        return jsonify({
            "message": "Database Error"
        }), 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database Tables Checked")
    app.run(debug=True, port=5000)
