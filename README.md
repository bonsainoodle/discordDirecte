# discordDirecte
a discord bot that retrieves your [Ecole directe](https://ecoledirecte.com) homeworks and sends them in a discord channel of your choice

## create the discord bot
follow this [tutorial](https://discordpy.readthedocs.io/en/stable/discord.html) to create your discord bot.

you must invite the bot on the discord server you want it to send the homeworks!

## installation
```bash
git clone https://github.com/EsprIx/discordDirecte
```
under the ```discordDirecte``` directory, you need to create a ```config.json``` file.

it should look like this:
```json
{
    "botToken": "TOKEN",
    "botStatus": "STATUS",
    "loopDelay": 10,
    "channelId": 000000000000000000,
    "ecLogin": "LOGIN",
    "ecPassword": "PASSWORD"
}
```
| Key | Description | Default |
|---|---|---|
| botToken | secret token of your discord bot | None |
| botStatus | discord status of your bot | None |
| looDelay | delay in seconds between each message of the bot (everytime the bot run through the loop, it sends the homeworks for tomorrow) | 86400 (= 24 hours) |
| channelId | discord id of the channel you want the bot to send the homeworks to | None |
| ecLogin | your [Ecole directe](https://ecoledirecte.com) login |
| ecPassword | your [Ecole directe](https://ecoledirecte.com) password |

## run the bot
execute the ```start.py``` file at the root of ```discordDirecte``` directory.
```bash
python start.py
```

## license
[MIT](https://choosealicense.com/licenses/mit/)