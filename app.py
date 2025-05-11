from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('uname')
        password = request.form.get('password')

        if username == 'sid02' and password == 'Siddhesh@02':
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        elif username == 'sid02' and password != 'Siddhesh@02':
            flash('Incorrect password. Please try again.', 'danger')
        else:
            flash('Invalid credentials. Please try again.', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('uname')
        password = request.form.get('password')

        if username == 'admin' and password == 'admin123':
            flash('Admin login successful!', 'success')
            return redirect(url_for('index'))
        elif username == 'admin' and password != 'admin123':
            flash('Incorrect password. Please try again.', 'danger')
        else:
            flash('Invalid credentials. Please try again.', 'danger')
            return redirect(url_for('admin_login'))

    return render_template('admin_login.html')

@app.route('/logout')
def logout():
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

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

        flash('Registration successful!', 'success')
        return redirect(url_for('registration'))

    return render_template('registration.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        flash('Message sent successfully!', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')

@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
