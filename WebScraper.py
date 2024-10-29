#use vscode, fix webbrowser issue, then find preset elements and integrate into scape function

import requests
from bs4 import BeautifulSoup

def presets():
  apnews = [f'https://apnews.com/search?q={subject}#nt=navsearch', element, classname]
  def return_apnews_link():
    return apnews[0]
#Function to scrape a provided url
def scrape(subject, preset):
  url = (f'https://apnews.com/search?q={subject}#nt=navsearch')
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  articles = soup.find_all('span', {'class':'PagePromoContentIcons-text'})

  #this holds the bad articles
  articles_to_remove = []
  #for article in articles:
   # print(articles.text)
  #find bad articles
  for article in articles:
    if article.text.find(subject) == -1:
        articles_to_remove.append(article)
      
  #remove bad articles
  for article in articles_to_remove:
      articles.remove(article)
  
  

  #find way to scrape articles with different text formatting
  #print article headers without all the html mumbo jumbo using a for loop
  #for article in articles:
    #print(article.text)
  return articles
def createUrl():
  pass
  #receive subject and create url for webscrape function

#Associate press ai search query

#website = (f'https://apnews.com/search?q={subject}#nt=navsearch')





















#gui for the app
#gui will have a search bar 
#the search bar will scrape google, nytimes, and more
#give the user the search results
#user can select an article and get a chatgpt summary
#pyqt 
#tutorial site
#https://www.tutorialspoint.com/pyqt/pyqt_layout_management.htm


'''
#defines url for web scrape
response1 = requests.get(website[0])
response2 = requests.get(website[1])

#creates an object based on website informaton 
soup1 = BeautifulSoup(response1.content, "html.parser")
soup2 = BeautifulSoup(response2.content, "html.parser")

#print(soup2.prettify())

#function needs to know what code the content is in (html), so that the parser can work
titles1 = soup1.find_all('h4')
titles2 = soup2.find_all('div', {'class':'BNeawe vvjwJb AP7Wnd'})
titles3 = soup2.find_all('a')

for article in titles1:
  print(article.text)
  
for i in range(4):
  print('')
  
for article in titles2:
  print(article.text)
  
for i in range(4):
  print('')
  
for link in titles3:
  url=link.get('href')
  if url.find('url') != -1 and url.find('google') == -1:
    print(url.replace('/url?q=', ''))
  

    #response = requests.get(url.replace('/url?q=', ''))
    #rescraping new article 
    #soup = BeautifulSoup(response.content, "html.parser")
    #the 
    #text=soup.find_all('div', {'class':'l-container'})
    #print('trying to print text article')
    #print(text)
    #print(soup)
    
    
#we are taking the url for the articles so the websites can be scraped for information
  
#Helpful Sites / Knowledge
#Site with Tutorial for Beautiful Soup and understanding the code
#https://realpython.com/beautiful-soup-web-scraper-python/#reasons-for-web-scraping

#https://opensource.com/article/21/9/web-scraping-python-beautiful-soup
#https://news.google.com/home?hl=en-US&gl=US&ceid=US:en
#https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
#https://beautiful-soup-4.readthedocs.io/en/latest/
#for loop
#response 
#soup
#soup findall( if url starts with nytimes use h4 if it starts with wall street use blah blah)
#print titles for each site

#gui for the app
#gui will have a search bar 
#the search bar will scrape google, nytimes, and more
#give the user the search results
#user can select an article and get a chatgpt summary '''
