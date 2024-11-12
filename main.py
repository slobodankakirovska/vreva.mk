from config import websites
from crawler import Crawler, get_article_links
import json
import os


def main():
    all_scraped_data = []
    existing_links = set()

    # Load existing links if the file exists
    if os.path.exists('all_articles.json'):
        with open('all_articles.json', 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
            existing_links = {article['references'] for article in existing_data}

    for site in websites:
        sitemap = site.url.endswith('.xml')
        article_links = get_article_links(site.url, 'a', is_sitemap=sitemap)

        crawler = Crawler(site)
        
        for link in article_links:
            if link in existing_links:
                continue

            print(f"SCRAPING LINK: {link}")
            page_data = crawler.parse(link)
            if page_data:
                all_scraped_data.append(page_data)
                existing_links.add(link)

    # Append new data to the existing JSON file
    if os.path.exists('all_articles.json'):
        with open('all_articles.json', 'r+', encoding='utf-8') as f:
            existing_data = json.load(f)
            existing_data.extend(all_scraped_data)
            f.seek(0)
            json.dump(existing_data, f, ensure_ascii=False, indent=4)
    else:
        with open('all_articles.json', 'w', encoding='utf-8') as f:
            json.dump(all_scraped_data, f, ensure_ascii=False, indent=4)

    print("Data exported to 'all_articles.json'")

if __name__ == '__main__':
    main()
