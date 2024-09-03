# Telegram Message Forwarder

A Python script that automates the process of forwarding messages from a source Telegram channel to multiple target Telegram chats. The script uses the Telethon library to interact with Telegram's API and includes features for handling errors and delays to ensure smooth operation.

## Features

- **Message Forwarding:** Automatically forwards the latest message from a specified source channel to multiple target chats.
- **Dynamic Chat Resolution:** Retrieves chat IDs dynamically from provided Telegram links.
- **Randomized Delays:** Introduces random delays between message forwarding to mimic natural behavior and avoid rate limits.
- **Error Handling:** Robust error handling to skip chats where message forwarding fails and continue with the next available chat.
- **Interval Management:** Configurable interval to set the frequency of message retrieval and forwarding.

## Requirements

- Python 3.7+
- Telethon library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/saddope/Telegram-Message-Forwarder.git
    ```

2. Navigate to the project directory:
    ```sh
    cd Telegram-Message-Forwarder
    ```

3. Install the required dependencies:
    ```sh
    pip install telethon
    ```

## Configuration

Open `run.py` and update the script with your Telegram API credentials, source channel link, and target chat links.

## Usage

Run the script with:
```sh
python run.py
