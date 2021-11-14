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
        if 'headless' in link and '64' in link:
            best_link = link
    if best_link != '':
        best_link = url + '/' + best_link
        zip_file_name = best_link.rsplit('/', 1)[-1]
        extracted_file_name = zip_file_name.rsplit('.', 1)[0]
        call(["./download_single.sh", 'godot', best_link, zip_file_name, extracted_file_name])
    else:
        print('headless download link not found!')
        exit(1)    

def main():
    if len(argv) > 1:
        version = argv[1]
    else:
        exit(1)
    version = version.replace('_', '/')
    url = URL + version
    get_best_link(url)

main()
