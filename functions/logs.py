from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineQuery, Message

import config


__all__ = ('log', 'log_message', 'log_callback', 'log_inline')


async def log(client: Client, text: str, no_log_in_test: bool = False, disable_notification: bool = True):
    """Sends log to the log channel."""

    if no_log_in_test and config.TEST_MODE:
        return

    await client.send_message(config.LOGCHANNEL, text, disable_notification=disable_notification)


async def log_message(client: Client, message: Message):
    """Sends message log to the log channel."""

    if config.TEST_MODE:
        return

    username = message.from_user.username
    display_name = f'@{username}' if username is not None else f'{message.from_user.mention} (username hidden)'

    text = (
        f"✍️ User: {display_name}\n"
        f"ID: {message.from_user.id}\n"
        f"Language: {message.from_user.language_code}\n"
        f"Private message: {message.text}"
    )
    await client.send_message(config.LOGCHANNEL, text, disable_notification=True)


async def log_callback(client: Client, callback_query: CallbackQuery):
    """Sends callback log to the log channel."""

    if config.TEST_MODE:
        return

    username = callback_query.from_user.username
    display_name = f'@{username}' if username is not None else f'{callback_query.from_user.mention} (username hidden)'

    text = (
        f"✍️ User: {display_name}\n"
        f"ID: {callback_query.from_user.id}\n"
        f"Language: {callback_query.from_user.language_code}\n"
        f"Callback query: {callback_query.data}"
    )
    await client.send_message(config.LOGCHANNEL, text, disable_notification=True)


async def log_inline(client: Client, inline_query: InlineQuery):
    """Sends an inline query to the log channel."""

    if config.TEST_MODE:
        return

    username = inline_query.from_user.username
    display_name = f'@{username}' if username is not None else f'{inline_query.from_user.mention} (username hidden)'

    text = (
        f"🛰 User: {display_name}\n"
        f"ID: {inline_query.from_user.id}\n"
        f"Language: {inline_query.from_user.language_code}\n"
        f"Inline query: {inline_query.query}"
    )
    await client.send_message(config.LOGCHANNEL, text, disable_notification=True)
