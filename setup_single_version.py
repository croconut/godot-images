from bs4 import BeautifulSoup
from sys import argv
from requests import get
from subprocess import call

IGNORE_LIST=['../',]
URL="https://downloads.tuxfamily.org/godotengine/"

ALL_PROCESSES=[]
RETURN_MODE='false'

def get_best_link(url):
    page = get(url) 
    data = page.text
    soup = BeautifulSoup(data, features='html.parser')
    links = map(lambda x: x.get('href'), soup.find_all('a'))
    best_link = ''
    for link in links:
        if 'headless' in link:
            best_link = link
        elif best_link == '' and ('x11.64' in link or 'x11_64' in link):
            best_link = link
    if best_link != '':
        best_link = url + '/' + best_link
        zip_file_name = best_link.rsplit('/', 1)[-1]
        extracted_file_name = zip_file_name.rsplit('.', 1)[0]
        call(["./download_single.sh", 'godot', best_link, zip_file_name, extracted_file_name])       

def main():
    if len(argv) > 1:
        version = argv[0]
    else:
        exit(1)
    version = version.replace('___', '/')
    url = URL + version
    get_best_link(url)

main()
