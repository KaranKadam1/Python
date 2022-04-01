# a chatbot is an application that interacts with users like human.chatbots are typically used to resolve
# the most common quries that a bussiness recieves from its coustomers daily.
# what is chatbot?==>chatbot is an ai aplication that mimics human conversations.it is widely used by
# companies to solve most common problem they recieve from coustomers daily.
# eg.,if we want to know the CRN of our bank account,a chatbot will assist us by asking for our bank
# details,then it will give us crn(cource reference number=is unique 5dig identifier assign to class for reg perpose).
# But if you want to know something that is not that common, like asking
# how you can turn your account into a joint account, chances are the authorized employee will assist you.
# So while creating a chatbot for any company we should know what that company deals in and what problems
#their customers get daily. 

# NLTK= one of the best python library in python for any task of natural langauge processing.
# Natural language processing is a subfield of linguistics, computer science, and artificial intelligence
#concerned with the interactions between computers and human language, in particular how to program
#computers to process and analyze large amounts of natural language data

from nltk.chat.util import Chat,reflections

# Pair is a list of patterns and responses=
'''r = string will be treated as a raw string'''

pairs = [
    [
       r"(.*)my name is (.*)",
       ["Hello %2, How are you today ?",]
    ],

    [
        r"(.*)help (.*)",
        ["I can help you",]
    ],

    [
        r"(.*)your name?(.*)",
        ["My name is kk,but you can just call me robot and I'm a chatbot.",]
    ],

    [
        r"How are you (.*) ?",
        ["I am doing very well","I am great !"]
    ],

    [
        r"sorry(.*)",
        ["Its alright","Its OK,never mind that",]
    ],

    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright,great !",]
    ],

    [
        r"(hi|hey|hello|holla)(.*)",
        ["Hello","Hey there",]
    ],

    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],

    [
        r"(.*)created(.*)",
        ["Karan Kadam created me using Python's NLTK library","top secret :)",]
    ],

    [
        r"(.*) (location|city) ?",
        ['Dapoli,India',]
    ],

    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],

    [
        r"how (.*) health (.*)",
        ["Health is vey important , but i am a computer,so i don't need worry about my health",]
    ],

    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of cricket",]
    ],

    [
        r"who (.*) (Cricketer|Batsman)?(.*)",
        ["MS Dhoni"]
    ],

    [
        r"quit",
        ["bye for now.See you soon :)","It was nice talking to you.See you soon :)"]
    ],

    [
        r"(.*)",
        ['That is nice to hear']
    ],
]


# default message at the start of chat
print('''\nHi,I'm chatbot and i like to chat\nPlease type lowercase English langauge
to start a conversation.Type quit to leave...\n''')

# Creating chatbot
chat  = Chat(pairs,reflections)

#Start conversation
chat.converse()