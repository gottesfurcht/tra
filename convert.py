#!/usr/bin/env python3

import re

books = {
    40: 'Matthew',
    41: 'Mark',
    42: 'Luke',
    43: 'John',
    44: 'Acts',
    45: 'Romans',
    46: '1 Corinthians',
    47: '2 Corinthians',
    48: 'Galatians',
    49: 'Ephesians',
    50: 'Philippians',
    51: 'Colossians',
    52: '1 Thessalonians',
    53: '2 Thessalonians',
    54: '1 Timothy',
    55: '2 Timothy',
    56: 'Titus',
    57: 'Philemon',
    58: 'Hebrews',
    59: 'James',
    60: '1 Peter',
    61: '2 Peter',
    62: '1 John',
    63: '2 John',
    64: '3 John',
    65: 'Jude',
    66: 'Revelation'
}

import sqlite3
conn = sqlite3.connect('tra.bbl.mybible')
c = conn.cursor()

with open('tra.imp', 'w') as tra:
    for row in c.execute('SELECT * FROM Bible'):
        book = books[row[0]]
        chapter = row[1]
        verse = row[2]
        text = row[3]
        tra.write("$$$%s %s:%s\n%s\n" % (book, chapter, verse, re.sub('<[^<]+?>', '', text)))



