import urllib.request
import webbrowser as web
url = "http://google.de"
content = urllib.request.urlopen(url).read()
open("google.html","wb").write(content)
web.open_new_tab("google.html")
