#!/usr/bin/env python
# coding: utf-8

# # Session 7 Assignment 

# # 1

# In[1]:


import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://www.colorado.edu/ecenter/2021/03/17/positive-impact-organic-foods"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the text content
    page_content = soup.get_text()

    # Save the content to a text file
    with open("web_content.txt", "w", encoding="utf-8") as file:
        file.write(page_content)

    print("Web content has been successfully saved to 'web_content.txt'.")
else:
    print(f"Error: Unable to fetch content. Status Code: {response.status_code}")


# In[ ]:




