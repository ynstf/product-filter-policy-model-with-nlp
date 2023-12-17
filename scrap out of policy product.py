import requests
from bs4 import BeautifulSoup


file = open("No_products_datasets.txt", 'a',encoding="utf-8")


for i in range(100):
    
    #drugs product
    URL_drugs = f"https://www.alibaba.com/trade/search?spm=a2700.galleryofferlist.0.0.67654d0ffz02DC&fsb=y&IndexArea=product_en&keywords=drugs&tab=all&&page={i}"
    page = requests.get(URL_drugs)
    
    #all product in page
    soup_drugs = BeautifulSoup(page.content, 'lxml')
    products_drugs = soup_drugs.find('div',{"class":"organic-list"})
    products = products_drugs.find_all('h2',{"class":"search-card-e-title"})
    
    for prod in products:
        result = f'{prod.text.strip().replace(",",".")},No\n'
        print(result)
        file.write(result)
    
    
    #weapons product

    URL_weapons = f"https://www.alibaba.com/trade/search?spm=a2700.galleryofferlist.0.0.52b17b25sK57NN&fsb=y&IndexArea=product_en&keywords=weapons&tab=all&&page={i}"
    page = requests.get(URL_weapons)
    
    #all product in page
    soup_weapons = BeautifulSoup(page.content, 'lxml')
    products_weapons = soup_weapons.find('div',{"class":"organic-list"})
    products = products_weapons.find_all('h2',{"class":"search-card-e-title"})
    
    for prod in products:
        result = f'{prod.text.strip().replace(",",".")},No\n'
        print(result)
        file.write(result)



    #sexual product

    URL_sexual = f"https://www.alibaba.com/trade/search?spm=a2700.galleryofferlist.0.0.5d906a1emVhJce&fsb=y&IndexArea=product_en&keywords=sexual+objects&tab=all&&page={i}"
    page = requests.get(URL_sexual)
    
    #all product in page
    soup_sexual = BeautifulSoup(page.content, 'lxml')
    products_sexual = soup_sexual.find('div',{"class":"organic-list"})
    products = products_sexual.find_all('h2',{"class":"search-card-e-title"})
    
    for prod in products:
        result = f'{prod.text.strip().replace(",",".")},No\n'
        print(result)
        file.write(result)


#close the file
file.close()