from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

# Halaman utama dengan form login
@app.route('/')
def home():
    return render_template('index.html')  # Render index.html yang ada di folder templates

# Halaman sukses yang menampilkan pesan selamat datang
@app.route('/success/<name>')
def success(name):
    return f'Welcome {name}!'

# Halaman login yang menerima metode GET dan POST
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # Mengambil data yang diinputkan oleh pengguna dari form
        user = request.form['nm']
        # Mengarahkan ke halaman sukses dengan username yang dimasukkan
        return redirect(url_for('success', name=user))
    else:
        # Jika request menggunakan GET, arahkan kembali ke halaman login (home)
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
