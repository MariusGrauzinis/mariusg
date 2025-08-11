from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from hangman import load_words, choose_word, display_word

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

# -------------------- MODELS --------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    score = db.Column(db.Integer, default=0)

# -------------------- Hangman paveiksliukai --------------------
HANGMANPICS = [
    r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
 [O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
 [O]  |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
 [O]  |
[/|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
 [O]  |
[/|\] |
 / \  |
      |
========='''
]

# -------------------- ROUTES --------------------
@app.route('/')
def index():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        if User.query.filter_by(username=uname).first():
            return "Vartotojas jau egzistuoja"
        user = User(username=uname, password_hash=generate_password_hash(pwd))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        user = User.query.filter_by(username=uname).first()
        if user and check_password_hash(user.password_hash, pwd):
            session['user_id'] = user.id
            return redirect(url_for('game'))
        return render_template('login.html', message="Neteisingi duomenys")
    return render_template('login.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if 'word' not in session:
        words = load_words("words.txt")
        session['word'] = choose_word(words)
        session['guessed'] = []
        session['tries'] = 10  # Pradinis bandymų skaičius

    word = session['word']
    guessed = set(session['guessed'])
    display = display_word(word, guessed)
    message = ""

    if request.method == 'POST':
        guess = request.form['guess'].lower().strip()
        if len(guess) == 1:
            if guess in guessed:
                message = "Raidė jau buvo spėta."
            elif guess in word:
                guessed.add(guess)
                message = "Teisinga raidė!"
            else:
                session['tries'] -= 1
                guessed.add(guess)
                message = "Neteisinga raidė!"
        elif guess == word:
            update_score()
            return render_template('result.html', success=True, word=word)
        else:
            session['tries'] -= 1
            message = "Neteisingas žodis!"

        session['guessed'] = list(guessed)

        if all(letter in guessed for letter in word):
            update_score()
            return render_template('result.html', success=True, word=word)

        if session['tries'] <= 0:
            return render_template('result.html', success=False, word=word)

    # Apskaičiuojam klaidų skaičių ir saugiai pasirenkam paveiksliuką
    mistakes = 10 - session['tries']
    hangman_index = min(mistakes, len(HANGMANPICS) - 1)
    hangman_pic = HANGMANPICS[hangman_index]

    return render_template('game.html',
                           display_word=display,
                           tries=session['tries'],
                           message=message,
                           hangman_pic=hangman_pic)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

def update_score():
    user = User.query.get(session['user_id'])
    user.score += 1
    db.session.commit()
    session.pop('word', None)
    session.pop('guessed', None)
    session.pop('tries', None)

# -------------------- INIT --------------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
