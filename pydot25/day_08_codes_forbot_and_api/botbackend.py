#pip install botogram
import botogram
from datetime import datetime
from util import  get_pron_for_word
TOKEN = "YOUR BOT TOKEN"

bot = botogram.create(TOKEN)

@bot.command("hello")
def hello_command(chat, message, args):
    """
    Say hello to the world!
    """
    chat.send("Hello world")

@bot.command("time")
def time_command(chat, message, args):
    """
    Gives you the current time...
    """
    resp = str(datetime.now())
    chat.send(  resp )

@bot.command("pron")
def pron_command(chat, message, args):
    """
    Gives you the pron for a word...
    """
    chat.send("Please wait.....")
    urls = get_pron_for_word(args[0])
    for u in urls: 
        chat.send_audio(  url=u )
    chat.send("Done...")

@bot.command("calculator")
def calculator_command(chat, message, args):
    """
    simple calculator
    """
    print(args)

    if len(args) != 3:
        chat.send("Usage: /calculator <?> <> <>")
        return

    a , op, b = args #["10", "+" , "20"]
    expr = f"{a} {op} {b}"
    res = eval(expr)
    resp = f"{expr} = {res}"
    chat.send(resp)


if __name__ == "__main__":
    bot.run()