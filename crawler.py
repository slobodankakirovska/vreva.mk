import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class Crawler:
    def __init__(self, site):
        self.site = site

    def getPage(self, url):
        try:
            req = requests.get(url)
            return BeautifulSoup(req.text, 'html.parser')
        except requests.exceptions.RequestException:
            return None

    def safeGet(self, pageObj, selector):
        selectedElems = pageObj.select(selector)
        if selectedElems and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''

    def safeGetAttr(self, pageObj, selector, attr):
        selectedElem = pageObj.select_one(selector)
        if selectedElem and attr in selectedElem.attrs:
            return selectedElem.attrs[attr]
        return ''

    def parse(self, url):
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, self.site.titleTag)
            body = [(tag.name, tag.get_text()) for tag in bs.find_all(self.site.bodyTags)]
            image = self.safeGetAttr(bs, self.site.imageTag, 'src')
            author = self.safeGet(bs, self.site.authorTag)
            date_published = self.safeGetAttr(bs, self.site.dateTag, 'datetime')
            category = self.safeGet(bs, self.site.category)
            if title and body:
                return {
                    'title': title or None,
                    'text': body or None,
                    'img': [image] if image else None,
                    'author': author or None,
                    'publisher': self.site.name,
                    'date of publication': date_published or None,
                    'references': url,
                    'category': category or None
                }
        return None

from bs4 import BeautifulSoup

def get_article_links(homepage_url, links_tag, is_sitemap=False):
    try:
        response = requests.get(homepage_url)
        soup = BeautifulSoup(response.content, 'html.parser' if not is_sitemap else 'lxml')
        links = [loc.get_text() for loc in soup.find_all('loc')] if is_sitemap else [urljoin(homepage_url, a['href']) for a in soup.find_all(links_tag) if 'href' in a.attrs]
        return links
    except requests.RequestException as e:
        print(f"Error fetching homepage: {e}")
        return []

