from pyrogram import Client, filters
from handler import check_heroku

@Client.on_message(filters.command('rebootmusic') & filters.user(870471128))
@check_heroku
async def gib_restart(client, message, hap):
    msg_ = await message.reply_text("[Oda Music] - Restarting")
    hap.restart()
