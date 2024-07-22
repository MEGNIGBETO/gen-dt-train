from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import firebase_admin
from firebase_admin import credentials, auth, firestore
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Change this to a real secret key

# Initialize Firebase
cred = credentials.Certificate('zz/gendt-educ-firebase-adminsdk-gxizv-055faedc54.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def get_user_by_email(email):
    users_ref = db.collection('users')
    docs = users_ref.where('email', '==', email).stream()
    return next(docs, None)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    hashed_password = generate_password_hash(password)
    role = request.form['role']
    try:
        user = auth.create_user(email=email, password=hashed_password, display_name=username)
        db.collection('users').document(user.uid).set({
            'username': username,
            'email': email,
            'role': role,
            'password': hashed_password
        })
        #session['email'] = email
        #session['username'] = username
        #session['role'] = role
        flash('Compte créer, veuillez vous connecter!')
        return redirect(url_for('index'))
    except Exception as e:
        return str(e)

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user_doc = get_user_by_email(email)
    if user_doc != None:
        user_data = user_doc.to_dict()
        try:
            if check_password_hash(user_data['password'], password):
                session['email'] = user_data['email']
                if user_data['role'] == 'apprenant':
                    return redirect(url_for('profile'))
                elif user_data['role'] == 'moniteur':
                    return redirect(url_for('moniteur'))
        except:
            flash('Identifiants incorrects')
            return redirect(url_for('home'))
    else:
        flash('Identifiants incorrects')
        return redirect(url_for('home'))

@app.route('/apprenant')
def apprenant():
    if 'email' in session:
        email = session['email']
        user_doc = get_user_by_email(email)
        user_data = user_doc.to_dict()
        return render_template('apprenant.html', utilisateur=user_data)
    else:
        return redirect(url_for('home'))

@app.route('/profile')
def profile():

    if 'email' in session:
        #email = session['email']
        #user_doc = get_user_by_email(email)
        #user_data = user_doc.to_dict()
        # Exemple de données utilisateur
        user = {
            'profile_picture': 'static/image/avatar1.png',
            'name': 'Jean Dupont',
            'role': 'Apprenant',
            'email': 'jean.dupont@example.com',
            'phone': '0123456789',
            'address': '123 Rue de Paris, 75000 Paris',
            'birth_date': '1990-01-01',
            'language_preference': 'Français',
            'privacy_settings': 'Public',
            'education_level': 'Baccalauréat',
            'courses': 'Mathématiques, Sciences',
            'certifications': 'Certificat de Programmation',
            'last_login': '2024-07-20 10:00',
            'total_time_spent': 120,
            'activity_participation': 'Forums, Quiz',
            'interactions': 'Moniteurs, Étudiants',
            'groups': 'Groupe A, Groupe B',
            'messages': '5 Messages Non-Lus',
            'performance': 'Excellente',
            'badges': 'Badge de Réussite, Badge de Participation',
            'feedback': 'Très Bon Travail!',
            'notifications': 'Email, SMS',
            'theme': 'Thème Clair'
        }
        return render_template('profile.html', user=user)

    

@app.route('/moniteur')
def moniteur():
    if 'email' in session:
        email = session['email']
        user_doc = get_user_by_email(email)
        user_data = user_doc.to_dict()
        return render_template('moniteur.html', utilisateur=user_data)
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
