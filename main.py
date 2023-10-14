from flask import Flask, request, session, redirect, url_for
import random

app = Flask(__name__)

def generate_token():
    return str(random.randint(100000, 999999))

@app.route('/')
def index():
    if 'user_token' in session:
        user_cookie = session['user_token']

        # Check if the cookie value matches the placeholder value '010001'.
        if user_cookie == '010001':
            # Generate a 6-digit 2FA code.
            two_factor_code = generate_token()

            # Construct the HTML response directly.
            response_content = f"""
                <html>
                <body>
                <h1>Your 2FA code:</h1>
                <p>{two_factor_code}</p>
                </body>
                </html>
            """
        else:
            # Cookie is present but not matching, take appropriate action (e.g., display an error message).
            response_content = "Error: Invalid cookie"
    else:
        # Cookie not found, take appropriate action (e.g., display an error message or redirect to login).
        response_content = "Error: Cookie not found"

    # Return the HTML content with a 200 OK status code and 'text/html' content type.
    return response_content, 200, {'Content-Type': 'text/html'}

@app.route('/loginpage', methods=['GET'])
def login_page():
    # Generate the login form as an HTML string.
    login_form_html = """
        <html>
        <body>
        <h1>Login</h1>
        <form method="post" action="/login">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required><br>
            <input type="submit" value="Log In">
        </form>
        </body>
        </html>
    """
    return login_form_html

@app.route('/login', methods=['POST'])
def login():
    # Simulate user authentication (replace with actual authentication logic).
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'demo' and password == 'password':
        # Set the session cookie value to '010001'.
        session['user_token'] = '010001'
        return redirect(url_for('index'))
    else:
        # Construct an HTML response for login failure.
        return "Login failed"


@app.route('/logout')
def logout():
    # Clear the user's session, effectively logging them out.
    session.pop('user_token', None)
    return "Logged out"

if __name__ == '__main__':
    app.run(debug=True)
