from werkzeug.exceptions import HTTPException
from flask import Flask, Response, jsonify
import api.main
import image_generator.proto_badge as proto_badge
import image_generator.white_badge_en as white_badge_en
import image_generator.black_badge_en as black_badge_en
import image_generator.white_badge_ko as white_badge_ko
import image_generator.black_badge_ko as black_badge_ko
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
    image = proto_badge.create_svg(user_data)
    response = Response(image,mimetype='image/svg+xml')
    response.headers['Cache-Control'] = 'public, max-age=3600'
    return response

@app.route('/user/<username>')
def show_user_profile(username):
    user_data = api.main.main(username)
    image = proto_badge.create_svg(user_data)
    response = Response(image,mimetype='image/svg+xml')
    response.headers['Cache-Control'] = 'public, max-age=3600'
    return response

@app.route('/black/en/<username>')
def show_black_badge_en(username):
    user_data = api.main.main(username)
    image = black_badge_en.create_svg(user_data)
    response = Response(image,mimetype='image/svg+xml')
    response.headers['Cache-Control'] = 'public, max-age=3600'
    return response

@app.route('/white/en/<username>')
def show_white_badge_en(username):
    user_data = api.main.main(username)
    image = white_badge_en.create_svg(user_data)
    response = Response(image,mimetype='image/svg+xml')
    response.headers['Cache-Control'] = 'public, max-age=3600'
    return response



if __name__ == '__main__':
    app.run(debug=True)
