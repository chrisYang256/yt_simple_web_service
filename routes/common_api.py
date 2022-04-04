import datetime

from . import common_api


@common_api.route("api/server_time", methods=["GET"]) 
def get_servertime():
    return '{}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))