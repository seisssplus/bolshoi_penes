from random import choice
from time import sleep
from pyrogram import Client, filters
from pyrogram.enums import ChatType
import os

api_id = 23962937
api_hash = 'e247a38e5d7d45235018717e76920252'
app = Client('client', api_id, api_hash)



@app.on_message(filters.command("rh", prefixes=[".", "/"]) & filters.me)
async def help(_, msg):
    await msg.delete()
    global uuui, help_text, help_photo_lish

    photo_help = "https://te.legra.ph/file/01191d867bc78093c9030.jpg"
    ksd = await app.get_chat(msg.chat.id)
    help_text = f"<b>𝗥 𝗘 𝗩 𝗢 𝗥 𝗛</b>\n\n" \
                f"<b>✟</b> <code>/rhst</code> ‒ time + chat id + shabl + shapka\n"\
                f"<b>✟</b> <code>/revorh</code> ‒ time + chat id + shabl + shapka(reply)\n" \
                f"<b>✟</b> <code>/der</code> ‒ директория шаблонов\n" \
                f"<b>✟</b> <code>/id</code> ‒ ID чата\пользователя(reply)\n"

    if ksd.type == ChatType.PRIVATE:
        await app.send_photo(msg.chat.id, photo="https://te.legra.ph/file/0363411881233fca2a416.jpg", caption=help_text)
    else:
        dddjs = ksd.permissions.can_send_media_messages
        if not dddjs:
            await app.send_message(msg.chat.id, help_text)
        else:
            await app.send_photo(msg.chat.id, photo_help, caption=help_text)


@app.on_message(filters.command('rhst', prefixes=[".", "/"]) & filters.me)
def spam(_, msg):
    msg.delete()
    global spam1, txtsh1
    spam1 = True
    text1 = msg.text.split('rhst', maxsplit=1)[1]
    textr1 = text1.split(' ')
    time1 = int(textr1[1])
    id_chat1 = int(textr1[2])
    if id_chat1 == 1:
        id_chat1 = msg.chat.id
    shb1 = int(textr1[3])
    if shb1 == 1:
        shbb1 = "shabl3.txt"
    elif shb1 == 2:
        shbb1 = "shabl4.txt"
    shp = textr1[4:]
    sh1 = ' '.join(shp)
    while spam1:
        lines = []
        with open(shbb1, 'r', encoding='utf8') as file:
            for line in file:
                lines.append(line)
            random_line1 = choice(lines)
            app.send_message(id_chat1, f"{sh1}" + ' ' + random_line1)
            sleep(time1)

@app.on_message(filters.command("defrh", prefixes=[".", "/"]) & filters.me)
def offspam(_, msg):
    msg.delete()
    global spam1, spam_fn
    spam1 = False


@app.on_message(filters.command("revorh", prefixes=[".", "/"]) & filters.me)
async def spamod(_, msg):
    global spam60
    text60 = msg.text.split('revorh', maxsplit=1)[1]
    textr60 = text60.split(' ')
    time60 = int(textr60[1])
    idChatas60 = int(textr60[2])
    if idChatas60 == 1:
        idChatas60 = msg.chat.id
    shanilonessu60 = int(textr60[3])
    if shanilonessu60 == 1:
        shanilonessuu60 = "shabl3.txt"
    elif shanilonessu60 == 2:
        shanilonessuu60 = "shabl4.txt"
    shp0 = textr60[4:]
    sh10 = ' '.join(shp0)
    if msg.reply_to_message:
        await msg.delete()
        spam60 = True
        dfdf = msg.reply_to_message.id
        while spam60:
            lines = []
            with open(shanilonessuu60, 'r', encoding='utf8') as file:
                for line in file:
                    lines.append(line)
                random_line1 = choice(lines)
            await app.send_message(idChatas60, f"{sh10 + ' ' + random_line1}", reply_to_message_id=dfdf)
            sleep(time60)
    else:
        await msg.edit("ответь на сообщение")


@app.on_message(filters.command("rhdef", prefixes=[".", "/"]) & filters.me)
def offspamod(_, msg):
    msg.delete()
    global spam60
    spam60 = False



@app.on_message(filters.command("der", prefixes=[".", "/"]) & filters.me)
def count_messages_in_files(_, msg):
    directory_path = os.path.dirname(__file__)
    files = []

    for file_name in os.listdir(directory_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(directory_path, file_name)
            with open(file_path, "r") as file:
                lines = file.readlines()
                message_count = len(lines) // 2 
                files.append((file_name, message_count))

    response = "<b>Деректория:</b>\n\n"
    for idx, (file_name, message_count) in enumerate(files, start=1):
        response += f"<b>{idx}</b>. {file_name} - {message_count} сообщений\n"
    msg.edit(response)


@app.on_message(filters.command("id", prefixes=[".", "/"]) & filters.me)
def id(_, msg):
    msg.delete()
    if msg.reply_to_message:
        app.send_message("me", f"Name: {msg.reply_to_message.from_user.first_name}\n"
                               f"Username: @{msg.reply_to_message.from_user.username or '-'}\n"
                               f"User ID: <code>{msg.reply_to_message.from_user.id}</code>\n"
                               f"Chat ID: <code>{msg.chat.id}</code>"
                         )
    else:
        app.send_message("me", f"Name: {msg.chat.title}\n"
                               f"Invite Link: @{msg.chat.username or '-'}\n"
                               f'Count: {app.get_chat_members_count(msg.chat.id)}\n'
                               f"Chat ID: <code>{msg.chat.id}</code>")


print("""
█▀▀▄ █▀ █░█ ▄▀▄ █▀▀▄ █░█
█▐█▀ █▀ █░█ █░█ █▐█▀ █▀█
▀░▀▀ ▀▀ ░▀░ ░▀░ ▀░▀▀ ▀░▀
""")
app.run()
