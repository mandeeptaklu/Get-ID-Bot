# 🚀 ID Finder Pro Bot

A professional, modular, and high-speed Telegram Bot to fetch User, Group, Channel, and Bot IDs instantly. Built with **Telethon** and powered by **MongoDB**.

---

## ✨ Features

* **Modular Architecture:** Clean code structure with `config.py` and `database.py`.
* **Database Integration:** Uses **MongoDB Atlas** for persistent data storage.
* **Interactive UI:** Stylish vertical keyboard buttons for easy navigation.
* **Admin Dashboard:** Built-in `/broadcast` feature to reach all users.
* **Developer Profile:** Integrated developer contact button.
* **Cloud Ready:** Fully compatible with Railway, Heroku, and VPS.

---

## 🛠️ Project Structure

```text
├── main.py           # Bot Logic & Event Handlers
├── config.py         # Configuration & Environment Variables
├── database.py       # MongoDB Connection & Methods
├── .env              # Secret Keys (Not uploaded to GitHub)
├── .gitignore        # Files to be ignored by Git
└── requirements.txt  # Python Dependencies

## 🚀 How to Setup (Installation Guide)

Follow these simple steps to get your own ID Finder Bot up and running in minutes!

### 1️⃣ Obtain Telegram API Keys
* Go to [my.telegram.org](https://my.telegram.org) and login.
* Click on **API Development Tools** and create a new app.
* Copy your `API_ID` and `API_HASH`.
* Get your `BOT_TOKEN` from [@BotFather](https://t.me/BotFather).

### 2️⃣ Database Setup (MongoDB)
* Create a free cluster on [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
* Whitelist your IP and create a database user.
* Copy your **Connection String** (URI).

### 3️⃣ Clone & Install
Open your Terminal or Termux and run:
```bash
# Clone the repository
git clone [https://github.com/YourUsername/ID-Finder-Bot.git](https://github.com/YourUsername/ID-Finder-Bot.git)
cd ID-Finder-Bot

# Install required libraries
pip install -r requirements.txt
🛠️ Deployment on Cloud (24/7 Online)
​If you want to keep the bot running forever without keeping your phone/PC on:
​Fork this repository to your GitHub account.
​Connect your GitHub to Railway.app or Koyeb.com.
​Add all the variables from your .env file into the Environment Variables section of the cloud provider.
​Deploy! The Procfile will handle the rest.
