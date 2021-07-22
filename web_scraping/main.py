#from an alredy present html file
from bs4 import BeautifulSoup

with open ('home.html', 'r') as html_file:
    content=html_file.read()
    
    soup= BeautifulSoup(content,'lxml')
    course_html_tags=soup.findAll('h1')

    for course in course_html_tags:
        print(course.text)
    