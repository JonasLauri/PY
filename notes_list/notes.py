#! /usr/bin/env python3
# Make list of notes

notes_list = []

def show_help():
    print('''This program will add your grocery notes to the list\n
    Enter 'stop' to stop adding notes.
    Enter 'help' calling for help.
    Enter 'show' for your list lookup.
    ''')

def add_item(items):
    notes_list.append(items)
    '''units = items.split()
    for unit in units:
        notes_list.append(unit)'''
    count = len(notes_list)
    print(f"Added! Your total items count: {count}")

def show_list():
    print("Your item list: ")
    for item in notes_list:
        print("* " + item)

show_help()
while True:
    list_note = input("> ")
    
    if list_note == 'stop':
        break
    elif list_note == 'help':
        show_help()
        continue
    elif list_note == 'show':
        show_list()
        continue
 
    add_item(list_note)

show_list()
    
        
