# Dependencies
from bs4 import BeautifulSoup
import requests
import os
import re
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np


def init_browser():
    #chromium path 
    chromiumPath=r'C:/Users/floPe/OneDrive/Desktop/chromedriver.exe'
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": chromiumPath}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()

    # url being scrapted
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # title of news article
    info = soup.find('div', "content_title")
    news_title=info.text.strip()
    news_title



    # description of news article
    news_p=soup.find('div', "rollover_description_inner").text.strip()


    # Scraper 2 for Image

    #jpl.nasa.gov mars featured image
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)
    html = browser.html
    soup2 = BeautifulSoup(html, 'html.parser')


    # find featured image 
    image_info = soup2.find('a',"button fancybox")
    # find relative location of image
    image_url=image_info['data-fancybox-href']
    # add relative url if image to site url
    featured_image_url='https://www.jpl.nasa.gov'+image_url


    # Scraper 3 for mars weather Tweet


    #https://twitter.com/marswxreport?lang=en for Tweet

    url3 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url3)
    html = browser.html
    soup3 = BeautifulSoup(html, 'html.parser')

    # find tweet
    tweet_info = soup3.find("div","tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content original-tweet js-original-tweet has-cards has-content")

    # get weather text
    mars_weather=tweet_info.find("div", class_="js-tweet-text-container").text.strip()



    # Scraper 4 for Mars Data Table



    #https://space-facts.com/mars/ for table info

    url4 = 'https://space-facts.com/mars/'
    browser.visit(url4)
    html = browser.html
    soup4 = BeautifulSoup(html, 'html.parser')

    table=soup4.find("table", "tablepress tablepress-id-p-mars")
    mars_table = pd.read_html(url4)
    table_df= pd.DataFrame(mars_table[0])
    table_df.columns = ["Profile", "Data"]
    mars_df2 = table_df.set_index("Profile")
    table_info = mars_df2.to_html(index = False)




    # Scraper 5 for High res. photos


    #https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars for table info

    url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url5)

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup5 = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain book information
    images=soup5.find_all('div', "item")

    #list
    titles=[]

    hemisphere_image_urls=[]


    usgs_link='https://astrogeology.usgs.gov'
    for image in images:
    # Use Beautiful Soup's find() method to navigate and retrieve attributes
        link = image.find('a')
        title=image.find('h3').text
        browser.click_link_by_partial_text(title)
        
        html = browser.html
    # Parse HTML with Beautiful Soup
        soupx = BeautifulSoup(html, 'html.parser')
    # find link for image .jpg
        imagex=soupx.find('div', 'downloads')
        image_x=imagex.find('a')

    # title and liks to list
        hemisphere_image_urls.append({'title': title, 'img_url': image_x['href']})

        browser.visit(url5)

   # Store data in a dictionary
    mars_data = {}
    
    mars_data['news_title']= news_title
    mars_data['news_p']= news_p
    mars_data['featured_image_url']=featured_image_url
    mars_data['mars_weather']= mars_weather
    mars_data['table_info']=table_info
    mars_data['hemisphere_image_urls']=hemisphere_image_urls
        
    


     # Close the browser after scraping
    browser.quit()
     # Return results
    
    return mars_data

  