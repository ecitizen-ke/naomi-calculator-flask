from flask import Blueprint
#blueprint enables for many python packages which will be registered in main run file
#blueprints created for each feature i.e every init file
#create blueprint
addition_bp=Blueprint('addition_bp',__name__)

from . import routes

    

    