# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 01:32:59 2025

@author: arpit
"""

# my_list = [[1,2,3],[4,5,6],[7,8,9]]

# my_list[0]
# my_list[1]
# my_list[2]

# my_list[1][1]


countries = {'France':{'Capital':'Paris','Language':'French'},'Spain':{'Capital':'Madrid','Language':'Spanish'},
            'United Kingdom':{'Capital':'London','Language':'English'},
           'United States':{'Capital':'Washington DC','Language':'English'},
           'Italy':{'Capital':'Rome','Language':'Italian'}
           }

countries['France']

for key,value in countries.items():
    print(key,value)
    
print()

for key,value in countries.items():
    print(f'{value["Capital"]} is the capital of {key}, they speak {value["Language"]}.')
    
    
##############################################################

#  The provided data
library = {
    "Fiction": [
        {"title": "1984", "author": "George Orwell"},
        {"title": "Brave New World", "author": "Aldous Huxley"}
    ],
    "Science": [
        {"title": "A Brief History of Time", "author": "Stephen Hawking"},
        {"title": "The Selfish Gene", "author": "Richard Dawkins"}
    ],
    "History": [
        {"title": "Sapiens", "author": "Yuval Noah Harari"},
        {"title": "Guns, Germs, and Steel", "author": "Jared Diamond"}
    ]
}

# Step 1: Access and print the title of the first Fiction book
print("First Fiction book title:", library["Fiction"][0]["title"])

# Step 2: Access and print the author of the second Science book
print("Second Science book author:", library["Science"][1]["author"])

# Step 3: Print each History book's title and author in a formatted sentence
for book in library["History"]:
    print(f"In the History category, we have {book['title']} by {book['author']}")