import amino
from concurrent.futures import ThreadPoolExecutor
print(
"""\u001b[33m
Script by zeviel
Github : https://github.com/zevieli
╋┏┓┏━━━┳━┳━┳━━┳━┳┳┓┏┳━━┳━━┳━━┳┳┳┳┳━┳━┳━━┳━┳┓┏┳━┳━┓
┏┛┃┃┏━┓┃┃┃┃┣┃┃┫┃┃┣┓┏╋━━┣┓┏┻┃┃┫┏┫┏┫┳┫╋┣━━┃╋┣┓┏┫┃┃┃┃
┗┓┃┗┛┏┛┃┃┃┃┣┃┃┫┃┃┣┛┗┫━━┫┃┃┏┃┃┫┗┫┗┫┻┫┓┫━━┫┏╋┛┗┫┃┃┃┃
╋┃┃┏┓┗┓┣┻━┻┻━━┻┻━┻┛┗┻━━┛┗┛┗━━┻┻┻┻┻━┻┻┻━━┻┛┗┛┗┻┻━┻┛
┏┛┗┫┗━┛┃
"""
)
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
clients = client.sub_clients(size=100)
for x, name in enumerate(clients.name, 1):
	print(f"{x}.{name}")
com_id = clients.comId[int(input("-- Select the community::: ")) - 1]
sub_client = amino.SubClient(comId=com_id, profile=client.profile)
chats = sub_client.get_chat_threads(size=100)
for z, title in enumerate(chats.title, 1):
	print(f"{z}.{title}")
chat_id = chats.chatId[int(input("-- Select the chat::: ")) - 1]
sticker_id = input("-- StickerID::: ")
tasks_count = int(input("-- Number of tasks::: "))
print("-- Started spamming...")

while True:
	with ThreadPoolExecutor(max_workers=100) as executor:
		[executor.submit(sub_client.send_message, chatId=chat_id, stickerId=sticker_id) for _ in range(tasks_count)]
