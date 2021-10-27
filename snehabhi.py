#SNEHABHI USERTAGGER BOT
#I LOVE YOU SNEHU😘

import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
  level=logging.INFO,
  format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

moment_worker = []

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global moment_worker
  moment_worker.remove(event.chat_id)
  
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("𝙷𝙴𝙻𝙻𝙾 𝙸'𝙼 𝚂𝙽𝙴𝙷𝙰𝙱𝙷𝙸 𝚄𝚂𝙴𝚁𝚃𝙰𝙶𝙶𝙴𝚁 𝙱𝙾𝚃./n𝙽𝙴𝙴𝙳 𝙷𝙴𝙻𝙿 /help",
                    buttons=(
                      [Button.url('🙃 𝙶𝚁𝙾𝚄𝙿 𝙼𝙴 𝙳𝙰𝙻 𝙳𝙴 𝙳𝙴𝙺𝙷 𝙼𝚃 🥺✨', 'https://t.me/SNEHABHI_TAGGERBOT?startgroup=true')],
                      [Button.url('𝙵𝙾𝚁 𝙰𝙽𝚈 𝙸𝚂𝚂𝚄𝙴 𝙹𝙾𝙸𝙽 𝙾𝚄𝚁 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿', 'https://t.me/SNEHABHI_SERVER')],
                      [Button.url('𝙵𝙾𝚁 𝙻𝙰𝚃𝙴𝚂𝚃 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 𝙹𝙾𝙸𝙽 𝙾𝚄𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻', 'https://t.me/SNEHABHI_UPDATES')]
                      ),
                    link_preview=False
                    )

#𝚆𝙰𝙰𝙷 𝙱𝙷𝙰𝙸𝙼𝚈𝙰 𝙵𝚄𝙻𝙻 𝙸𝙼𝙶𝙽𝙾𝚁𝙴𝙱𝙰𝚉𝙸

#𝙲𝚁𝙴𝙳𝙸𝚃 𝙳𝙴 𝙳𝙴𝙽𝙰 𝚆𝙰𝚁𝙽𝙰 𝙼𝙰 𝙲𝙷𝙾𝙳 𝙳𝙴𝙽𝙶𝙴

@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def help(event):
  helptext = "***𝚂𝙽𝙴𝙷𝙰𝙱𝙷𝙸 𝚄𝚂𝙴𝚁𝚃𝙰𝙶𝙶𝙴𝚁 𝙱𝙾𝚃'𝚂 𝙷𝙴𝙻𝙿 𝙼𝙴𝙽𝚄**\n\nCommand: /tag \n 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚆𝙸𝚃𝙷 𝚃𝙴𝚇𝚃 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝚃𝙴𝙻𝙻 𝙾𝚃𝙷𝙴𝚁𝚂. \n`𝙴𝚇𝙰𝙼𝙿𝙻𝙴: /all 𝙶𝙾𝙾𝙳 𝙼𝙾𝚁𝙽𝙸𝙽𝙶!` \n𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝙰𝚂 𝙰𝙽 𝙰𝙽𝚂𝚆𝙴𝚁. 𝙰𝙽𝚈 𝙼𝚂𝙶 𝙱𝙾𝚃 𝚆𝙸𝙻𝙻 𝚃𝙰𝙶 𝚄𝚂𝙴𝚁𝚂 𝚃𝙾 𝚁𝙴𝙿𝙻𝙸𝙴𝙳 𝙼𝚂𝙶"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('🙃 𝙶𝚁𝙾𝚄𝙿 𝙼𝙴 𝙳𝙰𝙻 𝙳𝙴 𝙳𝙴𝙺𝙷 𝙼𝚃 🥺✨', 'https://t.me/SNEHABHI_TAGGERBOT?startgroup=true')],
                      [Button.url('𝙵𝙾𝚁 𝙰𝙽𝚈 𝙸𝚂𝚂𝚄𝙴 𝙹𝙾𝙸𝙽 𝙾𝚄𝚁 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿', 'https://t.me/SNEHABHI_SERVER')],
                      [Button.url('𝙵𝙾𝚁 𝙻𝙰𝚃𝙴𝚂𝚃 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 𝙹𝙾𝙸𝙽 𝙾𝚄𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻', 'https://t.me/SNEHABHI_UPDATES')]
                      ),
                    link_preview=False
                    )
  
                    
                      
