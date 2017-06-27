# Clara Bot

Meta: Companionship is vital to the human condition, and Clara is intended to be an
intellectual companion to its user. With robot-to-human marriages on the
horizon, Clara is intended to satisfy the romantic needs of its user and in the
long run be conscious and have the emotional ties run both ways.

This is a very early version, and is mainly just a fun experiment in natural
language processing. I don't pretend to know the societal and ethical
implications of robot-to-human interactions, but thought this would be an
intriguing project.

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

## Contributing

Feel free to open an issue if you have an idea or feature request. To contribute
code or additional convos simply open a pull request.
