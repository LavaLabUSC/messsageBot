# messsageBot
Slackbot for broadcast messaging custom content based on user

This is a **work in progress** and employs lots of inefficient methods. Specifically, there's a loop through the object that should only happen once, if at all, but I do it per user. Doesn't really matter since the whole run took about 10 seconds per 100 users :)

##Input
messageBot takes a JSON of email & message objects and broadcasts them as DMs.
```
[
 {
   "email": "email@gmail.com",
   "message": "We have a shirt size of *M* on record for you. We're ordering shirts soon! If this is correct, *do nothing*. If it is wrong, reach out to @shirtadmin ASAP :)"
 }
]
```

##Example
<img width="616" alt="messagebot" src="https://cloud.githubusercontent.com/assets/7699842/22322041/11827898-e34e-11e6-8097-0fe09624a508.png">

##Required Files
```botId.py``` needs to have a simple class like the following:
```
class bot:
	id = "XXXXXXX"
	token = "xoxb-85858585858585-33939932908d09g8094mt3dfskjewfa"
```

##Run
Run ```python3 messageBot.py``` to loop through all of the messages and send instantly.
