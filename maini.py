import random
import telebot
import re
import sqlite3

conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, chat_id INTEGER, textN TEXT, displei TEXT, nobykv TEXT, points INTEGER, lvlU INTEGER)''')
conn.commit()

def load_data():
    users = {}
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        users[row[1]] = {
            "textN": row[2],
            "displei": row[3].split(", "),
            "nobykv": row[4].split(", "),
            "points": row[5],
            "lvlU": row[6]
        }
    return users

def save_data(users):
    for chat_id, user_data in users.items():
        cursor.execute("SELECT * FROM users WHERE chat_id=?", (chat_id,))
        row = cursor.fetchone()
        if row:
            cursor.execute("UPDATE users SET textN=?, displei=?, nobykv=?, points=?, lvlU=? WHERE chat_id=?",
                           (user_data["textN"], ", ".join(user_data["displei"]), ", ".join(user_data["nobykv"]), user_data["points"], user_data["lvlU"], chat_id))
        else:
            cursor.execute("INSERT INTO users (chat_id, textN, displei, nobykv, points, lvlU) VALUES (?, ?, ?, ?, ?, ?)",
                           (chat_id, user_data["textN"], ", ".join(user_data["displei"]), ", ".join(user_data["nobykv"]), user_data["points"], user_data["lvlU"]))
        conn.commit()

ru = r"^[а-я]+$"

bot = telebot.TeleBot('6849574384:AAGTMVbU8aPZPnymaB-OK_U2pz7C9bWhj2g')

users = {}

@bot.message_handler(commands=["restart"])
def restart(message):
    chat_id = message.chat.id
    global users
    
    levels = {1:["кот", "хол", "зуб", "нос", "лук", "рука", "язь", "юно", "лес", "слон", "сон", "снег", "кот", "оба", "муха", "гриб", "сад", "гром", "мяу", "мышь"],2:["дома", "солнце", "ночь", "море", "ручка", "книга", "мыло", "соль", "стол", "бокал", "носок", "кость", "крыша", "гора", "лужа", "страх", "крышка", "тень", "ледышка", "курок", "слон", "цвет", "муза", "штат", "крыша", "кора", "яма", "буря", "глаз", "русь"]}
    
    users = load_data()
    
    if chat_id in users:
        if users[chat_id].get("lvlU") == 1:
            lvlU = users[chat_id].get("lvlU",1)
        elif users[chat_id].get("lvlU") == 2:
            lvlU = users[chat_id].get("lvlU",2)
        lvlWords = levels.get(lvlU,levels[1])
        
        textN = lvlWords[random.randint(0, len(lvlWords)-1)]
        displei = ["_" for _ in textN]
        nobykv = []
        
        users[chat_id] = {"textN": textN, "displei": displei, "nobykv": nobykv, "points": users[chat_id]["points"], "lvlU": lvlU}
        save_data(users)
    else:
        lvlU = 1
        lvlWords = levels.get(lvlU,levels[1])
        
        textN = lvlWords[random.randint(0, len(lvlWords)-1)]
        displei = ["_" for _ in textN]
        nobykv = []
        
        users[chat_id] = {"textN": textN, "displei": displei, "nobykv": nobykv, "points": 0, "lvlU": 1}
        save_data(users)
        
    bot.send_message(chat_id, " ".join(displei) + "\n неправильные буквы: \n" + str(nobykv))
    
    bot.send_message(chat_id,"Новое слово - /restart\nМеню - /menu")
    
@bot.message_handler(commands=["menu"])
def menu(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Version - 1.5_dec\nЭто меню, куда вас переправить:\nПрофиль - /stats\nМагазин - /shop\nНовое слово - /restart")

@bot.message_handler(commands=["stats"])
def stats(message):
    chat_id = message.chat.id
    users = load_data()
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    if chat_id in users:
        points = users[chat_id]["points"]
        lvlU = users[chat_id]["lvlU"]
        bot.send_message(chat_id, f"{first_name} {last_name}\nВаш ID - {chat_id}\nВаши баллы: {points}\nУровнь: {lvlU}")
    else: bot.send_message(chat_id, "Вы ещё не начали игру /restart")

@bot.message_handler(commands=["shop"])
def stats(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Функция ещё в разработке!")

@bot.message_handler()
def send_message(message):
    chat_id = message.chat.id
    user = message.text.lower()
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    from_user = message.from_user.username

    if chat_id in users:
        textN = users[chat_id]["textN"]
        displei = users[chat_id]["displei"]
        nobykv = users[chat_id]["nobykv"]
        points = users[chat_id]["points"]

        if user in textN:
            for i in range(len(textN)):
                if textN[i] == user:
                    displei[i] = user
            users[chat_id]["displei"] = displei
            bot.send_message(chat_id, " ".join(displei) + "\n неправильные буквы: \n" + str(nobykv))
        
            if not "_" in displei:
                points += 1
                users[chat_id]["points"] = points
                bot.send_message(chat_id, f"Вы смогли отгадать слово: {textN}! Теперь ваши баллы {points}")
        else:
            if len(user) == 1 and user not in nobykv and re.match(ru,user):
                nobykv.append(user)
                users[chat_id]["nobykv"] = nobykv
            else:
                if not re.match(ru,user):
                    bot.send_message(chat_id,"Пишите только русские буквы")
                if not len(user) == 1:
                    bot.send_message(chat_id,"Пишите одну букву")
            bot.send_message(chat_id, " ".join(displei) + "\n неправильные буквы: \n" + str(nobykv))

        print(f"\n@{from_user}"," ",first_name," ",last_name,"\n",users[chat_id]["textN"],"\n",users[chat_id]["nobykv"],"\n"," ".join(users[chat_id]["displei"]),"\n",users[chat_id]["points"],"\n")
    bot.send_message(chat_id,"Новое слово - /restart\nМеню - /menu")
bot.polling(none_stop=True,timeout=30)
