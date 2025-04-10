from werkzeug.exceptions import HTTPException
from flask import Flask, Response, jsonify
import api.main
import badge_generator.v1_badge as v1_badge
import badge_generator.v2_badge_en as v2_badge_en
import badge_generator.v2_badge_ko as v2_badge_ko
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
def show_prototype_badge(username):
    user_data = api.main.main(username)
    image = v1_badge.create_svg(user_data)
    response = Response(image,mimetype='image/svg+xml')
    response.headers['Cache-Control'] = 'public, max-age=3600'
    return response

@app.route('/user/<username>')
def show_user_profile(username):
    user_data = api.main.main(username)
    image = v1_badge.create_svg(user_data)
    response = Response(image,mimetype='image/svg+xml')
    response.headers['Cache-Control'] = 'public, max-age=3600'
    return response

@app.route('/v2/en/<username>')
def show_black_badge_en(username):
    user_data = api.main.main(username)
    image = v2_badge_en.create_svg(user_data)
    response = Response(image,mimetype='image/svg+xml')
    response.headers['Cache-Control'] = 'public, max-age=3600'
    return response

@app.route('/v2/ko/<username>')
def show_white_badge_en(username):
    user_data = api.main.main(username)
    image = v2_badge_ko.create_svg(user_data)
    response = Response(image,mimetype='image/svg+xml')
    response.headers['Cache-Control'] = 'public, max-age=3600'
    return response

if __name__ == '__main__':
    app.run(debug=True)
