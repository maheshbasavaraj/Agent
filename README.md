# Telegram to WhatsApp Notifier Agent

## Overview

This script automates the process of forwarding relevant job placement messages from a specific Telegram group to a WhatsApp contact. It continuously monitors the group for posts containing specific keywords (e.g., "Data Science") and instantly sends them as a notification to a predefined WhatsApp number.

This project is designed as a simple yet effective **Application-to-Application (A2A) integration framework**, where a custom agent listens to the Telegram application and triggers actions in the WhatsApp application.

## Architecture

The agent operates on a simple A2A model consisting of three logical components:
1.  **The Telegram Listener:** Connects to the Telegram group using a bot and listens for all new messages.
2.  **The Data Science Filter:** Analyzes each message to check if it contains predefined keywords relevant to the user.
3.  **The WhatsApp Notifier:** Takes the filtered message and sends it to the target WhatsApp number using browser automation.

---

## Setup Instructions

Follow these steps carefully to set up and run the agent.

### 1. Prerequisites

*   Python 3.6+ installed on your system.
*   A Telegram account.
*   A WhatsApp account with WhatsApp Web accessible on your default browser.

### 2. Install Dependencies

Install the necessary Python libraries by running the following command in your terminal:
```bash
pip install python-telegram-bot==13.7 pywhatkit
```

### 3. Configure the Telegram Bot

You need a Telegram bot to monitor the group.

1.  **Create a Bot:**
    *   On Telegram, start a chat with the official `@BotFather`.
    *   Send the `/newbot` command.
    *   Give your bot a name (e.g., "Placement Notifier") and a username (e.g., `MyPlacementNotifierBot`).
    *   `BotFather` will provide you with a **HTTP API Token**. Copy this token.

2.  **Add the Bot to Your Group:**
    *   You must have administrative rights in the target Telegram group.
    *   Add your newly created bot as a member of the group.

3.  **Get the Group Chat ID:**
    *   After adding the bot to the group, send a temporary message in the group like `/info`.
    *   Open your web browser and navigate to the following URL, replacing `<YourBotToken>` with the token you copied:
        ```
        https://api.telegram.org/bot<YourBotToken>/getUpdates
        ```
    *   Look for a recent "message" object in the response. Inside it, you will find a "chat" object containing an "id". This ID is a negative number (e.g., `-100123456789`). This is your **Group Chat ID**.

### 4. Configure the Script

Open the `telegram_to_whatsapp_agent.py` file and fill in your details in the configuration section at the top:

```python
# --- CONFIGURATION ---
# Replace these with your actual details
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # From BotFather
TELEGRAM_GROUP_ID = -100123456789  # Your negative Chat ID
WHATSAPP_CONTACT_NUMBER = "+1234567890"  # Your full WhatsApp number including country code

# Keywords to filter for. Add more as needed. Case-insensitive.
KEYWORDS = ["data science", "ds", "ai/ml", "machine learning", "data scientist"]
# --- END CONFIGURATION ---
```

---

## Running the Agent

1.  **Log in to WhatsApp Web:** Before starting, make sure you are logged into WhatsApp Web in your default browser.
2.  **Start the Script:** Open your terminal, navigate to the project directory, and run:
    ```bash
    python telegram_to_whatsapp_agent.py
    ```

The agent is now active. It will run in the background, and you will see log messages in the terminal when it detects and forwards a relevant post. To stop the agent, press `Ctrl+C` in the terminal.

---

## ⚠️ Important Warning

This script uses an unofficial method (`pywhatkit`) to automate WhatsApp messaging. This method works by controlling your web browser.

*   **Violation of Terms of Service:** Automating WhatsApp through unofficial means is against their Terms of Service.
*   **Risk of Being Banned:** There is a risk that your WhatsApp account could be temporarily or permanently banned for using such automation.
*   **Reliability:** The script's functionality depends on the WhatsApp Web interface, which can change at any time, potentially breaking the script.

**Use this script at your own risk.** For a production-grade, reliable solution, you must use the official **WhatsApp Business Platform API**.
