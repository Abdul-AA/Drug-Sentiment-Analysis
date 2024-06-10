import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_reviews(url, drug_name):
    reviews = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    review_blocks = soup.find_all('div', class_='user-comment')
    
    for block in review_blocks:
        review_text = block.find('p', class_='comment-text').get_text()
        rating = block.find('span', class_='rating-score').get_text()
        condition = block.find('div', class_='condition').get_text().replace('Condition: ', '').strip()
        reviews.append({'drug': drug_name, 'review': review_text, 'rating': rating, 'condition': condition})
    
    return reviews

# URLs of the drug reviews pages
urls = {
    'Remicade': 'https://www.drugs.com/comments/infliximab/remicade.html',
    'Humira': 'https://www.drugs.com/comments/adalimumab/humira.html',
    'Enbrel': 'https://www.drugs.com/comments/etanercept/enbrel.html',
    'Simponi': 'https://www.drugs.com/comments/golimumab/simponi.html',
    'Cimzia': 'https://www.drugs.com/comments/certolizumab/cimzia.html',
    'Stelara': 'https://www.drugs.com/comments/ustekinumab/stelara.html',
    'Xeljanz': 'https://www.drugs.com/comments/tofacitinib/xeljanz.html'
}

all_reviews = []
for drug, url in urls.items():
    print(f'Scraping reviews for {drug}...')
    all_reviews.extend(get_reviews(url, drug))
    time.sleep(2)  # To avoid hitting the server too frequently

df = pd.DataFrame(all_reviews)
df.to_csv('drug_reviews.csv', index=False)
print("Scraping complete. Data saved to 'drug_reviews.csv'.")
