from flask import Flask, render_template, request

app = Flask(__name__, template_folder='C:/Users/hp/Desktop/project_vsd/templates/')

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/login1', methods=['POST', 'GET'])
def login1():
    if request.method == 'POST':
        NAME = request.form['NAME']
        EMAIL = request.form['EMAIL']
        if NAME == "srikanth" and EMAIL == "srikanth@gmail.com":
            return "Welcome to the portal"
        else:
            error = "Invalid credentials. Please try again."
            return render_template("login.html", error=error)
    return render_template("login.html")

@app.route('/register1', methods=['POST', 'GET'])
def register1():
    if request.method == 'POST':
        NAME = request.form['NAME']
        EMAIL = request.form['EMAIL']
        PASSWORD = request.form['PASSWORD']
        # Process registration data, possibly storing it in a database.
        return render_template("login.html")  # You might want to redirect to the login page after registration.
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
