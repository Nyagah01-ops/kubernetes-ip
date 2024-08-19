from flask import Flask
from app.routes.user import user_blueprint

app = Flask(__name__)

app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
