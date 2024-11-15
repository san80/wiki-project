from django.shortcuts import render
from django.http import HttpResponse
import markdown2
import re

from . import util


def index(request):
    print("Index callaed")
    # return HttpResponse("<p>welcome</p>")
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def title(request,name):
    content=util.get_entry(name)
    content_html=markdown2.markdown(content)
    return render(request,"encyclopedia/page.html",{"content":content_html, "name":name})
def search(request):
    print("Got in search")
    querys=request.GET["q"]
    #querys=".*".join(querys)
    entries=util.list_entries()
    matches=[]

    for entry in entries:
        # regex_pattern=''.join(f'(?=.*{char})' for char in querys)
        # if(re.search(regex_pattern,entry.lower())):
        #     matches.append(entry)
    #     for q in querys.lower():
    #         if q in entry.lower():
    #             continue
    #         else:
    #             return render(request,"encyclopedia/search.html",{"match": matches})
    #     matches.append(entry)
        if querys.lower() in entry.lower():
            matches.append(entry)
    return render(request,"encyclopedia/search.html",{"match": matches})
def opennew(request):
    try:
        title=request.GET['name']
        content=request.GET['content']
        return render(request,"encyclopedia/create.html",{"name":title, "content":content})
    except:
        return render(request,"encyclopedia/create.html")
def createnewpage(request):
    title=request.GET['title']
    content=request.GET['content']
    util.save_entry(title,content)
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def edit(request):
   
    title=request.GET['get_name']
    content=util.get_entry(title)
    return render(request,"encyclopedia/edit.html",{"name":title , "content":content})

