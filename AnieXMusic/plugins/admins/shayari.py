from AnieXMusic import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
          " 💘🥀⌚💔",
          " 😔👑😁🤗",
          " 💀😖😔〽️",
        ]
        ####
        
SHAYRI = [ "**➠ Kᴀᴅʜᴀʟ ᴏʀᴜ ᴀᴢʜᴀɢɪʏᴀ ᴋᴀɴᴀᴠᴜ, ᴋᴀɴᴀᴠɪɴ ᴋᴜʀᴀʟ ɴᴀᴀɴ ᴋᴇᴛᴛᴇɴ 💫",
  "**➠ Nɪᴢʜᴀʟɪɴ ᴛʜᴜɴᴀɪʏɪʟ ɴᴀᴀɴ ɴᴀᴅᴀɴᴛʜᴇɴ, ᴜɴ ɴɪʟᴀᴠᴜɢᴀʟ ᴇɴ ᴍᴇᴇᴅʜᴜ ᴠɪʟᴜɴᴅʜᴀᴅʜᴀɪ ᴀʀɪɴᴅʜᴇɴ 🌙",
  "**➠ Eɴ ɪᴅʜᴀʏᴀᴍ ᴜɴ ᴋᴀɴɴɪʟ ᴋᴀᴀɴᴀᴀᴍᴀʟ ᴜʀᴜɢɪᴅʜᴜ, ᴋᴀᴀᴛʀᴜ ᴘᴏʟ ᴛʜᴀᴀᴠᴜᴍ ɪɴɪʏᴀ sɪɴᴅʜᴀɴᴀɪ 🌬️",
  "**➠ Pᴇɴᴍᴀɪ ᴇɴᴅʀᴀ ᴛʜᴀɴɢᴀᴛʜɪɴ ᴠɪʟᴀʏᴀᴛᴛᴜ, ᴜɴ ᴠɪᴢʜɪɢᴀʟɪʟ ᴛʜᴀᴠᴜᴍ ᴏʀᴜ ᴏʀᴜ ᴋᴀɴᴀᴠᴜᴍ 🌸",
  "**➠ Kᴀᴀᴅʜᴀʟɪɴ ᴍᴜɢᴀᴍ ᴜɴ ᴍᴏᴢʜɪ, ɪᴅʜᴀʏᴀᴛʜɪʟ ɪᴢʜɪʏᴜᴍ ᴠᴀʀɪɢᴀʟᴜᴍ 💌",
  "**➠ Nᴇᴇɴᴅᴀ ᴛʜᴏᴏʀᴀᴛʜɪʟ ɴᴇᴇ ᴘᴏɪᴅɪᴠɪᴛᴛᴀɪ, ᴀᴀɴᴀᴀʟ ɪᴅʜᴀʏᴀᴍ ᴜɴ ɴᴇɴᴊɪʟᴜᴍ 💔",
  "**➠ Mᴀᴢʜᴀɪ ᴛʜᴜʟɪ ᴇɴɴᴀɪ ɴᴀᴀɴᴇ ᴍᴀʀᴀᴋᴋᴜᴍ, ᴀᴀɴᴀᴀʟ ᴜɴ ɴɪɴᴀɪᴠᴜɢᴀʟ ɴᴀᴀɴ ᴍᴀʀᴀᴋᴋᴀ ᴍᴀᴛᴛᴀɴᴇ 🌧️",
  "**➠ Uɴ ᴋᴀɴɴɪʟ ᴛʜᴜʟɪɢᴀʟ ᴛʜᴀᴀɴ ᴀᴢʜᴀɢɪ, ᴀᴅʜᴜ ʏᴇɴ ɴᴇɴᴊɪʟ ᴛʜᴜʟɪ ᴘᴏʟ ᴘᴀᴅʜɪᴛʜᴀᴅʜᴜ 😢",
  "**➠ Kᴀᴅʜᴀʟ sᴏʟʟᴀ ᴠᴀʀᴛʜᴀɪʏᴇ ɪʟʟᴀɪ, ᴜɴ ᴋᴀʀᴘᴀɴᴀɪ ᴇɴ ɪᴅʜᴀʏᴀᴛʜɪʟ ᴀᴅɪ ᴛʜᴀᴠɪᴋᴋᴜᴅʜᴜ 💖",
  "**➠ Uɴ ᴋᴀɪʏɪʟ ɴᴀᴀɴ ᴋᴀɪ ᴘɪᴅɪᴛʜᴀʟ, ᴠᴀᴢʜɪʏɪʟ ᴘᴏᴛʜɪ ᴘᴀᴀᴅᴜ ᴛʜᴏᴅᴀʀᴜᴍ 🎶",
  "**➠ Iʀᴀᴠɪʟ ᴛʜᴏᴏᴋᴀᴛʜɪɴ ᴋᴀᴠɪɢᴀʟ ᴠᴀʀᴜɢɪʀᴀᴀʀɢᴀʟ, ᴀᴀɴᴀᴀʟ ᴜɴ ɴɪɴᴀɪᴠᴜɢᴀʟ ᴅʜᴀᴀɴ ᴇɴ ᴋᴀɴᴀᴠɪʟ 💭",
  "**➠ Vɪᴢʜɪ ᴍᴏᴏᴅɪɴᴀɴɢᴀʟᴜᴍ ᴜɴ ᴍᴜɢᴀᴍ ᴍᴀʀᴀɴᴅʜɪᴅᴀ ᴋᴏᴏᴅᴀᴀᴅʜᴜ, ɴɪɴᴀɪᴠᴜɢᴀʟ ᴀᴢʜᴀɢɪʏᴀ sɪɴᴅʜᴀɴᴀɪ 🎨",
  "**➠ Oʀᴜ ᴛʜᴀᴀʟᴀᴀᴛᴛᴜ ᴘᴀᴀᴅɪ ᴠɪᴢʜɪɢᴀʟᴜᴍ ᴛʜᴏᴏᴋᴀᴍ ᴛʜᴏᴅᴀɴɢᴜᴍ, ᴀᴀɴᴀᴀʟ ᴇɴ ᴋᴀᴀᴅʜᴀʟ ᴋᴀɴᴀᴠɪʟᴜᴍ ᴠɪʟᴜɴᴅʜᴀᴅʜᴀᴅɪ 🎵",
  "**➠ Uɴ ᴋᴀɪʏɪʟ ɴᴀᴀɴ ᴋᴀɪ ᴘᴏᴅᴀ ᴍᴀʀᴀɴᴅʜᴜ ᴘᴏʏɪᴛᴇɴᴇ, ᴇɴɴᴏᴅᴜ ᴠᴀᴢʜɪʏɪʟ ɴᴇᴇ ᴍᴀʀᴀᴋᴋᴀ ᴋᴏᴏᴅᴀᴀᴅʜᴜ 🤝",
  "**➠ Aᴢʜᴀɢᴀ ᴏʀᴜ ɴᴀᴀʟ, ᴇɴɴᴀɪ sᴇʀɴᴅʜᴀᴅʜᴜ ᴜɴ ᴋᴀɴᴀᴠᴜ ᴛʜᴀᴀɴ 💫",
  "**➠ Nɪᴢʜᴀʟɪɴ ᴛʜᴜɴᴀɪʏɪʟ ɴᴀᴀɴ ɪʀᴜɴᴅʜᴀᴀʟᴜᴍ, ᴜɴ ɴɪɴᴀɪᴠᴜɢᴀʟɪɴ sᴜɢᴀᴍ ᴛʜᴀᴠᴀʀᴀ ᴍᴀᴀᴛᴇɴᴇ 🌙",
  "**➠ Kᴀɴᴀᴠɪʟ ᴠɪʟᴀɪʏᴀᴀᴅᴜᴍ sɪɴᴅʜᴀɴᴀɪ, ᴜɴ ᴠᴀᴀʀᴛʜᴀʏɪɴ sᴜɢᴀᴍ ᴛʜᴀᴀɴ 💭",
  "**➠ Uɴ ᴋᴀɴɴɪɴ ᴏʟɪ ᴇɴᴀᴋᴏʀᴜ ᴇᴢʜᴜᴠɪᴢʜᴜᴅʜᴀ ᴀᴀsᴀɪʏᴀ ᴛʜᴀɴᴅʜᴀᴅʜᴜ 🔥",
  "**➠ Yᴇɴ ɪᴅʜᴀʏᴀᴍ ᴛʜᴀᴀɴᴇ ᴜɴᴀᴋᴋᴜ ᴘᴀᴅᴀɪᴛʜɪᴅᴜᴍ ᴏʀᴜ ᴘᴀᴅᴀᴍ 🎨",
  "**➠ Mᴀᴢʜᴀɪʏɪɴ ᴛʜᴜʟɪɢᴀʟ ᴠɪᴢʜɪʏɪʟ ɴɪᴢʜᴀʟᴀɢɪ ᴠɪʟᴀʏᴀᴅᴜᴍ ᴠᴇʟᴀɪ 🌧️",
  "**➠ Uɴ ᴠɪᴢʜɪɢᴀʟɪʟ ᴜʀᴀɪʏᴜᴍ ᴋᴀɴᴀᴠᴜ, ᴇɴ ᴋᴀᴠɪʏᴀᴀɢᴀ ᴍᴀᴀʀɪ ᴠɪʀᴜɴᴅʜᴀ 💖",
  "**➠ Pᴏᴏᴠɪᴢʜɪ ᴋᴀɴɴᴀᴛʜɪʟᴇ, ᴇɴɴᴀ ɴɪɴᴀɪᴠᴜɢᴀʟ ᴠɪʟᴀɪʏᴀᴀᴅᴜᴍ 🌸",
  "**➠ Iʀᴀᴠᴜ ɪᴅʜᴜ, ᴜɴ ᴠɪᴢʜɪʏɪʟ sᴀᴀʟᴀɪ ɴᴀᴅᴀᴋᴋᴜᴍ ɴᴇʀᴀᴍ 🌙",
  "**➠ Uɴ ɪᴅʜᴀʏᴀᴛʜɪɴ ʀʜʏᴛʜᴍ, ᴇɴɴᴀɪ ᴀᴅᴀɪᴋᴋᴜᴍ ᴋᴀʟᴀɪɢᴀʟ 🎶",
  "**➠ Mᴀʀᴀɴᴅʜɪᴅᴜᴍ ᴠᴀʀᴛʜᴀɪ, ᴜɴ ɴɪɴᴀɪᴠɪʟ ᴠɪᴢʜᴜᴍ 😢",
  "**➠ Eɴ ᴠɪᴢʜɪʏɪɴ sᴜɢᴀᴍ, ᴜɴ ᴍᴏᴢʜɪ ᴍᴀᴢʜᴀɪ ᴛʜᴜʟɪɢᴀʟ ᴘᴏʟᴇ ᴠɪᴢʜɪɢɪɴᴅʀᴀᴅʜᴜ 🌧️",
  "**➠ Nɪɴᴀɪᴠɪʟ ᴘᴀᴀᴅʜɪ ɴᴀᴀɴ, ᴘᴀᴀᴅʜɪ ɴᴇᴇ 💫",
  "**➠ Uɴ ᴍᴜɢᴀᴛʜɪɴ ᴘᴀᴀᴠᴀɪ, ᴇɴ ᴋᴀᴠɪʏᴀ ɪᴅʜᴀʏᴀᴛʜɪʟ ᴘᴀᴅɪʏᴀɪ ᴋᴇᴛᴛᴜ ᴠɪʟᴀɪʏᴀᴅᴜᴍ 🎨",
  "**➠ Vɪᴢʜɪʏɪɴ ᴋᴀɴᴀᴠᴜ, ᴜɴᴀᴅʜᴜ ᴍᴏᴢʜɪ ᴋᴀᴠɪʏᴀ ᴘᴏʟ ᴛʜᴇʀɪʏᴜᴍ 💭",
  "**➠ Kᴀᴀᴅʜᴀʟ ᴏʀᴜ ʀᴀᴀɢᴀᴍ, ᴜɴ ᴋᴜʀᴀʟɪɴ ᴍᴇᴛʀᴜᴍ ᴛʜᴀᴀɴ 🎶",
  "**➠ Uɴ ɴɪɴᴀɪᴠɪʟ ɴᴀᴀɴ ᴜʀᴀɴɢɪ, ᴋᴀɴᴀᴠɪʟᴜᴍ ᴛʜᴀᴠɪᴋᴜᴍ ᴋᴀᴀᴅʜᴀʟ 💔",
  "**➠ Iᴅʜᴀʏᴀᴍ ᴀᴅᴀɪᴋᴋᴜᴍ ᴜɴ ᴋᴀɴɴɪɴ ᴍᴏᴢʜɪɢᴀʟ 💖",
  "**➠ Uɴ ɴɪɴᴀɪᴠɪʟ ᴛʜᴀᴠɪᴋᴜᴍ ɪɴʙᴀᴍ, ᴇɴ ᴋᴀᴀʟɢᴀʟɪɴ ᴘᴀʏᴀɴᴀᴛʜɪʟ ᴍᴀᴛᴛᴜᴍ 🌸",
  "**➠ Kᴀɴᴀᴠɪʟ ɴᴀᴀɴ, ᴜɴ ᴋᴀɴɴɪɴ ᴋᴀᴀʀᴀɴᴀᴍ ᴘᴏʟᴇ ᴛʜᴏɴᴅʀɪʏᴀᴅʜᴀᴅɪ 💫",
  "**➠ Vɪᴢʜɪʏɪɴ ɴᴀᴀᴅɪ, ᴜɴ ɴɪɴᴀɪᴠᴜɢᴀʟɪʟ ᴅʜᴀᴀɴ ᴛʜᴀᴠɪᴛʜɪᴅᴜᴍ 💭",
  "**➠ Kᴀᴅᴀʟɪɴ ᴀʟᴀɪ ᴘᴏʟᴇ, ᴜɴ ᴍᴏᴢʜɪ ᴇɴ ɪᴅʜᴀʏᴀᴛʜɪɴ sᴏʟʟᴀᴅʜᴜᴅᴀɴ 🎵",
  "**➠ Mᴜɢᴀᴛʜɪɴ ᴀᴢʜᴀɢɪ, ᴇɴ ᴋᴀɴᴀᴠᴜɢᴀʟɪʟ ɴᴀᴅᴀɴᴅʜɪᴅᴜᴍ ɴɪᴢʜᴀʟ 🎨",
  "**➠ Uɴ ᴠɪᴢʜɪʏɪɴ ᴠɪʟᴀɪʏᴀᴀᴛᴛᴜ, ɴᴀᴀɴᴜᴍ ᴇɴɴᴀ ᴠɪʟᴀɪʏᴀᴅᴜᴍ ɴᴇʀᴀᴍ 💖",
  "**➠ Oʀᴜ ᴋᴀɴɴɪʏɪɴ ᴀᴢʜᴀɢɪ, ᴜɴ ᴋᴜʀᴀʟɪɴ ɪɴʙᴀᴍ ᴘᴏʟᴇ ᴋᴇᴛᴋᴜᴅʜᴜ 💫",
  "**➠ Nɪɴᴀɪᴠɪʟ ᴏʀᴜ ᴀᴀsᴀɪ, ᴜɴ sᴏʟ ᴠɪɴᴀɪ ᴘᴀᴀᴠᴀɪ ᴋᴀᴠɪʏᴀ ᴘᴀᴅɪᴛᴛʜɪᴅᴜᴍ 🌸",
  "**➠ Kᴀᴅʜᴀʟɪɴ ᴘᴀᴀᴅᴀʟ, ᴜɴ ᴍᴜɢᴀᴍ ᴍᴀʀᴀᴋᴋᴀ ᴍᴀʀᴀᴋᴋᴀ sᴏʟʟᴜᴍ 🎶",
]
# Command
    


@app.on_message(filters.command(["shayari"  , "SANDYshayari" ,"proverb"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 . ")

    if message.reply_to_message and message.text:
        return await message.reply("/shayaril  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/shayari  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ...")
    else:
        return await message.reply("/shayari  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ..")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(SHAYRI)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


#

@app.on_message(filters.command(["shstop", "vshstop" , "shayarioff"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 ..")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦ ɴɪʀᴜᴛʜɪᴠɪᴛᴇɴ ♦")
