from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(executable_path=r"C:\Users\Pieter\Documents\chromedriver.exe")
wordlist=[]

driver.get("https://nl.wikwik.org/woorden12letter.htm")
content = driver.page_source
soup = BeautifulSoup(content)
paragraph = soup.find_all('p')[2]
text = paragraph.get_text()
text.split()
print


for n in range(1,2):
    if n == 1:
        driver.get("https://nl.wikwik.org/woorden12letter.htm")
        pindex = 2
    else:
        driver.get("https://nl.wikwik.org/woorden12letterpagina"+str(n)+".htm")
        pindex = 3
    content = driver.page_source
    soup = BeautifulSoup(content)
    paragraph = soup.find_all('p')[pindex]
    text = paragraph.get_text()
    wordlist += text.split()
driver.quit()

with open("wordlist.txt", "wb") as f:
    for word in wordlist:
        wordspace = str(word + " ")
        f.write(wordspace.encode('utf-8'))