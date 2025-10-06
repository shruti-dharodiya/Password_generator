from flask import Flask, render_template, request, flash
import random
import string

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a random string for security


@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    error = None

    if request.method == 'POST':
        try:
            # Get form inputs
            length = int(request.form['length'])
            if length < 8:
                raise ValueError("Password length should be at least 8 characters.")

            # Character sets based on user choices
            chars = ''
            if request.form.get('lowercase'):
                chars += string.ascii_lowercase
            if request.form.get('uppercase'):
                chars += string.ascii_uppercase
            if request.form.get('numbers'):
                chars += string.digits
            if request.form.get('symbols'):
                chars += string.punctuation

            if not chars:
                raise ValueError("Select at least one character type.")

            # Generate password
            password = ''.join(random.choice(chars) for _ in range(length))

        except ValueError as e:
            error = str(e)
            flash(error)  # This will display the error on the page

    return render_template('index.html', password=password, error=error)


if __name__ == '__main__':
    app.run(debug=True)
