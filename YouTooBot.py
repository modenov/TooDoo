import telebot
import random

token = "5466630722:AAEGzvWqPC7Ht_vJDyc5uYAJHkGWS6cJhiY"

bot = telebot.TeleBot(token)

youtoo_phrases = ["сам ты ", "да сам ты ", "чо? сам ты ", "бля сам ", "ахххахах сам ", "не понел! сам ",
                  "хыххх))0 сам давай "]
end_phrases = ["!", "!!", "!!!", "...", "!!!11!", ".", ")0", ")))))"]


@bot.message_handler(content_types=["text"])
def echo(message):
    text = random.choice(youtoo_phrases) + message.text.lower() + random.choice(end_phrases)
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
