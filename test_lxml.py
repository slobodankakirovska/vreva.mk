from bs4 import BeautifulSoup

xml_content = "<root><child>Test</child></root>"
soup = BeautifulSoup(xml_content, 'xml')
print(soup.prettify())
