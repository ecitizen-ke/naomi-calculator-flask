from flask import Flask
from multiply_app import multiplication_bp

def create_app():
    app = Flask(__name__)

    #blueprints
    app.register_blueprint(multiplication_bp)

    return app

app=create_app()

if __name__=='__main__':
    app.run(debug=True)