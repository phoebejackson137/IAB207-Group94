from flask import Flask, render_template

app = Flask(__name)

# Custom error page for 404 - Page Not Found
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Custom error page for 50X - Internal Server Error
@app.errorhandler(50X)
def server_error(error):
    return render_template('50X.html'), 50X

if __name__ == '__main__':
    app.run(debug=True)
