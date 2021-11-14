from bs4 import BeautifulSoup
import requests
from subprocess import Popen

IGNORE_LIST=['../',]
URL="https://downloads.tuxfamily.org/godotengine/"

ALL_PROCESSES=[]

def get_best_link(add_dict, fname, url):
    page = requests.get(url) 
    data = page.text
    soup = BeautifulSoup(data, features='html.parser')
    links = map(lambda x: x.get('href'), soup.find_all('a'))
    best_link = ''
    folders = []
    for link in links:
        if 'headless' in link:
            best_link = link
        elif best_link == '' and ('x11.64' in link or 'x11_64' in link):
            best_link = link
        elif '/' in link and link not in IGNORE_LIST:
            folders.append([fname + '_' + link.strip('/'), url + '/' + link.strip('/') ])
    if best_link == '':
        print(fname, 'option not found')
    else:
        best_link = url + '/' + best_link
        zip_file_name = best_link.rsplit('/', 1)[-1]
        extracted_file_name = zip_file_name.rsplit('.', 1)[0]
        ALL_PROCESSES.append(Popen(["./download_single.sh", fname, best_link, zip_file_name, extracted_file_name]))
    for sfname, sfurl in folders:
        get_best_link(add_dict, sfname, sfurl)            

def main():
    page = requests.get(URL)
    data = page.text
    soup = BeautifulSoup(data, features='html.parser')

    top_level_versions = {}
    for link in soup.find_all('a'):
        lhref = link.get('href').strip('/')
        if len(lhref) < 1:
            continue
        if not lhref[0].isnumeric():
            continue
        top_level_versions[lhref] = { 'base_url': URL + lhref }

    for version in top_level_versions:
        vdict = top_level_versions[version]
        if version == '3.0':
            get_best_link(vdict, version, vdict['base_url'])
        
    for i in ALL_PROCESSES:
        i.wait()

main()
