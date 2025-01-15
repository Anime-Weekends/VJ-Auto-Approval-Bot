# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from database import add_user, add_group, all_users, all_groups, users, remove_user
from configs import cfg
import random, asyncio

app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_chat_join_request(filters.group | filters.channel)
async def approve(_, m : Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        await app.approve_chat_join_request(op.id, kk.id)
        await app.send_message(kk.id, "**<blockquote>Hello {} ❤</blockquote>\n\nWelcome To {}\n\n__<blockquote>Powerd By : @Anime_Weekends</blockquote>**".format(m.from_user.mention, m.chat.title))
        add_user(kk.id)
    except errors.PeerIdInvalid as e:
        print("user isn't start bot(means group)")
    except Exception as err:
        print(str(err))    
 
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Start ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.private & filters.command("start"))
async def op(_, m :Message):
    try:
        await app.get_chat_member(cfg.CHID, m.from_user.id)
    except:
        try:
            invite_link = await app.create_chat_invite_link(int(cfg.CHID))
        except:
            await m.reply("**<blockquote>Ara Ara ❤️ Always Make Sure I Am Admin In Your Channel</blockquote>**")
            return 
        key = InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("Jᴏɪɴ", url=invite_link.invite_link),
                InlineKeyboardButton("Rᴇᴛʀʏ ", callback_data="chk")
            ]]
        ) 
        await m.reply_text("**<blockquote>⚠️ Aᴄᴄᴇss ᴅᴇɴɪᴇᴅ ! ⚠️</blockquote>\n\n<blockquote expandable>Pʟᴇᴀsᴇ ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ.ɪғ ʏᴏᴜ ᴊᴏɪɴᴇᴅ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴄʜᴇᴄᴋ ᴀɢᴀɪɴ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴄᴏɴғɪʀᴍ.</blockquote>**", reply_markup=key)
        return 
    keyboard = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("🗯 Cʜᴀɴɴᴇʟ ", url="https://t.me/+0ybPnj46jcQ2N2Jl"),
            InlineKeyboardButton("💬 Sᴜᴘᴘᴏʀᴛ ", url="https://t.me/Weebs_Weekends")
        ]]
    )
    add_user(m.from_user.id)
    await m.reply_photo("https://envs.sh/vsJ.jpg", caption="**<blockquote>Hello {} 🍀</blockquote>\n<blockquote expandable>I'm an auto approve [Admin Join Requests]({}) Bot.I can approve users in Groups & Channels Add me to your chat and promote me to admin with add members permission.</blockquote>\n\n__<blockquote>Powered By : @Alisa_Zoe ✨**</blockquote>".format(m.from_user.mention, "https://t.me/+_N_ND3XfOCNhYjI1"), reply_markup=keyboard)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ callback ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_callback_query(filters.regex("chk"))
async def chk(_, cb : CallbackQuery):
    try:
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
    except:
        await cb.answer("<blockquote>❤️ Ara Ara You are not joined my channel first join channel then check again. ❤️</blockquote>", show_alert=True)
        return 
    keyboard = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("🗯 Cʜᴀɴɴᴇʟ ", url="https://t.me/+0ybPnj46jcQ2N2Jl"),
            InlineKeyboardButton("💬 Sᴜᴘᴘᴏʀᴛ ", url="https://t.me/Weebs_Weekends")
        ]]
    )
    add_user(m.from_user.id)
    await cb.edit_text(text="**<blockquote>Hello {} 🍀</blockquote>\n<blockquote expandable>I'm an auto approve [Admin Join Requests]({}) Bot.\nI can approve users in Groups / Channels.Add me to your chat and promote me to admin with add members permission.</blockquote>\n\n__<blockquote>Powered By : @Alisa_Zoe ✨**</blockquote>".format(cb.from_user.mention, "https://t.me/+_N_ND3XfOCNhYjI1"), reply_markup=keyboard)
    

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ info ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("users") & filters.user(cfg.SUDO))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
<blockquote>🍀 Chats Stats 🍀</blockquote>
<blockquote>✨ Users : `{xx}`</blockquote>
<blockquote>👥 Groups : `{x}`</blockquote>
<blockquote>❤️ Total users & groups : `{tot}`</blockquote> """)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("bcast") & filters.user(cfg.SUDO))
async def bcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("<blockquote>`⚡️ Processing...`</blockquote>")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"<blockquote expandable>✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.</blockquote>")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast Forward ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("fcast") & filters.user(cfg.SUDO))
async def fcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("<blockquote>`⚡️ Processing...`</blockquote>")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"<blockquote expandable>✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.</blockquote>")

print("I'm Alive Now!")
app.run()
