from telethon import TelegramClient, events, types
from config import Config
from database import save_user, get_all_users

# Bot Connection using Config
bot = TelegramClient('id_pro_session', Config.API_ID, Config.API_HASH).start(bot_token=Config.BOT_TOKEN)

# ID Fix Function (Wahi pehle wala)
def format_id(peer, raw_id):
    str_id = str(raw_id)
    if not isinstance(peer, (types.RequestedPeerUser, types.PeerUser)):
        if not str_id.startswith("-"):
            if not str_id.startswith("100"):
                return f"-100{str_id}"
            else:
                return f"-{str_id}"
    return str_id

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    save_user(event.sender_id)
    
    kb_buttons = [
        [types.KeyboardButton("👨‍💻 Developer Profile")], 
        [types.KeyboardButtonRequestPeer("👤 User ID", 1, types.RequestPeerTypeUser(bot=False), 1)],
        [types.KeyboardButtonRequestPeer("🤖 Bot ID", 2, types.RequestPeerTypeUser(bot=True), 1)],
        [types.KeyboardButtonRequestPeer("👥 Group ID", 3, types.RequestPeerTypeChat(), 1)],
        [types.KeyboardButtonRequestPeer("📢 Channel ID", 4, types.RequestPeerTypeBroadcast(), 1)]
    ]
    
    await bot.send_message(event.chat_id, Config.START_MSG, buttons=kb_buttons)

@bot.on(events.Raw())
async def raw_handler(event):
    try:
        if isinstance(event, types.UpdateNewMessage):
            msg = event.message
            
            if msg.message == "👨‍💻 Developer Profile":
                await bot.send_message(msg.peer_id, Config.DEV_TEXT, parse_mode='md')
                return

            action = getattr(msg, 'action', None)
            if action and (isinstance(action, types.MessageActionRequestedPeerSentMe) or 
                          isinstance(action, types.MessageActionRequestPeerSent)):
                
                for peer in action.peers:
                    raw_id = getattr(peer, 'user_id', None) or \
                             getattr(peer, 'chat_id', None) or \
                             getattr(peer, 'channel_id', None)
                    
                    if raw_id:
                        final_id = format_id(peer, raw_id)
                        response_text = (
                            f"🔸 **ID Found :**\n\n"
                            f"`{final_id}`\n\n"
                            f"👆 **Click on ID to copy**"
                        )
                        await bot.send_message(msg.peer_id, response_text, reply_to=msg.id, parse_mode='md')
    except Exception as e:
        print(f"Error: {e}")

@bot.on(events.NewMessage(pattern='/broadcast'))
async def broadcast_handler(event):
    if event.sender_id != Config.ADMIN_ID: return
    b_message = event.message.message.replace('/broadcast', '').strip()
    if not b_message: return

    await event.reply("🚀 Broadcasting...")
    all_users = get_all_users()
    success = 0
    for user_doc in all_users:
        try:
            await bot.send_message(user_doc['user_id'], b_message)
            success += 1
        except: pass
    await event.reply(f"✅ Sent to {success} users.")

print("✅ Bot is Live with Modular Structure (Config + Database)!")
bot.run_until_disconnected()

