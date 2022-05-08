import requests
import urllib.parse
import json

class Client(object):

    # internal and/or helper functions or variables:

    BASE_URL = "https://the-one-api.dev/v2/"
    g_apiKey = ""

    def __init__(self, apiKey):
        self.g_apiKey = apiKey

    def makeAuthenticatedRequest(self, path, options=None):
        self.makeRequest(path, True, options)

    def makeRequest(self, path, authenticate=False, options=None):

        print(path)

        # { param -> { operator : "!=<>", "value" : "100"}}

        if options:
            queryParams = ""
            for param in options:
                if param != 'sort':
                    queryParams += param + options[param]['operator'] + options[param]['value'] + "&"
                else:
                    queryParams += 'sort=' + options['sort']['criteria'] + ':' + options['sort']['order']
            queryParams = urllib.parse.quote(queryParams[:-1])
            path += '?' + queryParams

            print(path)

        if not authenticate:
            r = requests.get(self.BASE_URL + path)
        else:
            r = requests.get(self.BASE_URL + path, headers={'Authorization':"Bearer " + self.g_apiKey})

        # Handle http errors and return that response to the caller.

        print(r.status_code)
        print(r.headers['content-type'])
        print(r.encoding)
        print(json.dumps(r.json(), indent=4))
        print(path)


    # Book functions:

    def getAllBooks(self, options=None):
        self.makeRequest("book", False, options)

    def getBookById(self, book_id):
        self.getAllBooks({"_id": { "operator": "=", "value": book_id}})

    def getBookByName(self, book_name):
        self.getAllBooks({"name": { "operator": "=", "value": book_name}})



    # Chapter functions

    def getAllChapters(self, options=None):
        self.makeAuthenticatedRequest("chapter", options)

    def getAllChaptersOfBook(self, book_id):
        self.makeRequest("book/" + book_id + "/chapter")

    def getChapterById(self, chapter_id):
        self.getAllChapters({"_id": { "operator": "=", "value": chapter_id}})

    def getChapterByName(self, chapter_name):
        self.getAllChapters({"name": { "operator": "=", "value": chapter_name}})



    # Movie functions:

    def getAllMovies(self, options=None):
        self.makeAuthenticatedRequest("movie", options)

    def getMovieById(self, movie_id):
        self.getAllMovies({"_id": { "operator": "=", "value": movie_id}})

    def getMovieByName(self, movie_name):
        self.getAllMovies({"name": { "operator": "=", "value": movie_name}})



    # Character functions:

    def getAllCharacters(self, options=None):
        self.makeAuthenticatedRequest("character", options)

    def getCharacterQuotes(self, character_id):
        self.makeAuthenticatedRequest("character/" + character_id + "/quote")

    def getCharacterById(self, character_id):
        self.getAllCharacters({"_id": character_id})

    def getCharactersByName(self, character_name):
        self.getAllCharacters({"name": character_name})



    # Quote functions:

    def getAllQuotes(self, options=None):
        self.makeAuthenticatedRequest("quote", options)

    def getQuoteById(self, quote_id):
        self.getAllQuotes({"_id": {'operator': '=', 'value': quote_id}})