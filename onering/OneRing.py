import requests

class Client(object):

    # internal and/or helper functions or variables:

    BASE_URL = "https://the-one-api.dev/v2/"
    g_apiKey = ""

    def __init__(self, apiKey):
        self.g_apiKey = apiKey

    def makeAuthorizedRequest(self, path):
        self.makeRequest(path, True)

    def makeRequest(self, path, authorized=False):
        print(path)
        if not authorized:
            r = requests.get(self.BASE_URL + path)
        else:
            r = requests.get(self.BASE_URL + path, headers={'Authorization':"Bearer " + self.g_apiKey})

        print(r.status_code)
        print(r.headers['content-type'])
        print(r.encoding)
        print(r.text)
        print(r.json())


    # Book and Chapter functions:

    def getBook(self, id=None):
        if id:
            self.makeRequest("book/" + id)
        else:
            self.makeRequest("book/")

    def getChapter(self, id):
        self.makeRequest("book/" + id + "/chapter")

    def getChapter(self, id=None):
        if id:
            self.makeAuthorizedRequest("chapter/" + id)
        else:
            self.makeAuthorizedRequest("chapter")


    # Movie functions:

    def getMoviesWithLimit(self, limit):
        self.makeAuthorizedRequest("movie?limit=" + str(limit))

    def getMovies(self):
        self.makeAuthorizedRequest("movie")

    def getMovie(self, id):
        self.makeAuthorizedRequest("movie/" + id)


    # Character functions:

    def getCharactersWithLimit(self, limit):
        self.makeAuthorizedRequest("character?limit=" + str(limit))

    def getCharacter(self, id=None):
        if id:
            self.makeAuthorizedRequest("character/" + id)
        else:
            self.makeAuthorizedRequest("character")

    def getCharacterByName(self, name):
        self.makeAuthorizedRequest("character?name=" + name)

    def getCharactersNotNamed(self, name):
        self.makeAuthorizedRequest("character?name!=" + name)

    def getCharacterQuote(self, id):
        self.makeAuthorizedRequest("character/" + id + "/quote")


    # Quote functions:

    def getAllQuotesWithLimit(self, limit):
        self.makeAuthorizedRequest("quote?limit=" + str(limit))

    def getAllQuotes(self):
        self.makeAuthorizedRequest("quote")

    def getQuote(self, id):
        self.makeAuthorizedRequest("quote/" + id)