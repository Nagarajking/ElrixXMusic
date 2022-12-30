import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQDAvaxt8-WR1nh6abaKTltCO4pXbxtwRysf2WPHWkS6UBaNcysJaXwP08CWssjnfUl8i9Ku8hcWWiPFdX6DYMd5ba9obDv9lsMlMyfwMegZ6V90ga8Zb3s-m6J6KPky41dt7T0mWfiBTi0Shrsr4MJn1FpAHDvNSUXdYk8pw3zvZhKH_MyMjt3NzfI3VausA4SasXuiUMJodlHLcqJBiBEYnNfmY48IwKONkd8xa2896VIXoUV_YTReyQ0TqFtJb00sFb4FP8TxmoOGnY61BePX3Rm6YhRZZEKevCiCNghDIAWrFo5Df9SLzeM6Qb79SuUbpUu3n_ZraVUqiNCMK4RGAAAAAFR7FIkA")
BOT_TOKEN = getenv("2084060024:AAG2qH4BL9PXPKFnvmuIxwDjcKFJG-jLXEQ")
BOT_NAME = getenv("BOT_NAME", "ElrixXMusic")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/ccdb7dd3392bc90248472.jpg")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/257c2b28860112a84d985.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/257c2b28860112a84d985.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/257c2b28860112a84d985.jpg")
admins = {}
API_ID = int(getenv("6246021"))
API_HASH = getenv("112a701ebaf8995ce35ba7ae4433eb4b")
BOT_USERNAME = getenv("BOT_USERNAME", "Phoenix_vcsong_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Jaihindupuramking")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Dramaa_Club")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Sanki_BOTs")
OWNER_NAME = getenv("OWNER_NAME", "Jaihindupuramking") # isi dengan username kamu tanpa simbol @
DEV_NAME = getenv("DEV_NAME", "Jaihindupuramking")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("1417352329").split()))
