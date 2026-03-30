import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(os.getenv("API_ID", "0"))
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    MONGO_URI = os.getenv("MONGO_URI", "")
    ADMIN_ID = int(os.getenv("ADMIN_ID", "8126957656")) # Default Admin
    
    # Extra settings (Optional)
    START_MSG = (
        "✨ **Welcome to ID Finder** ✨\n\n"
        "🚀 `Use Buttons below to get someone's ID`\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "**Bot Command**\n"
        "/start **Start the bot**\n\n"
        "**Admin Command\n**"
        "/broadcast **For Broadcasting Message**\n" 
        "/stats **Show users database**\n"
    )
    DEV_TEXT = "🔗 **Developer:**[@masterbwn](t.me/masterbwn)\n\n*Contact for any queries!*"

