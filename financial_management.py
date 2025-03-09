from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Hàm xử lý lệnh /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Đây là bot tính toán tài chính')

async def handleMessage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return "Done"


# Hàm chính để chạy bot
def main():
    # Token bot từ BotFather
    token = 'Day la token cua toi'

    # Tạo ứng dụng (Application) mới với token của bot
    application = Application.builder().token(token).build()

    # Thêm lệnh /start vào bot
    application.add_handler(CommandHandler('start', start))

    # Thêm MessageHandler để xử lý các tin nhắn văn bản
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handleMessage))

    # Bắt đầu bot
    application.run_polling()

if __name__ == '__main__':
    main()
