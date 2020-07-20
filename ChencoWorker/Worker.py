#! /usr/bin/env python3
# coding: utf-8

import json
import discord
import random

from .WorkerConfigLoader import WorkerConfigLoader


class ChencoWorker(discord.Client):
    async def on_ready(self):
        print('Logged on {0} as {1}!'.format(self.guilds[0].name, self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        print('Message from {0.author}: {0.content}'.format(message))

        responseValue = ['Comrade {0} !'.format(
            message.author), 'Praise our great leaders !']

        if 'COMRADE' in message.content.upper():
            response = random.choice(responseValue)

            await message.channel.send(response)

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send('Hi comrade {0}, welcome to our Discord server!'.format(member.name))


if __name__ == "__main__":
    config = WorkerConfigLoader("config.json")

    client = ChencoWorker()
    client.run(config.token)
