# Remember to read the instructions in the task description (section-1/docs/task-1-data-extraction.md)
# Your implementation here

# Libraries
import requests
import os
import time
import json


# Validates if I downloaded at least 100 articles
def test_number_of_articles(counter):
    if counter >= 100:
        print('\nThere are at least 100 articles')
    else:
        print('\nThe amount of articles downloaded is less than 100')


# Main method of extraction
def extract_data():
    # Set destination for the json files
    destination_folder = os.path.join(os.getcwd(), 'json_responses')

    # Erase previous json files
    for file in os.listdir(destination_folder):
        if file.endswith('.json'):
            full_file = os.path.join(destination_folder, file)
            os.remove(full_file)

    # Parameters to access the API
    # For the api key, I have saved it into a local environment variable
    api_key = os.environ.get('NYT_API_KEY')
    url_base = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'

    # Search parameter
    key_word = 'economy'

    # article container
    articles_counter = 0
    page = 0

    # send request and save the JSON into json_responses folder
    while articles_counter < 100:

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

            # Filename
            file_name = 'page_' + str(page) + '_response.json'
            # Filename with path
            file_path = os.path.join(destination_folder, file_name)

            # Saving the variable into json format
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

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
