from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Add logic to verify the user credentials
        if username == "admin" and password == "password":  # Example check
            return "Login Successful!"
        else:
            return "Invalid credentials, try again."
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
