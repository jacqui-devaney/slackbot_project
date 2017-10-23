The WSJ top stories bot pulls the top five stories on the site at any given moment.

This bot is very simple to use, which will make it easy for WSJ editors to use at any given moment.
All one needs to do is type "top stories" into slack and the bot will automatically respond
with the top five stories and their respective links.

This bot was created by employing a python script that was built to scrape the data
from the WSJ homepage, where the trending stories are listed. Within the test.js file
(the file that runs the bot), I used a node.js package called python-shell that allows me
to trigger a python file to run inside of a .js file, that way the .json file with the
trending stories data is always updated when someone runs the slackbot and will deliver
the most up to date information.

There was a lot of trial and error creating this bot, included to creating a web scraper with text and links
, importing data into the .js file, running a python script in the .js file, iterating
over an array within an object, and manipulating the data in order to have it show up in a readable way
in Slack.

That being said, I really would've liked the data to show up line by line, for example:
1. first story
2. second story
However, it shows up more as a continuous string. Example:
1. first story, 2. second story 

I tried a few methods but had very little luck getting that line break in there. (normal HTML <br> don't work)
