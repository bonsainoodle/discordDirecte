import repackage

repackage.up()

import discord
import time
from discord.ext import tasks
import datetime
import json

import libs.homeworks


with open("config.json", "r") as f:
    secrets = json.load(f)

assert "botToken" in secrets
assert "channelId" in secrets

client = discord.Client()

CHANNEL_ID = secrets["channelId"]
LOOP_DELAY = 86400
NOTIF_ROLE_ID = None

if "loopDelay" in secrets:
    try:
        LOOP_DELAY = int(secrets["loopDelay"])
    except Exception:
        LOOP_DELAY = 86400

if "notifRoleId" in secrets:
    try:
        NOTIF_ROLE_ID = f'<@&{int(secrets["notifRoleId"])}>'
    except Exception:
        NOTIF_ROLE_ID = None


def getChannel():
    CHANNEL = None
    for guild in client.guilds:
        CHANNEL = guild.get_channel(CHANNEL_ID)

    if CHANNEL == None:
        print(f"No channel found for id={CHANNEL_ID}")
        return

    print(f"Channel found for id={CHANNEL_ID}")

    return CHANNEL


@client.event
async def on_ready():
    print("------")
    print("DiscordBot: Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")

    if secrets["botStatus"]:
        await client.change_presence(activity=discord.Game(name=secrets["botStatus"]))


@tasks.loop(seconds=LOOP_DELAY)
async def sendHomeworks():
    time.sleep(10)
    CHANNEL = getChannel()

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

    if homeworks["subjects"]:
        embed = discord.Embed(
            title=(f"Devoir pour le {date.day} {months[date.month - 1]} {date.year}  📋"),
            description=f"{'||<@&{NOTIF_ROLE_ID}>||' if NOTIF_ROLE_ID else ''}\nMessage automatique qui récupère UNIQUEMENT les devoirs sur école directe.",
            url="https://ecoledirecte.com",
            color=discord.Color.purple(),
        )

        for subject in homeworks["subjects"]:
            teacher = homeworks["subjects"][subject]["teacher"]
            interrogation = homeworks["subjects"][subject]["interrogation"]
            documents = homeworks["subjects"][subject]["documents"]
            documentsJoined = ", ".join(documents)

            if interrogation == "True":
                interrogation = "Oui"
            else:
                interrogation = "Non"

            if documents:
                embed.add_field(
                    name=f"**{subject} ({teacher})**",
                    value=(
                        homeworks["subjects"][subject]["content"]
                        + f"\n__Interrogation__: {interrogation}"
                        + f"\n__Il y a {len(documents)} document(s) disponible(s)__: {documentsJoined}"
                    ),
                    inline=False,
                )
            else:
                embed.add_field(
                    name=f"**{subject} ({teacher})**",
                    value=(homeworks["subjects"][subject]["content"] + f"\n__Interrogation__: {interrogation}"),
                    inline=False,
                )
    else:
        embed = discord.Embed(
            title=(f"Il n'y a pas de devoirs pour le {date.day} {months[date.month - 1]} {date.year}  🎉"),
            description=f"{'||<@&{NOTIF_ROLE_ID}>||' if NOTIF_ROLE_ID else ''}\nMessage automatique qui récupère UNIQUEMENT les devoirs sur école directe.",
            color=discord.Color.purple(),
        )

    embed.set_footer(text="Made with 💜 by Bonsaï#8521")

    await CHANNEL.send(embed=embed)
    print("Message sent!")


sendHomeworks.start()
client.run(secrets["botToken"])
