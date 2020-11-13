import sys
import lxml.html
from  urllib.request import urlopen

def scraping(html):
    paper_list = html.cssselect('li.chapter-item')
    ret = []
    for paper in paper_list:
        title = paper.cssselect('a.content-type-list__link')[0]
        author = paper.cssselect('div.content-type-list__text')[0].text
        ret.append((title.text, title.get('href'), author))
    return ret

def format_pukiwiki(tup):
    return '* [[' + tup[0] + '(' + tup[2] + '):https://link.springer.com' + tup[1] + ']]'
    

args = sys.argv
tree = lxml.html.parse(urlopen(args[1]))
html = tree.getroot()
l = scraping(html)
for s in map(format_pukiwiki, l):
    print(s)


