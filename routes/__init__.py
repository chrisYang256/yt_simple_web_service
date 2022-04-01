from flask import Blueprint
company_api = Blueprint('company_api', __name__, url_prefix="/company/")
company_view = Blueprint('company_view', __name__, url_prefix="/company/")

from .company_api import *
from .company_view import *