from telethon import events
from config import Config
from .. import database 

# Stats Command
@events.register(events.NewMessage(pattern='/stats'))
async def stats(event):
    if event.sender_id != Config.ADMIN_ID:
        return
    users = database.get_all_users() 
    total = len(users) if users else 0
    await event.respond(f"📊 **Total Users:** `{total}`")

# Broadcast Command

@events.register(events.NewMessage(pattern='/broadcast'))
async def broadcast(event):
    if event.sender_id != Config.ADMIN_ID:
        return
        
    if not event.reply_to_msg_id:
        return await event.respond("❌ Kisi message ko reply karke `/broadcast` likho!")
    
    msg = await event.get_reply_message()
    
    # --- YAHAN CHECK KARO ---
    # Database se users ki list uthao (Await hata dena agar Pymongo sync hai)
    all_users = database.get_all_users() 
    
    count = 0
    await event.respond("🚀 Broadcast shuru ho raha hai...")
    
    # Loop mein 'all_users' (jo upar define kiya hai) wahi use karo
    for user_doc in all_users:
        try:
            # MongoDB mein user_id 'user_id' key ke andar hoti hai
            u_id = user_doc['user_id'] 
            await event.client.send_message(u_id, msg)
            count += 1
        except Exception as e:
            print(f"Error sending to {user_doc.get('user_id')}: {e}")
            
    await event.respond(f"✅ Broadcast complete! `{count}` users ko message mil gaya.")

