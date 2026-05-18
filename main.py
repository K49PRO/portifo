# Import

import sqlite3
from flask import Flask, render_template, request, redirect, flash




app = Flask(__name__)
app.secret_key = 'supersecretkey'  # flash mesajları için

# SQLite veritabanı ve tablo oluşturma
def init_db():
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        text TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

init_db()


# İçerik sayfasını çalıştırma ve geri bildirim işlemleri
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        text = request.form.get('text')
        if email and text:
            conn = sqlite3.connect('feedback.db')
            c = conn.cursor()
            c.execute('INSERT INTO feedback (email, text) VALUES (?, ?)', (email, text))
            conn.commit()
            conn.close()
            flash('Geri bildiriminiz için teşekkürler!')
            return redirect('/')
    return render_template('index.html')



# Dinamik beceriler (örnek)
@app.route('/skills', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)


if __name__ == "__main__":
    app.run(debug=True)
