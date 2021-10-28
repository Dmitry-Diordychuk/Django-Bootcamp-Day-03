#!/usr/bin/python3
# coding: utf-8
import sys
import requests
from bs4 import BeautifulSoup


def run():
    if len(sys.argv) != 2:
        raise Exception("Program take one argument!")

    result_path = []
    page_title = sys.argv[1].replace(' ', '_')
    while True:
        result_path.append(page_title.replace('_', ' '))
        if result_path[-1] == 'Philosophy':
            break
        elif result_path[-1] in result_path[0:-1]:
            raise Exception("It leads to an infinite loop !")
        page_title = page_title
        req = requests.get(
            "https://en.wikipedia.org/wiki/{0}".format(page_title)
        )

        if req.status_code == 404:
            raise Exception("Page {0} doesn't exist".format(page_title))
        elif req.status_code != 200:
            raise Exception("Wiki server error")

        soup = BeautifulSoup(req.text, 'html.parser')
        content_text = soup.html.body.find(class_="mw-parser-output")
        p_tags = content_text.find_all(
            lambda tag: tag.name == 'p' and not tag.attrs,
            recursive=False
        )

        first_a_tag = None
        for p in p_tags:
            first_a_tag = p.find('a', recursive=False)
            if first_a_tag != None:
                if len(first_a_tag["href"].split('/')) != 3:
                    continue
                if first_a_tag["href"].split('/')[1] != 'wiki':
                    continue
                break
        if first_a_tag == None:
            raise Exception("It leads to a dead end !")

        page_title = first_a_tag["href"].split('/')[2]

    print(*result_path, sep='\n')
    print("{0} roads from {1} to philosophy".format(
        len(result_path),
        result_path[0]
    ))


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        print(ex)
