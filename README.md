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
    "loopDelay": 86400,
    "channelId": 123456789101112,
    "ecLogin": "LOGIN",
    "ecPassword": "PASSWORD"
}
```
| Key | Description | Default | Required |
|---|---|---|---|
| botToken | secret token of your discord bot | None | True |
| botStatus | discord status of your bot | None | False |
| loopDelay | delay in seconds between each message of the bot (everytime the bot runs through the loop, it sends the homeworks for tomorrow) | 86400 (= 24 hours) | False |
| channelId | discord id of the channel you want the bot to send the homeworks to | None | True |
| notifRoleId | discord id of the role you want the bot to ping when it sends a message | None | False |
| ecLogin | your [Ecole directe](https://ecoledirecte.com) login | None | True |
| ecPassword | your [Ecole directe](https://ecoledirecte.com) password | None | True |

## run the bot
execute the ```start.py``` file at the root of ```discordDirecte``` directory.
```bash
python start.py
```

## license
[MIT](https://choosealicense.com/licenses/mit/)
