from bs4 import BeautifulSoup

file = open("Yes_products_datasets.txt", 'a',encoding="utf-8")
with open("AliExpress - Online Shopping for Popular Electronics, Fashion, Home & Garden, Toys & Sports, Automobiles and More.htm","r", encoding="utf-8") as html:
    soup = BeautifulSoup(html, 'lxml')
    
    products = soup.find_all('div',{"class":"recommend-card--card-wrap--2jjBf6S"})
    
    #print(len(products))

    for prod in products:
        result = f'{prod.text.strip().replace(",",".")},Yes\n'
        print(result)
        file.write(result)
        
#close the file
file.close()
