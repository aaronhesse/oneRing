# oneRing
## _An API SDK/Client for Lord of the Rings API_

This is a python3 library sdk for interfacing with a publically available Lord
of The Rings API.

- Supports all the basic functionality of the original API.
- Supports some of the advanced features of the original API:
    - Supports limiting the query result count.
    - Supports querying characters not a particular name.
    - Supports querying characters by a particular name.


## Installation

oneRing requires [python3 requests](https://pypi.org/project/requests/) to run.

Install oneRing from PyPI.

```
pip install oneRing
```
# Usage

Instantiate the OneRing Client:

```
client = OneRing.Client(<your_api_key>)
```

Make a request using one of the many client methods:
```
client.getBook()
```
or
```
client.getBook('5cf5805fb53e011a64671582')
```

# List of Client methods:

- client.getBook()
- client.getBook(<book_id>)
- client.getChapter(<chapter_id>)
- client.getMovies()
- client.getMovie(<movie_id>)
- client.getCharacter()
- client.getCharacter(<character_id>)
- client.getCharacterQuote(<character_id>)
- client.getAllQuotes()
- client.getQuote(<quote_id>)
- client.getChapter()
- client.getChapter(<chapter_id>)
- client.getCharactersWithLimit(<int>)
- client.getMoviesWithLimit(<int>)
- client.getAllQuotesWithLimit(<int>)
- client.getCharactersNotNamed(<character_name>)
- client.getCharacterByName(<character_name>)

## License

MIT
