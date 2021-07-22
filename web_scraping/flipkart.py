# phone specs and price from flipkart

from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DApple&otracker=clp_metro_expandable_7_3.metroExpandable.METRO_EXPANDABLE_iPhone_mobile-phones-store_92RED14GXPXF_wp3&fm=neo%2Fmerchandising&iid=M_80bdd5ab-72cf-462b-bd36-f2119a4c9bf4_3.92RED14GXPXF&ppt=hp&ppn=homepage&ssid=fhh0qjup2o0000001626796620162')

soup = BeautifulSoup(html_text.content, 'lxml')
phones = soup.find_all('div', class_="_3pLy-c row")
for phone in phones:

    name = phone.find('div', class_='_4rR01T').text
    if 'iPhone 12' in name:
        price = phone.find('div', class_='_30jeq3 _1_WHN1').text
        rating = phone.find('div', class_='_3LWZlK').text
        discount = phone.find('div', class_='_3Ay6Sb').span.text
        print(f"Model: {name}")
        print(f"Costs: {price}")
        print(f"User Rating: {rating}")
        print(f"Discount: {discount}")
        print(' ')
