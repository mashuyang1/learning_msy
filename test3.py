from bs4 import BeautifulSoup
html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class='title' name='dormouse'><b>Thie dormouse's story</b></p>
    <p class='story'>Once upon a time there little sisters; and their names were
    <a href='http://example.com/elsie' class='sister' id='link1'><!--Elsie--></a>
    <a class='sister' href='http://example.com/lacie' id='link2'>Lacie</a>
    <a class='sister' href='http://example.com/tillie' id='link3'>Tillie</a>
    and they lived at the bottom of a well.</p>
    <p class='story'>...</p>
    """
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
# print(soup.title.string)
# print(type(soup.title))
# print(soup.a)
# print(soup.p.contents)
# print(soup.title.name)
# print(soup.p.attrs)
# print(soup.p['class'])
# print(list(enumerate(soup.a.next_siblings)))
# print(soup.a.next_sibling.next_sibling)
# print(type(soup.a.parents))
print(soup.find_all(name='a'))
print(soup.find_all(attrs='sister'))
