#!/usr/bin/python3
# coding: utf-8
import requests
import json
from dewiki.parser import Parser
import sys


def run():
    if len(sys.argv) != 2:
        raise Exception("Need one argument!")

    try:
        #https://www.mediawiki.org/wiki/API:Search
        response_json = requests.get(
            'https://en.wikipedia.org/w/api.php',
            {
                'action': 'query',
                'format': 'json',
                'list': 'search',
                'srsearch': sys.argv[1]
            }
        ).json()
        totalhits = response_json["query"]["searchinfo"]["totalhits"]
        if totalhits == 0:
            raise Exception("Can't find any mathing result")
        page_title = response_json["query"]["search"][0]["title"]

        #https://www.mediawiki.org/wiki/API:Get_the_contents_of_a_page
        response_json = requests.get(
            "https://en.wikipedia.org/w/api.php",
            {
                'action': 'query',
                'format': 'json',
                'prop': 'revisions',
                'titles': page_title,
                'formatversion': 2,
                'rvprop': 'content',
                'rvslots': '*'
            }
        ).json()

        wiki_page = response_json \
                ["query"] \
                ["pages"][0] \
                ["revisions"][0] \
                ["slots"] \
                ["main"] \
                ["content"]

        filename = sys.argv[1].replace(' ', '_')
        with open(filename + ".wiki", 'w+') as file:
            file.write(Parser().parse_string(wiki_page))
    except Exception as ex:
        raise ex


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        print("Error:", ex)
