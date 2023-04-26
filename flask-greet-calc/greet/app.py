from flask import Flask

app = Flask(__name__ )


# ***/welcome***   Returns “welcome”

# ***/welcome/home***   Returns “welcome home”

# ***/welcome/back***   Return “welcome back”

@app.route('/welcome')
def say_welcome():
    """Return simple "Welcome" Greeting."""

    html = "<html><body><h1>Welcome</h1></body></html>"
    return html

@app.route('/welcome/home')
def say_welcome_home():
    """Return simple "Welcome Home" Greeting."""

    html = "<html><body><h1>Welcome Home</h1></body></html>"
    return html

@app.route('/welcome/back')
def back():
    """Return simple "Welcome Back" Greeting."""

    html = "<html><body><h1>Welcome Back</h1></body></html>"
    return html

