import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from AnieXMusic import LOGGER, app, userbot
from AnieXMusic.core.call import FIXX
from AnieXMusic.misc import sudo
from AnieXMusic.plugins import ALL_MODULES
from AnieXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐒𝐞𝐬𝐬𝐢𝐨𝐧")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AnieXMusic.plugins" + all_module)
    LOGGER("AnieXMusic.plugins").info("ᴀʟʟ ғᴇᴀᴛᴜʀᴇs ʟᴏᴀᴅᴇᴅ ʙᴀʙʏ🥳.....")
    await userbot.start()
    await FIXX.start()
    try:
        await FIXX.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("AnieXMusic").error(
            "ᴘʟᴢ sᴛᴀʀᴛ ʏᴏᴜʀ ʟᴏɢ ɢʀᴏᴜᴘ ᴠᴏɪᴄᴇᴄʜᴀᴛ\ᴄʜᴀɴɴᴇʟ\n\ ᴍᴜsɪᴄ ʙᴏᴛ sᴛᴏᴘ........"
        )
        exit()
    except:
        pass
    await FIXX.decorators()
    LOGGER("AnieXMusic").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ☠︎︎ᴍᴀᴅᴇ ᴍʏ ᴍʀ ᴍᴜsɪᴄ ☠︎︎\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("AnieXMusic").info("sᴛᴏᴘ ᴍᴜsɪᴄ ᴍᴜsɪᴄ🎻 ʙᴏᴛ..")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
