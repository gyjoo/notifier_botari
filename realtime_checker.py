import telegram
import id, notifier
import time

bot = telegram.Bot(token = id.my_token)

# Realtime Checker Function
def receiving():
    received_html = notifier.get_html_body()
    received_length = len(received_html)

    if received_length == id.original_length:
        print("아직 지갑 안 열렸네요")
    else:
        bot.sendMessage(chat_id = id.chat_id, text="@@@@@@@@@@@@@@@@@@@@  지갑 열렸습니다  @@@@@@@@@@@@@@@@@@@@")

    time.sleep(1)


while True:
    receiving()


# Original Length Checker
# received_html = notifier.get_html_body()
# received_length = len(received_html)
# print(received_length)
