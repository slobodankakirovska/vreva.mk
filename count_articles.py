import json

def count_articles(json_file):
    # Load the JSON file
    with open(json_file, 'r', encoding='utf-8') as f:
        articles = json.load(f)

    # Count the number of articles
    num_articles = len(articles)

    print(f'Total number of articles scraped: {num_articles}')

# Specify the path to your JSON file
json_file_path = 'all_articles.json'

# Count the articles
count_articles(json_file_path)
