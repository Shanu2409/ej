import datetime
import telepot
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO
from time import sleep

red_led_pin, green_led_pin = 21, 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_led_pin, green_led_pin, GPIO.OUT)

now = datetime.datetime.now()


def action(msg):
    chat_id = msg["chat"]["id"]
    command = msg["text"]

    if command == "/hi":
        bot.sendMessage(chat_id, "Hi! MakerPro")
    elif command == "/time":
        bot.sendMessage(chat_id, f"Time: {now.hour}:{now.minute}:{now.second}")
    elif command == "/date":
        bot.sendMessage(chat_id, f"Date: {now.day}/{now.month}/{now.year}")
    elif command == "/red_1":
        bot.sendMessage(chat_id, "Red led is ON")
        GPIO.output(red_led_pin, True)
    elif command == "/red_0":
        bot.sendMessage(chat_id, "Red led is OFF")
        GPIO.output(red_led_pin, False)
    elif command == "/green_1":
        bot.sendMessage(chat_id, "Green led is ON")
        GPIO.output(green_led_pin, True)
    elif command == "/green_0":
        bot.sendMessage(chat_id, "Green led is OFF")
        GPIO.output(green_led_pin, False)


bot = telepot.Bot("YOUR_TELEGRAM_BOT_TOKEN")
MessageLoop(bot, action).run_as_thread()

while True:
    sleep(10)
