from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMembersFilter

import env
import config


@Client.on_message(filters.command("ban") & filters.chat(config.INCS2CHAT))
async def ban(client: Client, message: Message):
    chat = await client.get_chat(config.INCS2CHAT)

    admins = chat.get_members(filter=ChatMembersFilter.ADMINISTRATORS)
    admins = {admin.user.id async for admin in admins}

    if message.from_user.id not in admins:
        await message.reply("Эта команда недоступна, Вы не являетесь разработчиком Valve.")

    if message.reply_to_message:
        og_msg = message.reply_to_message
        await chat.ban_member(og_msg.from_user.id)
        await message.reply(f"{og_msg.from_user.first_name} получил(а) VAC бан.")


@Client.on_message(filters.command("unban") & filters.chat(config.INCS2CHAT))
async def unban(client: Client, message: Message):
    chat = await client.get_chat(config.INCS2CHAT)
    admins = chat.get_members(filter=ChatMembersFilter.ADMINISTRATORS)
    admins = {admin.user.id async for admin in admins}

    if message.from_user.id not in admins:
        await message.reply("Эта команда недоступна, Вы не являетесь разработчиком Valve.")

    if message.reply_to_message:
        og_msg = message.reply_to_message
        await chat.unban_member(og_msg.from_user.id)
        await message.reply(f"VAC бан {og_msg.from_user.first_name} был удалён.")


@Client.on_message(filters.channel & filters.text)
async def cs_l10n_update(client: Client, message: Message):
    if message.from_user.id == 777000 \
        and message.forward_from_chat.id == config.INCS2CHANNEL \
            and "Обновлены файлы локализации" in message.text:
        await message.reply_sticker("CAACAgIAAxkBAAID-l_9tlLJhZQSgqs"
                                    "MUAvLv0r8qhxSAAIKAwAC-p_xGJ-m4XRqvoOzHgQ")
