import db_bot
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler

f = open('users.txt','r+')
user_list=set([line[:-1] for line in f])




async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_list.add(update.effective_user.username)
    f.write(update.effective_user.username+'\n')
    await update.message.reply_text(f"Привет {update.effective_user.username}! Чтобы добавиться в команду набери /team <название команды>")

async def nums(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    buf='\n'.join(user_list)
    await update.message.reply_text(f"Number of users - {len(user_list)} Users:\n{buf}")

app = ApplicationBuilder().token("").build()

app.add_handler(CommandHandler(["hello","start"], hello))
app.add_handler(CommandHandler(["users"],nums))
app.add_handler(MessageHandler(filters.Chat(-4055857863)&filters.TEXT & (~filters.COMMAND),read))

app.run_polling()