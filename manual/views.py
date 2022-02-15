from django.shortcuts import render
from django.http import HttpResponse

from os import listdir
from os.path import isfile, join
from html.parser import HTMLParser

class myparser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.h2s = []
        self.ish2 = False
    
    def handle_starttag(self, tag, attrs):
        if tag == "h2":
            self.ish2 = True

    def handle_endtag(self, tag):
        if tag == "h2":
            self.ish2 = False

    def handle_data(self, data):
        if self.ish2:
            self.h2s.append(data)

# Create your views here.
def index(request):

    item = "index"
    try:
        item = request.GET['item']
    except:
        pass

    # get manual list by reading template/manual directory
    manual_list = filter(
        lambda x: x != "index", 
            [f.split("-")[1].split(".html")[0] 
                for f in listdir("templates/manual") if isfile(join("templates/manual", f))
            ])

    htmldoc = "manual/manual-{}.html".format(item)

    # parse HTML and get <h2> list (for TOC)
    parser = myparser()
    with open("templates/" + htmldoc) as f:
        parser.feed(f.read())

    return render(
        request, 
        htmldoc,
        {
            "manual_list": manual_list,
            "manname": item,
            "h2s": parser.h2s,
            "idx": 0,
        })