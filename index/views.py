from django.shortcuts import render
from django.db import connection

from .const import *

import sys


# Create your views here.

def index(request):
    args = dict()

    with connection.cursor() as cursor:
        cursor.execute("select * from updates")
        args['updates'] = sorted(list(cursor.fetchall()), key=lambda x: x[2], reverse=True)
        

    args['message'] = "some-message"
    args['main_desc'] = LOREM

    msg = "some-message"
    return render(
        request, 
        "index/index.html",
        args
    )