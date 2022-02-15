from django.shortcuts import render
from django.http import HttpResponse

import MySQLdb as mysql
import yaml

# Create your views here.
def index(request):
    with open("dbconfig.yaml") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    db = mysql.connect(host=config['DB']['HOST'],
                    port=config['DB']['PORT'],
                    user=config['DB']['USER'],
                    passwd=config['DB']['PASSWD'],
                    db=config['DB']['NAME'],
                    charset="utf8")
    cursor = db.cursor()

    
    cursor.execute("select distinct cat from eat_meta")
    meta_cat = cursor.fetchall()

    cat = request.GET.get("cat", "")
    _type = request.GET.get("type", "")
    subtype = request.GET.get("sub", "")

    if cat:
        q_filter = " where cat = '{}'".format(cat)
        cursor.execute("select distinct cat, type from eat_meta where cat = '{}'".format(cat))
        meta_type = cursor.fetchall()

        if _type:
            cursor.execute("select cat, type, subtype from eat_meta where cat = '{}' and type = '{}' and subtype is not null".format(cat, _type))
            meta_subtype = cursor.fetchall()

            if subtype:
                q_filter = " where cat = '{}' and type = '{}' and subtype = '{}'".format(cat, _type, subtype)
            else:
                q_filter = " where cat = '{}' and type = '{}'".format(cat, _type)
        else:
            meta_subtype = ""

    else:
        q_filter = ""
        meta_type = ""
        meta_subtype = ""


    cursor.execute("select * from eat" + q_filter + " order by name")
    a = cursor.fetchall()

    header = ': '.join([i for i in [cat, _type, subtype] if i != ""])

    return render(request, "eat/eat.html", {
        "nitems": len(a),
        "items": a,
        "header": header,
        "meta_cat": meta_cat,
        "meta_type": meta_type,
        "meta_subtype": meta_subtype,
    })