#!/usr/bin/env python
# -*- coding: utf-8 -*-

import elasticsearch
import pprint

pp = pprint.PrettyPrinter(indent=4)

posts = [{
        'author': 'Santa Clause',
        'blog': 'Slave based shippers of the north',
        'title': 'using celery for distributing gift dispatch',
        'topics': [
            'slave labor', 'elves', 'python', 'celery', 'antigravity reindeer'
        ],
        'awesomeness': 0.2
    }, {
        'author': 'Benjamin Pollack',
        'blog': 'bitquabit',
        'title': 'Having Fun: Python and Elasticsearch',
        'topics': ['elasticsearch', 'python', 'parseltongue'],
        'awesomeness': 0.7
    }, {
        'author': 'Benjamin Pollack',
        'blog': 'bitquabit',
        'title': 'How to Write Clickbait Titles About Git Being \
Awful Compared to Mercurial',
        'topics': ['mercurial', 'git', 'flamewars', 'hidden messages'],
        'awesomeness': 0.95
    }]


def main():
    es = elasticsearch.Elasticsearch()
    # push and index some posts
    for i, post in enumerate(posts):
        es.index(index='posts', doc_type='blog', id=i, body=post)
        # get some posts by id
        print "Inserting document ", i
        pp.pprint(es.get(index='posts', doc_type='blog', id=i))

    # search documents based on a query
    print "Searching for all documents where Benjamin Pollack is an author..."
    pp.pprint(es.search(index='posts', q='author:"Benjamin Pollack"'))

    # search 'Santa' across all fields
    print "Searching for all documents where Santa appears in any field..."
    pp.pprint(es.search(index='posts', q='Santa'))

    # search across all fields, mix and match queries
    print "Searching for all documents where Benjamin Pollack is an author and python appears..."
    pp.pprint(es.search(index='posts', q='author:"Benjamin Pollack" python'))


if __name__ == '__main__':
    main()

