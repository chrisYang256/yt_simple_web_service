from flask import Blueprint

common_api = Blueprint("common_api", __name__, url_prefix="/common")
company_api = Blueprint("company_api", __name__, url_prefix="/company")
company_view = Blueprint("company_view", __name__, url_prefix="/company")
user_api = Blueprint("user_api", __name__, url_prefix="/user")
user_view = Blueprint("user_view", __name__, url_prefix="/user")

from .common_api   import *
from .company_api  import *
from .company_view import *
from .user_api     import *
from .user_view    import *

