# Given name of calling program, a url and a string to wrap,
# output string in html body with basic metadata and open in Firefox tab.

import datetime
from webbrowser import open_new_tab


def wrapStringInHTMLMac(program, url, body):
    now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")
    filename = './html/' + program + '.html'
    f = open(filename, 'w')

    wrapper = """<html>
    <head>
    <title>%s output - %s</title>
    </head>
    <body><p>URL: <a href=\"%s\">%s</a></p><p>%s</p></body>
    </html>"""

    whole = wrapper % (program, now, url, url, body)
    f.write(whole)
    f.close()

    # Change the filepath variable below to match the location of your directory
    filename = 'file:///Users/udhavsethi/dev/rl-scheduling/' + filename

    open_new_tab(filename)


wrapStringInHTMLMac("testprogram", "www.google.com", "testbody")
