import discord
import io
import random

def get_random_message():
    f = open('randomlines.txt', 'r')
    lines = []
    for line in f:
        lines.append(line)
    rand_num = random.randint(0, len(lines)-1)
    return lines[rand_num]
    

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    
    async def on_message(self, message):
        if self.user in message.mentions:
            msg = get_random_message()
            await message.channel.send(msg)

client = MyClient()
client.run('bottoken')