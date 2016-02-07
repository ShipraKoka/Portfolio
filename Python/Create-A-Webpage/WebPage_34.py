import webbrowser

url = "SummerSale.html"
webPage = open(url,'w')

contents = """<html>
<body>Stay tuned for our amazing summer sale!</body>
</html>"""

webPage.write(contents)
webPage.close()

webbrowser.open(url)

#Internet Explorer
ie = webbrowser.get('c:\\program files (x86)\\internet explorer\\iexplore.exe')
ie.open(url)

