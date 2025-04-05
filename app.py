from werkzeug.exceptions import HTTPException
from flask import Flask, Response, jsonify
import api.main
import images.badge as badge
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('app.log')
    ]
)

logger = logging.getLogger(__name__)
app = Flask(__name__)

@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"Unhandled exception: {e}", exc_info=True)
    if isinstance(e, HTTPException):
        message = e.description if e.description else "Error"
        return jsonify(error=message), e.code
    return jsonify(error="Internal Server Error"), 500
        
@app.route('/<username>')
def hello(username):
    user_data = api.main.main(username)
    image = badge.create_svg(user_data)
    response = Response(image,mimetype='image/svg+xml')
    response.headers['Cache-Control'] = 'public, max-age=3600'
    return response

@app.route('/user/<username>')
def show_user_profile(username):
    user_data = api.main.main(username)
    image = badge.create_svg(user_data)
    response = Response(image,mimetype='image/svg+xml')
    response.headers['Cache-Control'] = 'public, max-age=3600'
    return response

if __name__ == '__main__':
    app.run(debug=True)
