from flask import Flask, render_template

app = Flask(__name)

# Custom error page for 404 - Page Not Found
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Custom error page for 500 - Internal Server Error
@app.errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500

# Custom error page for 501 - Not Implemented
@app.errorhandler(501)
def server_error(error):
    return render_template('501.html'), 501

# Custom error page for 502 - Bad Gateway
@app.errorhandler(502)
def server_error(error):
    return render_template('502.html'), 502

# Custom error page for 503 - Service Unavailable
@app.errorhandler(503)
def server_error(error):
    return render_template('503.html'), 503

# Custom error page for 504 - Gateway Timeout
@app.errorhandler(504)
def server_error(error):
    return render_template('504.html'), 504

# Custom error page for 505 - HTTP Version Not Supported
@app.errorhandler(505)
def server_error(error):
    return render_template('505.html'), 505

# Custom error page for 506 - Variant Also Negotiates
@app.errorhandler(506)
def server_error(error):
    return render_template('506.html'), 506

# Custom error page for 507 - Insufficient Storage
@app.errorhandler(507)
def server_error(error):
    return render_template('507.html'), 507

# Custom error page for 508 - Loop Detected
@app.errorhandler(508)
def server_error(error):
    return render_template('508.html'), 508

if __name__ == '__main__':
    app.run(debug=True)

