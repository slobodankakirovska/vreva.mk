import json
import re

def clean_text(text):
    """Clean the text by removing unwanted characters and extra spaces."""
    if text is None:
        return ""
    cleaned_text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    cleaned_text = ' '.join(cleaned_text.split())
    return cleaned_text

def process_article(article):
    """Process a single article to clean the text and combine title with text."""
    title = article.get('title', '') or ''
    text = article.get('text', []) or []
    category = article.get('category', '') or ''
    
    # Clean the title and convert to a single string if it's a list
    cleaned_title = clean_text(title)
    
    # Clean each paragraph in the text and combine them into a single string
    combined_text = cleaned_title + " " + " ".join([clean_text(paragraph[1]) for paragraph in text if len(paragraph) > 1 and paragraph[0] == 'p'])
    
    # Create a new dictionary for the cleaned article
    cleaned_article = {
        'title': cleaned_title,
        'text': combined_text,
        'category': clean_text(category)
    }
    
    return cleaned_article

def clean_articles(input_file, output_file):
    """Clean articles from the input JSON file and save to the output JSON file."""
    try:
        with open(output_file, 'r', encoding='utf-8') as f:
            cleaned_articles = json.load(f)
            existing_titles = set(article['title'] for article in cleaned_articles)
    except (FileNotFoundError, json.JSONDecodeError):
        cleaned_articles = []
        existing_titles = set()

    # Load the original JSON file
    with open(input_file, 'r', encoding='utf-8') as f:
        articles = json.load(f)
    
    # Process each article only if it hasn't been cleaned yet
    for article in articles:
        title = article.get('title', '')
        if title not in existing_titles:
            cleaned_article = process_article(article)
            cleaned_articles.append(cleaned_article)
            existing_titles.add(title)
    
    # Save the cleaned articles to a new JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_articles, f, ensure_ascii=False, indent=4)
    
    print(f'Cleaned articles saved to {output_file}')

# Specify the paths to your input and output JSON files
input_file_path = 'all_articles.json'
output_file_path = 'cleaned_articles.json'

# Clean the articles
clean_articles(input_file_path, output_file_path)
