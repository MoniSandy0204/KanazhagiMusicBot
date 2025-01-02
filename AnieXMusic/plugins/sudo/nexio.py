import requests
import random
from AnieXMusic import app, userbot
from AnieXMusic.misc import SUDOERS
from pyrogram import * 
from pyrogram.types import *
from AnieXMusic.utils.fix_ban import admin_filter






Yumikoo_text = [
"ʜᴇʏ ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ᴅɪsᴛᴜʀʙ ᴍᴇ.",
"ᴡʜᴏ ᴀʀᴇ ʏᴏᴜ",
"ᴡʜᴏ ᴀʀᴇ ʏᴏᴜ",
"ʏᴏᴜ ᴅᴏɴ'ᴛ sᴇᴇᴍ ᴛᴏ ʙᴇ ᴍʏ ᴏᴡɴᴇʀ",
"ʜᴇʏ ᴡʜʏ ᴀʀᴇ ʏᴏᴜ ᴛᴀᴋɪɴɢ ᴍʏ ɴᴀᴍᴇ, ʟᴇᴛ ᴍᴇ sʟᴇᴇᴘ",
"ʏᴇs ᴛᴇʟʟ ᴍᴇ ᴡʜᴀᴛ ᴡᴏʀᴋ ʏᴏᴜ ʜᴀᴠᴇ",
"ʟᴏᴏᴋ I ᴀᴍ ʙᴜsʏ ʀɪɢʜᴛ ɴᴏᴡ",
"ʜᴇʏ I ᴀᴍ ʙᴜsʏ",
"ᴅᴏɴ'ᴛ ʏᴏᴜ ᴜɴᴅᴇʀsᴛᴀɴᴅ?",
"ʟᴇᴀᴠᴇ ᴍᴇ ᴀʟᴏɴᴇ",
"ᴅᴜᴅᴇ ᴡʜᴀᴛ ʜᴀᴘᴘᴇɴᴇᴅ"    
]

strict_txt = [
"ɪ ᴄᴀɴ'ᴛ ʀᴇsᴛʀɪᴄᴛ ᴀɢᴀɪɴsᴛ ᴍʏ ʙᴇsᴛɪᴇs",
"ᴀʀᴇ ʏᴏᴜ sᴇʀɪᴏᴜs ɪ ᴀᴍ ɴᴏᴛ ʀᴇsᴛʀɪᴄᴛ ᴛᴏ ᴍʏ ғʀɪᴇɴᴅs"
]


 
ban = ["ban","boom"]
unban = ["unban",]
mute = ["mute","silent","shut"]
unmute = ["unmute","speak","free"]
kick = ["kick", "out","nikaal","nikal"]
promote = ["promote","adminship"]
fullpromote = ["fullpromote","fulladmin"]
demote = ["demote","lelo"]
group = ["group"]
channel = ["channel"]



# ========================================= #


@app.on_message(filters.command(["exi","exiko"], prefixes=["n", "N"]) & admin_filter)
async def restriction_app(app :app, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    if len(message.text) < 2:
        return await message.reply(random.choice(Yumikoo_text))
    bruh = message.text.split(maxsplit=1)[1]
    data = bruh.split(" ")
    
    if reply:
        user_id = reply.from_user.id
        for banned in data:
            print(f"present {banned}")
            if banned in ban:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))          
                else:
                    await app.ban_chat_member(chat_id, user_id)
                    await message.reply("ᴠᴇʟɪʏᴀ ᴘᴏᴅᴀ ᴛʜᴀᴍʙɪ")
                    
        for unbanned in data:
            print(f"present {unbanned}")
            if unbanned in unban:
                await app.unban_chat_member(chat_id, user_id)
                await message.reply(f"ɴᴇᴇ ᴇɴ ᴘᴀɴɢᴀʟɪ ᴅᴀ") 
                
        for kicked in data:
            print(f"present {kicked}")
            if kicked in kick:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))
                
                else:
                    await app.ban_chat_member(chat_id, user_id)
                    await app.unban_chat_member(chat_id, user_id)
                    await message.reply("get lost! ") 
                    
        for muted in data:
            print(f"present {muted}") 
            if muted in mute:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))
                
                else:
                    permissions = ChatPermissions(can_send_messages=False)
                    await message.chat.restrict_member(user_id, permissions)
                    await message.reply(f"muted successfully! Disgusting people.") 
                    
        for unmuted in data:
            print(f"present {unmuted}")            
            if unmuted in unmute:
                permissions = ChatPermissions(can_send_messages=True)
                await message.chat.restrict_member(user_id, permissions)
                await message.reply(f"Huh, OK, sir!")   


        for promoted in data:
            print(f"present {promoted}")            
            if promoted in promote:
                await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=True,
                    can_delete_messages=True,
                    can_restrict_members=False,
                    can_pin_messages=True,
                    can_promote_members=False,
                    can_manage_chat=True,
                    can_manage_video_chats=True,
                       )
                     )
                await message.reply("promoted !")

        for demoted in data:
            print(f"present {demoted}")            
            if demoted in demote:
                await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=False,
                    can_delete_messages=False,
                    can_restrict_members=False,
                    can_pin_messages=False,
                    can_promote_members=False,
                    can_manage_chat=False,
                    can_manage_video_chats=False,
                       )
                     )
                await message.reply("demoted !")


#async def your_function():
    for fullpromoted in data:
        print(f"present {fullpromoted}")            
        if fullpromoted in fullpromote:
            await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
                can_change_info=True,
                can_invite_users=True,
                can_delete_messages=True,
                can_restrict_members=True,
                can_pin_messages=True,
                can_promote_members=True,
                can_manage_chat=True,
                can_manage_video_chats=True,
               )
             )
            await message.reply("fullpromoted !")
