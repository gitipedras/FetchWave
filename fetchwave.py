from flask import Flask, request, render_template, redirect, url_for, session
from flask_mail import Mail, Message


app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-password'
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Secret key for session management
mail = Mail(app)

# Predefined username and password
valid_username = 'ian'
valid_password = 'ian'

app.static_folder = 'templates'

@app.route('/')
def index():
    return render_template('login.html')
    #return '<link rel="stylesheet" type="text/css" href="../style.css" />'

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the provided username and password are valid
        if username == valid_username and password == valid_password:
            # Set 'logged_in' session variable to True
            session['logged_in'] = True
            # Redirect to the 'success' endpoint
            return redirect(url_for('success'))
        else:
            return 'Invalid username or password. Please try again.'

@app.route('/success')
def success():
    # Check if 'logged_in' session variable is True
    if session.get('logged_in'):
        #return 'Login successful!'
        return '<h1 style="font-family:monospace"> Login Succesfull </h1> <br> <a style="font-family:monospace;font-size:15px;" href="/dashboard">Go to Dashboard</a>'
    else:
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    # Check if 'logged_in' session variable is True
    if session.get('logged_in'):
        return render_template('dashboard.html')
        #return '<link rel="stylesheet" type="text/css" href="../style.css" />'
    else:
        return redirect(url_for('index'))
        


        

def page_not_found(error):
    return render_template('404.html'), 404



########

@app.route('/upload', methods=['POST'])
def upload_file():
    email = request.form['email']
    repository = request.form['repository']
    expiration = request.form['expiration']
    downloads = request.form['downloads']
    file = request.files['file']
    
    # Save the file to the server (customize this part)
    file.save('uploads/' + file.filename)
    
    # Send email
    msg = Message('File Shared', sender='your-email@example.com', recipients=[email])
    msg.body = f'File has been shared with you.\nTopic: {repository}\nExpiration: {expiration}\nDownloads: {downloads}'
    mail.send(msg)
    
    return 'File uploaded and email sent successfully.'


if __name__ == '__main__':
    app.run(debug=True)
