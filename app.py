from flask import Flask, render_template

# Create Flask app instance
app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    return render_template('menu.html')

# Route for menu (same as home for now)
@app.route('/menu')
def menu():
    return render_template('menu.html')

# Run the app
if __name__ == '__main__':
    # Development mode - change debug to False for production
    app.run(debug=True, host='0.0.0.0', port=5000)