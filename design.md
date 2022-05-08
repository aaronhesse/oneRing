# Design of OneRing

OneRing is designed to provide an abstraction of the Lord of the Rings API at
https://the-one-api.dev/, in the form of a python3 library.

# Provides basic common API calls

There are some common and basic API calls that are provided as SDK methods
that do not require a dictionary payload to use. Note: some of these can
accept an optional dictionary payload as mentioned in the next section.
Also some of these do take arguments, such as a string for the name, or
an integer for an id.

- getAllBooks()
- getBookById()
- getBookByName()
- getAllChapters()
- getAllChaptersOfBook()
- getChapterById()
- getChapterByName()
- getAllMovies()
- getMovieById()
- getMovieByName()
- getAllCharacters()
- getCharacterQuotes()
- getCharacterById()
- getCharactersByName()
- getAllQuotes()
- getQuoteById()

# Supporting the original advanced API features

Most of the SDK methods will accept a dictionary object that contains query
criteria that will be passed to the original underlying API. This querying
pattern supports any combination of originally supported criteria. It can
be very simple or very complex.

The list of advanced features can be found on the original API documentation
page at: https://the-one-api.dev/documentation



Simple:

characterQuery = { 'race': { 'operator': '=', 'value': 'Hobbit,Human' } }

jsonData = client.getAllCharacters(characterQuery)



Complex:

characterQuery = { 'race': { 'operator': '=', 'value': 'Hobbit,Human' },
                   'gender': {'operator': '=', 'value': 'Male' },
                   'limit' : {'operator': '=', 'value': '3'},
                   'sort': { 'criteria': 'name', 'order': 'desc'} }

jsonData = client.getAllCharacters(characterQuery)