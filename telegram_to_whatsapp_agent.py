
import logging
import pywhatkit
from telegram.ext import Updater, MessageHandler, Filters
import datetime

# --- CONFIGURATION ---
# Replace these with your actual details
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # From BotFather
TELEGRAM_GROUP_ID = -100123456789  # Your negative Chat ID
WHATSAPP_CONTACT_NUMBER = "+1234567890"  # Your full WhatsApp number including country code

# Keywords to filter for. Add more as needed. Case-insensitive.
KEYWORDS = ["data science", "ds", "ai/ml", "machine learning", "data scientist"]
# --- END CONFIGURATION ---

# Set up logging to see what the bot is doing
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def send_to_whatsapp(message_text):
    """
    Agent 3: The WhatsApp Notifier.
    Sends the filtered message to the specified WhatsApp contact.
    """
    try:
        logger.info(f"Attempting to send message to {WHATSAPP_CONTACT_NUMBER}")
        
        # pywhatkit opens WhatsApp Web and sends the message.
        # A new tab will open in your browser.
        pywhatkit.sendwhatmsg_instantly(
            phone_no=WHATSAPP_CONTACT_NUMBER,
            message=message_text,
            wait_time=15,  # Time for WhatsApp Web to open and send
            tab_close=True # Close the tab after sending
        )
        logger.info("Successfully sent message to WhatsApp.")
    except Exception as e:
        logger.error(f"Failed to send WhatsApp message: {e}")
        logger.error("Please ensure you are logged into WhatsApp Web in your default browser.")

def message_handler(update, context):
    """
    Agent 1 & 2: The Telegram Listener and Data Science Filter.
    This function is called every time a new message is posted in the group.
    """
    # Ensure the message is from the correct group and has text
    if update.message.chat_id != TELEGRAM_GROUP_ID or not update.message.text:
        return

    message_text = update.message.text
    logger.info(f"Received message in group: {message_text[:50]}...")

    # Filter Logic: Check if any keyword is in the message (case-insensitive)
    if any(keyword in message_text.lower() for keyword in KEYWORDS):
        logger.info(f"Found relevant post with keywords: {[k for k in KEYWORDS if k in message_text.lower()]}")
        
        # Prepare the message to be sent to WhatsApp
        formatted_message = f"--- Automated Alert from Placement Group ---\n\n{message_text}"
        
        # Trigger the WhatsApp Notifier Agent
        send_to_whatsapp(formatted_message)

def main():
    "Starts the Telegram bot."
    # Create the Updater and pass it your bot's token.
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    logger.info("Bot started. Listening for messages...")

    # Register the message_handler to respond to all text messages
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    # IMPORTANT: Fill in your configuration details at the top of the script
    if "YOUR_TELEGRAM_BOT_TOKEN" in TELEGRAM_TOKEN:
        logger.error("Please fill in your Telegram Bot Token in the script.")
    elif "1234567890" in WHATSAPP_CONTACT_NUMBER:
        logger.error("Please fill in your WhatsApp contact number in the script.")
    elif TELEGRAM_GROUP_ID == -100123456789:
        logger.error("Please fill in your Telegram Group ID in the script.")
    else:
        main()
