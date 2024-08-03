# Libraries
import requests
import time
import os

target_articles_count = int(input("Please enter a minimum number of articles to retrive (API downloads multiples of "
                                  "10): "))
# Search parameter
key_word = input('Please enter a keyword of a topic like "economy": ')


# Validates if I downloaded at least 100 articles
def test_number_of_articles(counter):
    if counter >= target_articles_count:
        print(f'\nThere are at least {target_articles_count} articles')
    else:
        print(f'\nThe amount of articles downloaded is less than {target_articles_count}')


# Main method of extraction
def extract_data():
    # This function will return a list of jsons
    jsons = []

    # Parameters to access the API
    # For the api key, I have saved it into a local environment variable
    api_key = os.environ.get('NYT_API_KEY')
    url_base = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'

    # article container
    articles_counter = 0
    page = 0

    # send request and save the JSON into json_responses folder
    while articles_counter < target_articles_count:

        # If the page is not the first one, this will delay 12 seconds as the NYT API documentation recommends
        if page > 0:
            time.sleep(12)

        # @q: key_word, what we are searching
        # @api_key: the key_value I saved previously in a local variable
        params = {'q': key_word, 'api-key': api_key, 'page': page}
        response = requests.get(url_base, params=params)

        # if the answer is success (status 200), we save the json into a file in json_responses
        if response.status_code == 200:
            # json content
            data = response.json()

            # jsons append
            jsons.append(data)

            # Counting the articles found in the request
            articles_count = len(data['response']['docs'])

            # Feed the global variable that counts the articles
            articles_counter += articles_count

            # Increase the page
            page += 1

            # Success message of the request response
            print(articles_counter, 'were downloaded')

        else:

            print(f"\nError to get data from API: {response.status_code}")

    # Validates the final number of downloaded articles
    test_number_of_articles(articles_counter)

    return jsons

#%%

#%%
