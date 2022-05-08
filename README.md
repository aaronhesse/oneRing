# oneRing
## _An API SDK/Client for Lord of the Rings API_

This is a python3 library sdk for interfacing with a publically available Lord of The Rings API.

- Supports almost all of the original features of the API.
- The only unsupported feature is: **exists, doesn't exists**

## Installation

oneRing requires [python3 requests](https://pypi.org/project/requests/) to run.

Install oneRing from PyPI.

```
pip install oneRing
```

# Usage

Instantiate the OneRing Client:

- Instantiating the OneRing Client requires an API key from https://the-one-api.dev/. Create an account there to grab your API key, and pass it as an argument to the Client constructor like below:

```
client = OneRing.Client(<your_api_key>)
```

Make a request using one of the many client methods:
```
client.getBook()
```
or
```
client.getBookById('5cf5805fb53e011a64671582')
```

# List of Client methods with examples:

- client.getAllCharacters()
- client.getCharacterById('5cdbe3667ed9587226e7949e')
- client.getCharactersByName('Figwit')
- client.getCharacterQuotes('5cdbe3667ed9587226e7949e')
- client.getAllQuotes()
- client.getQuoteById('5cd96e05de30eff6ebccebca')
- client.getAllChapters()
- client.getChapterById('6091b6d6d58360f988133bc6')
- client.getChapterByName("Homeward Bound")
- client.getAllChaptersOfBook('5cf58080b53e011a64671584')
- client.getAllBooks()
- client.getBookById('5cf5805fb53e011a64671582')
- client.getBookByName('The Fellowship Of The Ring')

## License

MIT
