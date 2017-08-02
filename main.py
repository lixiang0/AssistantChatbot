import sys
import chatbot

cbot=chatbot.chatbot()
for line in sys.stdin:
    print(cbot.reply(line))

