from bs4 import BeautifulSoup
import os

cmd='dir'
res = os.popen(cmd).read()

page_number = len(res.split(".htm"))-1

file = open("Yes_products_datasets.txt", 'a',encoding="utf-8")

for n in range(1,page_number+1):

    #file = input('enter your amazon page : ')
    with open(f"Amazon{n}.htm","r", encoding="utf-8") as html:
        soup = BeautifulSoup(html, 'lxml')
    
    products = soup.find_all('div',{"class":"DealContent-module__truncate_sWbxETx42ZPStTc9jwySW"})

    for prod in products:
        result = f'{prod.text.strip().replace(",",".")},Yes\n'
        #print(result)
        print(n)
        file.write(result)

#close the file
file.close()
