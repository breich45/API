#!/usr/bin/python3
import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"
AOIF_HOUSES = "https://www.anapioficeandfire.com/api/houses/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()

        ## lookup and get book info
        books = []
        for book in got_dj["books"]:
             gotresp2 = requests.get(book)
             got_books = gotresp2.json()["name"]
             books.append(got_books)


        ## lookup and get house info
        allies = []
        for ally in got_dj["allegiances"]:
             gotresp3 = requests.get(ally)
             got_ally = gotresp3.json()["name"]
             allies.append(got_ally)




        char_name = (got_dj["name"])
        print(f'''
        name: {char_name}
        books: {books}
        allegieances: {allies}
        ''')

if __name__ == "__main__":
        main()
