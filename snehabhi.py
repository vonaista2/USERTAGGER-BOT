#RAPİD T@G MENTION BOT
#DEVELOPER @EfsaneLions😘

import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
  level=logging.INFO,
  format='%(message)s - %(name)s - [%(levelname)s]'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

moment_worker = []

@client.on(events.NewMessage(pattern='^(?i)/bitir$'))
async def cancel(event):
  global moment_worker
  moment_worker.remove(event.chat_id)
  
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("MERHABA. BEN RAPİD T@G. GRUBUNUZDA SİZİN YERİNİZE ETİKET ATABİLİRİM. DESTEK KANALIMIZ İÇİN [RAPİD DESTEK](HTTP://T.ME/RapidDestek). YARDIM MENÜSÜ İÇİN /help YAZIN.",
                    buttons=(
                      [Button.url('🙃 GRUBA EKLE 🙂', 'https://t.me/rapidtagbot?startgroup=true')],
                      [Button.url('DESTEK KANALIMIZ', 'https://t.me/RapidDestek')],
                      [Button.url('DEVELOPER', 'https://t.me/EfsaneLions')]
                      ),
                    link_preview=False
                    )



@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "***RAPİD T@G YARDIM MENÜSÜ**\n\nKOMUT: /all \n YAZARAK ETİKET İŞLEMİNİ BAŞLATABİLİRSİNİZ \n`ÖRNEK: /all GÜNAYDIN!` \nAYNI KOMUTU BİR MESAJA YANIT VEREREK O MESAJA KULLANICILARI ETİKETLEYEBİLİRSİNİZ. /bitir KOMUTU ETİKETLEME İŞLEMİNİ BİTİRİR"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('🙃 GRUBA EKLE 🙂', 'https://t.me/rapidtagbot?startgroup=true')],
                      [Button.url('DESTEK KANALIMIZ', 'https://t.me/RapidDestek')],
                      [Button.url('DEVELOPER', 'https://t.me/efsanelions')]
                      ),
                    link_preview=False
                    )
  
@client.on(events.NewMessage(pattern="^/bot$"))
async def bot(event):
  snehabhitext = "**ÖZEL BOT YAPIMI İÇİN**"
  await event.reply(snehabhitext,
                    buttons=(
                      [Button.url('DESTEK KANALIMIZ', 'http://t.me/RapidDestek')],
                      [Button.url('DEVELOPER', 'http://t.me/Efsanelions')]
                      ),
                    link_preview=False
                    )
  
#RAPID DESTEK @RapidDestek

#DEVELOPER @EfsaneLions

@client.on(events.NewMessage(pattern="^/all ?(.*)"))
async def mentionall(event):
  global moment_worker
  if event.is_private:
    return await event.reply("BENİ BİR GRUBA EKLE!")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.reply("SADECE YÖNETİCİLER KULLANABİLİR.")
    
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.reply("𝙸 𝙲𝙰𝙽'𝚃 𝙼𝙴𝙽𝚃𝙸𝙾𝙽 𝙼𝙴𝙼𝙱𝙴𝚁𝚂 𝙵𝙾𝚁 𝙾𝙻𝙳 𝙿𝙾𝚂𝚃")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.reply("BANA BİR MESAJ VER. ÖRNEK: `/all GÜNAYDIN`")
  else:
    return await event.reply("MESAJ YANITLAYABİLİRSİNİZ!")
  if mode == "text_on_cmd":
    moment_worker.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await event.respond("𝔼𝕥𝕚𝕜𝕖𝕥𝕝𝕖𝕞𝕖 𝔻𝕦𝕣𝕕𝕦𝕣𝕦𝕝𝕕𝕦! 🟥")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
        
  if mode == "text_on_reply":
    moment_worker.append(event.chat_id)
    
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await event.reply("𝔼𝕥𝕚𝕜𝕖𝕥𝕝𝕖𝕞𝕖 𝔻𝕦𝕣𝕕𝕦𝕣𝕦𝕝𝕕𝕦! 🟥")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
        
print("RAPID T@G BOTUNU BAŞLATIN")
print("¯\_(ツ)_/¯ DEVELOPER @EfsaneLions")
client.run_until_disconnected()
