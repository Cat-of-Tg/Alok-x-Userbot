import glob
import os
import sys
from sys import argv
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from Lucifer import LOGS, bot, luciferver
from Lucifer.LuciferConfig import Var
from Lucifer.utils import load_module,start_mybot, load_pmbot
from pathlib import Path
import telethon.utils
from Alok import CMD_HNDLR

LUCIFER = Var.PRIVATE_GROUP_ID
BOTNAME = Var.TG_BOT_USER_NAME_BF_HER
LOAD_MYBOT = Var.LOAD_MYBOT

# let's get the bot ready
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)

async def startup_log_all_done():
    try:
        await bot.send_message(LUCIFER, f"**𝙻lok 𝙱𝙾𝚃 𝙸𝚂 𝙳𝙴𝙿𝙻𝙾𝚈𝙴𝙳.\n𝚂𝙴𝙽𝙳** `{CMD_HNDLR}alive` **𝚃𝙾 𝚂𝙴𝙴 𝙱𝙾𝚃 𝙸𝚂 𝚆𝙾𝚁𝙺𝙸𝙽𝙶 𝙾𝚁 𝙽𝙾𝚃.\n\nAdd** @{BOTNAME} **𝙰𝙳𝙳 𝚃𝙾 𝚃𝙷𝙸𝚂 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙼𝙰𝙺𝙴 𝙷𝙸𝙼 𝙰𝙳𝙼𝙸𝙽 𝙵𝙾𝚁 𝙴𝙽𝙰𝙱𝙻𝙸𝙽𝙶 𝙰𝙻𝙻 𝚃𝙷𝙴 𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂 𝙾𝙵 𝙻alok 𝙱𝙾𝚃**")
    except BaseException:
        print("Either PRIVATE_GROUP_ID is wrong or you have left the group.")

# Luciferbot starter...
# chal jana bdsk🤧 
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()

path = 'Lucifer/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

if LOAD_MYBOT == "True":
    path = "Lucifer/plugins/mybot/pmbot/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_pmbot(shortname.replace(".py", ""))
    print("TGBot set up completely!")

print("TGBot set up - Level - Basic")
print(
    """
                ----------------------------------------------------------------------
                    Alok X  ʜᴀs ʙᴇᴇɴ ᴅᴇᴘʟᴏʏᴇᴅ, ᴅᴏ ᴠɪsɪᴛ @Alok_x_Support !!
                    Alok ᴠᴇʀ: V1
                    
                ----------------------------------------------------------------------
"""
)

# that's life...
async def lucifer_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                HELL_PIC,
                caption=f"#START \n\nDeployed Alok x Successfully\n\n**Alok x. - {alok}**\n\nType {hl}ping or {hl}alive to check! \n\nJoin [support](t.me/alok_x_Support) for any query regarding Alok x userbot",
            )
    except Exception as e:
        LOGS.info(str(e))


    try:
        await bot(JoinChannelRequest("@Alok_x_userbot"))
    except BaseException:
        pass

# Why not come here and chat??
#    try:
#        await bot(JoinChannelRequest("@alok_x_support"))
#    except BaseException:
#        pass


bot.loop.create_task(alok_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()


#Alok
