from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.flipkart.com/apple-iphone-x-space-gray-64-gb/p/itmexrgv6hctyrav?pid=MOBEXRGVCMGVCGGQ&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_pr&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_pr&lid=LSTMOBEXRGVCMGVCGGQFLD1LA&fm=SEARCH&iid=7b28ec7e-21bd-4244-9283-5afa1de2c1f3.MOBEXRGVCMGVCGGQ.SEARCH&ppt=sp&ppn=sp&ssid=rzawizgivk0000001567695382717&qH=882a0465d260983a'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("div", {"class":"_1HmYoV _35HD7C"})
# print(containers)
# print(len(containers)) # return numbers of products in a page
# print(soup.prettify(containers[0])) # return the page in html format basically all the classes and id and html tags will be returned

container = containers[0]
#print(container.div.img["alt"])

price = container.findAll("div",{"class":"_1_nB2f"})
print(price[0].text)

raitings = container.findAll("div",{"class":"niH0FQ"}) #  hGSR34 use this class for prices only
print(raitings[0].text)