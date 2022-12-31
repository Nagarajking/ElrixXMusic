import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQBDs6xBrEi1fBwJXQFuN6DYQB8vVza7lPzjLiQ70_cwjg3MjU4d1mPb8DiHEjOs4Zbpy3Ty5RWHOL6PMXekcBjLeB1MxM_ib6f9vPosGllKVhubnsNT67FbbcgwNuQSlyZgim1PY5_nm-2qTxHATCW4CgWqzt_NErplRmetDa8vJ_d43ycVobOiDZx08iDVgoxljjfAddz9FwECZUKOSqbV3RAhk8JFj4cJGoONytuxyfBP5E10AEhuvyZYiGsCqhGQTWkylgXCdU_JNGTNU-tEFGpbNMgIoxhsWWgdRO_HsppVj8u0-HSqZHJHjX7KPJfe8ofbs3ru5VbWzxUuk84UVHsUiQA")
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
