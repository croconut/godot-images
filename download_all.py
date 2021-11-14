from bs4 import BeautifulSoup
from sys import argv
from requests import get
from subprocess import run

IGNORE_LIST=['../',]
URL="https://downloads.tuxfamily.org/godotengine/"

ALL_PROCESSES=[]
RETURN_MODE='false'

def get_best_link(add_dict, fname, url, return_list):
    page = get(url) 
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
            folders.append([fname + '___' + link.strip('/'), url + '/' + link.strip('/') ])
    if best_link != '':
        p = run(["./check_docker.sh", fname, argv[1]])
        if p.returncode == 0:
            return_list.append(fname)
    for sfname, sfurl in folders:
        get_best_link(add_dict, sfname, sfurl, return_list)            

def main():
    return_list = []
    page = get(URL)
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
        if version < '3.0':
            get_best_link(vdict, version, vdict['base_url'], return_list)
        
    print(return_list)        

main()
