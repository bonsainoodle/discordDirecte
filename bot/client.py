import repackage

repackage.up()

import discord
from discord.ext import tasks
import datetime
import json

import secrets
import libs.homeworks


with open("config.json", "r") as f:
    secrets = json.load(f)

assert "botToken" in secrets
assert "channelId" in secrets
assert "loopDelay" in secrets
assert "botStatus" in secrets

client = discord.Client()

CHANNEL_ID = secrets["channelId"]


@client.event
async def on_ready():
    print("------")
    print("DiscordBot: Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")

    await client.change_presence(activity=discord.Game(name=secrets["botStatus"]))


@tasks.loop(seconds=secrets["loopDelay"])
async def sendHomeworks():
    CHANNEL = None
    for guild in client.guilds:
        CHANNEL = guild.get_channel(CHANNEL_ID)

    if CHANNEL == None:
        print(f"No channel found for id={CHANNEL_ID}")
        return

    print(f"Channel found for id={CHANNEL_ID}")

    homeworks = libs.homeworks.getHomeworks()

    date = datetime.datetime.strptime(homeworks["date"], "%Y-%m-%d")

    months = [
        "janvier",
        "février",
        "mars",
        "avril",
        "mai",
        "juin",
        "juillet",
        "août",
        "septembre",
        "octobre",
        "novembre",
        "décembre",
    ]

    embed = discord.Embed(
        title=(f"Devoir pour le {date.day} {months[date.month - 1]} {date.year}"),
        description="Message automatique qui ne récupère UNIQUEMENT les devoirs sur école directe.",
        color=discord.Color.purple(),
    )

    for subject in homeworks["subjects"]:
        interrogation = homeworks["subjects"][subject]["interrogation"]

        if interrogation == "True":
            interrogation = "Oui"
        else:
            interrogation = "Non"

        embed.add_field(
            name=f"**{subject}**",
            value=(homeworks["subjects"][subject]["content"] + f"\n__Interrogation__: {interrogation}"),
            inline=False,
        )

    embed.set_footer(text="Made with 💜 by Bonsaï#8521")

    await CHANNEL.send(embed=embed)
    print("Message sent!")


sendHomeworks.start()
client.run(secrets["botToken"])
