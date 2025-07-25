from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import asyncio

# أدخل توكن البوت هنا
BOT_TOKEN = "6288532598:AAEf-5FT5mCBr6D5Pv1iHap3mp9CtB7FE10"

# مجموعة أذكار عشوائية
adhkar = [
    "أصبحنا وأصبح الملك لله، والحمد لله...",
    "اللهم بك أصبحنا، وبك أمسينا، وبك نحيا وبك نموت...",
    "اللهم أعني على ذكرك وشكرك وحسن عبادتك.",
    "اللهم باسمك أموت وأحيا.",
    "سبحان الله وبحمده، سبحان الله العظيم.",
    "لا إله إلا الله وحده لا شريك له، له الملك وله الحمد وهو على كل شيء قدير."
]

# تخزين المستخدمين المسجلين
registered_users = set()

# عند استخدام /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    registered_users.add(user_id)
    dhikr = random.choice(adhkar)
    await update.message.reply_text(f"🤍 ذكر اليوم:\n\n{dhikr}")

# إرسال أذكار دورية لكل المستخدمين
async def send_adhkar_periodically(app):
    while True:
        await asyncio.sleep(3600)  # كل ساعة
        for user_id in registered_users:
            dhikr = random.choice(adhkar)
            try:
                await app.bot.send_message(chat_id=user_id, text=f"🕊️ تذكير:\n\n{dhikr}")
            except:
                pass  # لو المستخدم حظر البوت

# إعداد التطبيق
app = ApplicationBuilder().token(BOT_TOKEN).build()

# أوامر البوت
app.add_handler(CommandHandler("start", start))

# بدء الإرسال الدوري
app.job_queue.run_once(lambda ctx: asyncio.create_task(send_adhkar_periodically(app)), 1)

if __name__ == "__main__":
    print("🚀 بوت تذكير يعمل...")
    app.run_polling()
