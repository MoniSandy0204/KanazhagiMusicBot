from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnieXMusic import app
from config import BOT_USERNAME
from AnieXMusic.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
♡︎ ωεℓ¢σмє ƒσя ˹ᴋᴀɴᴀᴢʜᴀɢɪ ᴍᴜsɪᴄ ʙᴏᴛ ˼ ♡︎
 
 ✯ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✯
 
 ✯ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✯
 
 ✯ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✯
 
 ✯ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✯
 
 ✯ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✯
 
 ✯ ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss

 ✯ MY 𝐎ᴡɴᴇʀ  IS 𝑆 𝐴 𝑁 𝐷 𝑌✯
**"""




@app.on_message(filters.command("repo" , "Sandyrepo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝐓𝐀𝐏 𝐓𝐎 𝐒𝐄𝐄 𝐘𝐎𝐔𝐒 𝐒𝐄𝐂𝐑𝐄𝐓𝐒 💀", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("❥︎ Gʀᴏᴜᴘ 1 💗🍃", url="https://t.me/TMK_MUSICCHANNEL"),
          InlineKeyboardButton("❥︎ Gʀᴏᴜᴘ 2 💗🍃", url="https://t.me/TMK_MUSICCHANNEL"),
          ],
[
          InlineKeyboardButton("💗 ᴄʜᴀɴɴᴇʟ 💗", url="https://t.me/TMK_MUSICCHANNEL"),
          InlineKeyboardButton("💗 ᴅᴘᴢ ᴄʜᴀɴɴᴇʟ 💗", url="https://t.me/TMK_MUSICCHANNEL"),
          ],
[
              InlineKeyboardButton("˹ꞏ─𓆩‌🌼‌⃝⃪👀ᤌᰢᮀᰪᰢᰪഴᤌ᭄آ‌🐾 ⃝ ˼ 💗", url=f"@Kanazhagi_bot"),
              InlineKeyboardButton("︎˹ꞏ─𓆩‌🌼‌⃝⃪👀ᤌᰢᮀᰪᰢᰪഴᤌ᭄آ‌🐾 ⃝ ˼ 💗", url=f"@Kanazhagi_bot"),
              ],
[
InlineKeyboardButton("𝐎ᴡɴᴇʀ ♕︎", url=f"https://t.me/Mr_king008"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/65470847d88dad800596c.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://github.com/mukeshmoni/graphs/commit-activity")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://github.com/mukeshmoni/AnieMusicbot2.0) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/TMK_MUSICCHANNEL)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")
