html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class='title' name='dormouse'><b>Thie dormouse's story</b></p>
    <p class='story'>Once upon a time there little sisters; and their names were
    <a class='sister' href='http://example.com/elsie'  id='link1'><!--Elsie--></a>
    <a class='sister' href='http://example.com/lacie' id='link2'>Lacie</a>
    <a class='sister' href='http://example.com/tillie' id='link3'>Tillie</a>
    and they lived at the bottom of a well.</p>
    <p class='story'>...</p>
    """
from pyquery import PyQuery as pq

doc = pq(url='http://cuiqingcai.com')
# print(doc)
items = doc('body .main .ws_images li')
# print(items)
lis = items.find('img').items()
print(lis)
for li in lis:
    print(li.attr('title'))
