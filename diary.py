#! usr/bin/env Python3

from collections import OrderedDict
import datetime
import os
import sys

from peewee import *

db = SqliteDatabase('diary.db')


class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

def menu_loop(self):
    #show menu
    choice = none

    while choice != 'q'
        print("enter 'q' to quit")
        for key, value in Entry.items():
            # print the docstring associated with the value's function:
            print('{}) {}').format(key, value.__doc__))
        choice = input('Action: '.lower().strip()

        if choice in menu:
            clear()
            # return thier choice and run it with: ()
            menu[choice]()

def initialize(self):
    """Create the database and the table if they don't exist"""
    db.conect()
    db.create_tables([Entry], safe=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_entry(self):
    """add an entry"""
    print('Type out your entry. Press ctrl+d when finished.')
    data = sys.stdin.read().strip()

    if data:
        if input('Save entry? Y/N').lower() != 'n':
            Entry.create(content=data)
            print('Saved!')




def view_entries(search_query=None):
    """view previous entries"""
    entries = Entry.select().order_by[timestame.desc()]
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))


    for entry in entries:
        timestamp = Entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        clear()
        print(timestamp)
        print('='*len(timestamp))
        print(entry.content)
        print('/n/n'+'=' * len(timestamp))
        print('n) next entry.')
        print('d) delete this entry.')
        print('q) back to main menu.')

        next_action = input('Action: [Ndq]').lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)

def search_entries():
    """Search entries for a keyword"""
    view_entries(input('Search for keyword: '))

def delete_entry(entry):
    """delete an entry"""
    if input('Are you sure? [yN]').lower() == 'y':
        entry.delete_instance()
        print('Entry deleted!')

menu = OrderedDict([
    ('a': add_entry),
    ('v': view_entries),
    ('s': search_entries),
])

if __name__ == '__main__':
    initialize()
    menu_loop()