from flask import Flask
from subtract_app import subtraction_bp

def create_app():
    app=Flask(__name__)

    #blueprints
    app.register_blueprint(subtraction_bp)

    return app

app=create_app()

if __name__=='__main__':
    app.run(debug=True)