import random

messages = ["It is certain",
            "It is decidedly so",
            "Yes definitely",
            "Reply hazy try again",
            "Ask again later",
            "Concentrate and ask again",
            "My reply is no",
            "Outlook not so good",
            "Very doubtful"]

# random index bt 0 and list length - 1
print(messages[random.randint(0, len(messages) - 1)])
