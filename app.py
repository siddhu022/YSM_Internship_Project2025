from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def home():
    return redirect(url_for('registration'))

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        username = request.form.get('uname')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('conf_password')
        gender = request.form.get('gender')
        country = request.form.get('country')

        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('registration'))

        # Normally, you would save user data to a database here.
        flash('Registration successful!', 'success')
        return redirect(url_for('registration'))

    return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True)
