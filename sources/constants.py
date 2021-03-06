# -*- coding: utf-8 -*-

####################################################################################################

### Imported modules ###

from os import path

####################################################################################################

### Constants ###

# Actual constants.py full path directory name
SCRIPT_PATH = path.dirname(path.realpath(__file__))


# General Bots Parameters
CONST = {

    # Bot Token (get it from @BotFather) "XXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    "TOKEN": "XXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",

    # Languages texts files directory path
    "LANG_DIR": SCRIPT_PATH + "/language",

    # Chats directory path
    "CHATS_DIR": SCRIPT_PATH + "/data/chats",

    # Directory where create/generate temporary captchas
    "CAPTCHAS_DIR": SCRIPT_PATH + "/data/captchas",

    # Chat configurations JSON files
    "F_CONF": "configs.json",

    # Private chat valid captcha time in minutes
    "VALID_CAPTCHA_TIME" : 10,

    # Initial trigger char
    "INIT_TRIGGER_CHAR" : "#",

    # Initial chat title at Bot start
    "INIT_TITLE": "Unknown Chat",

    # Initial chat link at Bot start
    "INIT_LINK": "Unknown",

    # Initial language at Bot start
    "INIT_LANG": "EN",

    # Initial enable/disable status at Bot start
    "INIT_ENABLE": True,

    # Initial welcome message
    "INIT_WELCOME_MSG" : "Welcome {1}!\n\nUsername: {0}\nUser-ID: {2}",

    # Initial captcha solve time (in minutes)
    "INIT_CAPTCHA_TIME_MIN": 5,

    # Initial captcha difficult level
    "INIT_CAPTCHA_DIFFICULTY_LEVEL": 2,

    # Initial captcha characters mode (nums, hex or ascci)
    "INIT_CAPTCHA_CHARS_MODE": "nums",

    # Initial new users just allow to send text messages
    "INIT_RESTRICT_NON_TEXT_MSG": False,

    # Default time (in mins) to remove self-destruct sent messages from the Bot
    "T_DEL_MSG": 5,

    # Auto-remove custom welcome message timeout
    "T_DEL_WELCOME_MSG": 5,

    # Custom Welcome message max length
    "MAX_WELCOME_MSG_LENGTH": 3968,

    # Maximum number of users ID allowed in each chat ignore list
    "IGNORE_LIST_MAX_ID": 100,

    # Command don't allow in private chat text (just english due in private chats we 
    # don't have language configuration
    "CMD_NOT_ALLOW_PRIVATE": "Can't use this command in the current chat.",

    # IANA Top-Level-Domain List (https://data.iana.org/TLD/tlds-alpha-by-domain.txt)
    "F_TLDS": "tlds-alpha-by-domain.txt",

    # Regular expression to detect URLs in a string based in TLD domains
    "REGEX_URLS": r"((?<=[^a-zA-Z0-9])*(?:https\:\/\/|[a-zA-Z0-9]{{1,}}\.{{1}}|\b)" \
        r"(?:\w{{1,}}\.{{1}}){{1,5}}(?:{})\b/?(?!@))",

    # List string of supported languages commands shows in invalid language set
    "SUPPORTED_LANGS_CMDS": \
        "\nEnglish / English\n/language en\n",

    # Orginal Bot developer
    "ORG_DEVELOPER": "@JoseTLG",

    # Bot developer
    "DEVELOPER": "@v_1nc",

    # Bot code repository
    "REPOSITORY": "https://github.com/v1nc/butter_bot",

    # Developer Paypal address
    "DEV_PAYPAL": "https://www.paypal.me/josrios",

    # Developer Bitcoin address
    "DEV_BTC": "3N9wf3FunR6YNXonquBeWammaBZVzTXTyR",

    # Bot version
    "VERSION": "0.2 (12/05/2020)",

    #Bot owner(hoster)
    "OWNER": "294121217",

    #Bot owner(hoster) telegram username
    "OWNER_NAME": "v_1nc"
}


# Supported languages list
TEXT = {
    "EN": None, # English
}
