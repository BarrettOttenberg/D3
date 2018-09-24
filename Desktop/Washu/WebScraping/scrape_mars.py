# Dependencies

from bs4 import BeautifulSoup

import requests

import pandas as pd

from splinter import Browser

import requests





#function to initialize browser

def init_browser():

    executable_path = {'executable_path': r'C:\Users\bott00a\Desktop\Washu\chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)



# ### NASA Mars News



def scrape():

    browser = init_browser()

    mars = {}



    nasa_url= 'https://mars.nasa.gov/news/'

    browser = init_browser()

    browser.visit(nasa_url)

    news_title = browser.find_by_css('.content_title').first.text

    news_p = browser.find_by_css('.article_teaser_body').first.text

    

# ### JPL Mars Space Images - Featured Image



    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    browser = init_browser()

    browser.visit(jpl_url)

    jpl_html = browser.html

    jpl_soup = BeautifulSoup(jpl_html, 'html.parser')

    jpl_results = jpl_soup.find('article')

    extension = jpl_results.find('a')['data-fancybox-href']

    jpl_link = "https://www.jpl.nasa.gov"

    featured_image_url = jpl_link + extension



# ## Mars Weather



    mars_twitter_url = 'https://twitter.com/marswxreport?lang=en'

    browser = init_browser()

    browser.visit(mars_twitter_url)

    for text in browser.find_by_css('.tweet-text'):

        if text.text.partition(' ')[0] == 'Sol':

            mars_weather = text.text

        break

    

# ## Mars Facts



    mars_facts_url = 'https://space-facts.com/mars/'

    mars_facts_df =  pd.read_html (mars_facts_url, attrs = {'id': 'tablepress-mars'})[0]

    mars_facts_df.columns = ['Measurement','Value']

    mars_fact_df = mars_facts_df.set_index('Measurement')

    mars_facts_html = mars_fact_df.to_html()

    

# ## Mars Hemisperes



    hemisperes_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    hemisperes_response = requests.get(hemisperes_url)

    hemisperes_soup = BeautifulSoup(hemisperes_response.text, 'html.parser')



    hemisperes_list = hemisperes_soup.find_all('a', class_="itemLink product-item")

    hemisperes_list



    hemisphere_image_urls = []

    for hemi_img in hemisperes_list:

        img_title = hemi_img.find('h3').text

        link_to_img = "https://astrogeology.usgs.gov/" + hemi_img['href']

        img_request = requests.get(link_to_img)

        soup = BeautifulSoup(img_request.text, 'html.parser')

        img_tag = soup.find('div', class_='downloads')

        img_url = img_tag.find('a')['href']

        hemisphere_image_urls.append({"Title": img_title, "Image_Url": img_url})

    

    

    mars_data = {

     "News_Title": news_title,

     "Paragraph_Text": news_p,

     "Most_Recent_Mars_Image": featured_image_url,

     "Mars_Weather": mars_weather,

     "Mars_hem": hemisphere_image_urls,

     "Mars_Facts" : mars_facts_html

     

     }

    return mars_data  