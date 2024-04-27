#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install requests')


# In[10]:


get_ipython().system('pip3 install beautifulsoup4')


# In[11]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[43]:


url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"
r = requests.get(url)
print(r)


# In[44]:


soup = BeautifulSoup(r.text, "lxml")
print(soup)


# In[45]:


url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
np = soup.find ("a", class_ = "_1LKTO3").get("href")
cnp = "https://www.flipkart.com"+np
url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"
r = requests.get(url)print(cnp)


# In[60]:


for i in range(2, 10):
    url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    # Check if the tag is found before trying to access its attributes
    link_tag = soup.find("a", class_="_1LKTO3")
    
    if link_tag is not None:
        np = link_tag.get("href")
        cnp = "https://www.flipkart.com" + np
        print(cnp)
    else:
        print(f"No matching tag found on page {i}")


# In[78]:


import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []

url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

names = box.find_all("div", class_ = "_4rR01T")
#print(names)

for i in names:
    name = i.text
    Product_name.append(name)
    
print(Product_name)

prices = soup.find_all("div", class_ = "_30jeq3 _1_WHN1")
#print(prices)

for i in prices:
    name = i.text
    Prices.append(name)
print(Prices)


desc = soup.find_all ("ul", class_ = "_1xgFaf")

for i in desc:
    name = i.text
    Description.append(name)
    
print(Description)

review = soup.find_all ("div", class_ = "_3LWZlK")

for i in review:
    name = i.text
    Reviews.append(name)
    
print(Reviews)
print(len(Reviews))


# In[85]:


import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []

url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

names = box.find_all("div", class_ = "_4rR01T")
#print(names)

for i in names:
    name = i.text
    Product_name.append(name)
    
print(Product_name)

prices = box.find_all("div", class_ = "_30jeq3 _1_WHN1")
#print(prices)

for i in prices:
    name = i.text
    Prices.append(name)
print(Prices)


desc = box.find_all ("ul", class_ = "_1xgFaf")

for i in desc:
    name = i.text
    Description.append(name)
    
print(Description)

review = box.find_all ("div", class_ = "_3LWZlK")

for i in review:
    name = i.text
    Reviews.append(name)
    
print(Reviews)


# In[90]:


Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(2,12):
    url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")
    
    names = box.find_all("div", class_ = "_4rR01T")
#print(names)

for i in names:
    name = i.text
    Product_name.append(name)
    
#print(Product_name)

prices = box.find_all("div", class_ = "_30jeq3 _1_WHN1")
#print(prices)

for i in prices:
    name = i.text
    Prices.append(name)
#print(Prices)


desc = box.find_all ("ul", class_ = "_1xgFaf")

for i in desc:
    name = i.text
    Description.append(name)
    
#print(Description)

review = box.find_all ("div", class_ = "_3LWZlK")

for i in review:
    name = i.text
    Reviews.append(name)
    
#print(Reviews)

Flipkart = pd.DataFrame({"Product Name":Product_name, "Prices":Prices, "Description":Description, "Reviews":Reviews})


# In[91]:


Flipkart


# In[99]:


import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(2, 10):
    url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    names = box.find_all("div", class_ = "_4rR01T")
#print(names)

    for i in names:
        name = i.text
        Product_name.append(name)
    
#print(Product_name)

    prices = box.find_all("div", class_ = "_30jeq3 _1_WHN1")
#print(prices)

    for i in prices:
        name = i.text
        Prices.append(name)
#print(Prices)


    desc = box.find_all ("ul", class_ = "_1xgFaf")

    for i in desc:
        name = i.text
        Description.append(name)
    
#print(Description)

    review = box.find_all ("div", class_ = "_3LWZlK")

    for i in review:
        name = i.text
        Reviews.append(name)
    
#print(Reviews)
    
Flipkart_Data = pd.DataFrame({"Product Name":Product_name, "Prices":Prices, "Description":Description, "Reviews":Reviews})   


# In[101]:


Flipkart_Data


# In[102]:


Flipkart.to_csv("C:/Users/admin/OneDrive/Desktop/Interview prepration/Python/Flipkart_mobile_under_50000.csv")


# In[103]:


Flipkart_Data.to_csv("C:/Users/admin/OneDrive/Desktop/Interview prepration/Python/Flipkart_Data_mobile_under_50000.csv")


# In[ ]:




