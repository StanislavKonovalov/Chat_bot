import requests

token = "5495417282:AAGFBUapgn1cxfGFfjE-8f2xWRNjFCpBiMs"
# https://api.telegram.org/bot5495417282:AAGFBUapgn1cxfGFfjE-8f2xWRNjFCpBiMs/getme
# res = requests.get()
root_url = "https://api.telegram.org/bot"
ok_codes = 200, 201, 202, 203, 204
last_updated_id = 0

res = requests.get(f"{root_url}{token}/getMe")
print(res.json())


def get_bot_info(token):
	url = f"{root_url}{token}/getme"
	res = requests.get(url)
	bot_info = res.json()
	return bot_info

def get_updates(token):
	url = f"{root_url}{token}/getUpdates"
	res = requests.get(url)
	if res.status_code in ok_codes:
		updates = res.json()
		return updates
	else:
		print(f"Request failed with status code: {res.status_code}")


updates = get_updates(token)
if len(updates["result"]) > 0:
	last_message = updates["result"][-1]
	last_message_text = last_message["message"]["text"]
else:
	"No messages"

last_user_name = updates["result"][-1]["message"]["from"]["first_name"]
last_user_id = updates["result"][-1]["message"]["from"]["id"]

print(last_message_text)
print(last_user_name)

def send_message(token, chat_id, text):
	url = f"{root_url}{token}/sendMessage"
	data = {
		"chat_id": chat_id,
		"text": text
	}
	re = requests.post(url=url, data=data)
	print(re)


"""def get_user_name(token):
	url = f"{root_url}{token}/getUpdates"
	res = requests.get(url)
	user_name = res.json()["result"][0]["message"]["from"]["first_name"]
	return user_name


user_name = get_user_name(token)"""


while True:
	updates = get_updates(token)
	messages = updates["result"]
	for message in messages:
		if message['update_id'] > last_updated_id:
			send_message(token, last_user_id, f"Hello, {last_user_name}")
			last_updated_id = message['update_id']



# send_message(token, last_user_id, f"Hello, {last_user}")
