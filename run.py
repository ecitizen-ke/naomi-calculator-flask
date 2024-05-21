from flask import Flask
from divide_app import division_bp

def create_app():
    app=Flask(__name__)

    #blueprints
    app.register_blueprint(division_bp)

    return app

app=create_app()

if __name__=='__main__':
    app.run(debug=True)