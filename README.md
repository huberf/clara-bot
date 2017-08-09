# Clara Bot

Conversational UI? Digital companion? The clara system can act as a stand alone chitchat framework or can easily be used to augment an existing chatbot by handling general small talk or non-command based queries. Clara uses JSON conversation files containing possible inputs and corresponding responses to match the best response to the user's query using the [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) so even if they make a typo or type a query not included, it will still deliver a proper response. The system also has a dynamic emotional state which can affect the responses the system gives if made use of.

This is an early version, and has only recently graduated from being a fun experiment. However, it has worked very well in my systems and tests, and could prove to be immensenly useful to chatbot developers or those trying to build their own artificial companion.

## Setup

1. Run `git clone https://github.com/huberf/clara-bot`
2. Now `cd` into the `clara-bot` directory.
3. Try running `python3 brain.py`. If you get requirement errors, `pip3` them
   into your instance.
4. If the command didn't return an error, try typing `Hello!` into the input box
   that should be present on the command line.
5. All messages and accompanying responses are located in the `convos/`
   directory. You can easily add conversation scripts others made by simply
   copying them into this directory. On startup, the program will load all data
   from any JSON file in that directory.
6. Feel free to add new responses or entire new conversation sets.

## Mobile App and Web API

Clara has a Flask webserver setup in the `web.py` file, and can be immediately
deployed to Heroku.

### Heroku Setup
1. Enter the clara-bot directory.
2. Run `heroku create`
3. Type `git push heroku master`
4. Profit!

You can also setup the server locally by running `python3 web.py`.

Currently, I've built a fully functional React Native clara client that has only
been tested on iOS. It can connect to any Clara instance, and currently doesn't
save your messages. On launch, one simply enters the URL of any Clara instance,
and it will properly work with it.
Link to checkout [the Clara Mobile
client](https://github.com/huberf/clara-mobile)

## Convo File Formats
All json files from the `convos/` directory are automatically loaded at startup.
Therefore, you break your convo files into an infinite number of individual
convo files. All such files contain an array of objects with the following keys:
* `starters` - This is an array of possible things a user could say to initiate
  the responses mentioned directly below this.
* `replies` - This is an array of possible replies which are selected at random
  based upon the `weight` key for each reply value. Replies can also be reserved
  for only certain states such as a happiness level greater than 0. To use this
  functionality one need only include the `qualifiers` key which is an array of
  objects with the keys `name` and then either `{"$lt": 0}`, `{"$gt": 0}`, or
  `{"$eq": 0}` except with 0 being whatever value you wish the response to
  activate at against the less than, greater than, or equal to operators.
Here is an example JSON response file:
```
[
  {
    "starters": ["this is a test", "i am testing you"],
    "replies": [
      {"text": "Hello very happy world!", "weight": 1, "modifiers": 
        [
          {"name": "happy_level", "$gt": 2}
        ]
      },
      {"text": "Hello world!", "weight": 1, "modifiers": 
        [
          {"name": "happy_level", "$eq": 2},
          {"name": "happy_level", "$lt": 2}
        ]
      }
    ]
  }
]
```
A new simplified format in development is signified with the `.convo` suffix. It
uses newlines combined with a letter, colon and space to divide up the data.
Ex:
```
Q: Who are you?; What are you?; Tell me what you are.
R: I am an artificial intelligence bot.
Q: I enjoy programming.
R: Wow! I do too!; Programming is the best thing in the world.
```
It is much easier to add to than the JSON, but with a much more limited feature
set and doesn't include the ability to add conditional responses requiring
certain moods or modifying data inside the "brain".
Therefore, this convo format is meant for quickly adding new conversation info
that isn't expected to be commonly used. It is also planned to be used in future
machine learning response generation, where Clara could consume and process the
data from such a file and then generate brand new responses with what the system
learned. Therefore, in the future, the interpreter will support including chunks
of conversation that has a flow. For example:
```
X:
Q: Hello?
R: Hi! What are you up to?
Q: I am working on a coding project.
R: That is very neat. What language are you using?
Q: I am using JavaScript.
R: Very neat!
Q: I have to go now. Bye!
\X:
```
As this is still in development, the format will continue to update and morph,
and the JSON is still planned to be the main format for scripted responses.

## Contributing

Feel free to open an issue if you have an idea or feature request. To contribute
code or additional convos simply open a pull request.
