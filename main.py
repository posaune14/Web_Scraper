#create new presets for element/class for other news websites allow different
#buttons to be pressed for different websites potenital websites: usa today nbc

#pattern for usa today titles: http: then title then number, so we can just remove http and number
#also replace '-' with spaces

import tkinter as tk
import WebScraper


class Window:
  def __init__(self):
    self.window = tk.Tk()
    self.window.geometry('800x600')
    self.labels = []  

  def remove_labels(self):
    for label in self.labels:
      label.destroy()


#function that will set the url for the web scrape function
def button_clicked():
  #remove any existing labels before displaying new ones
  WindowHome.remove_labels()
  subject = WindowHome.window.searchBox.get() #url

  #scrape the articles from the apnew site
  articles = WebScraper.scrape(subject)
  #create a label for each article head
  for article in articles:
    WindowHome.window.label = tk.Label(WindowHome.window, text = article.text)
    WindowHome.window.label.pack()
    WindowHome.labels.append(WindowHome.window.label)
    
  
#tkinter window 
WindowHome = Window()

#button to initiate search
WindowHome.window.button = tk.Button(WindowHome.window, text='Search for Articles', command=button_clicked)
WindowHome.window.button.pack()

#search box on search page
WindowHome.window.searchBox = tk.Entry()
WindowHome.window.searchBox.pack()


#creating a link that opens a new browser page on function call 
#https://stackoverflow.com/questions/23482748/how-to-create-a-hyperlink-with-a-label-in-tkinter