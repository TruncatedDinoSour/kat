#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""kat bot"""

import asyncio
import hashlib
import mimetypes
import os
import random
from typing import Any

import aiofiles
import aiohttp
import simplematrixbotlib as botlib  # type: ignore

config: botlib.Config = botlib.Config()

config.encryption_enabled = True  # type: ignore
config.emoji_verify = True  # type: ignore
config.ignore_unverified_devices = False  # type: ignore
config.store_path = "./crypto_store/"  # type: ignore

bot: botlib.Bot = botlib.Bot(
    botlib.Creds(
        os.environ["KAT_HOMESERVER"],
        os.environ["KAT_USERNAME"],
        os.environ["KAT_PASSWORD"],
    ),
    config,
)


@bot.listener.on_message_event  # type: ignore
async def kat(room: Any, message: Any) -> None:
    """sets a random cat on a specific keyword"""

    if message.body.lower() in (
        "cat",
        "kat",
        "katze",
        "die katze",
        "kato",
        "cato",
        "cats",
        "katė",
        "katinas",
        "kačiukas",
        "🐈️",
        "😹",
        "😸",
        "😼",
        "😿",
        "🙀",
        "😺",
        "😽",
        "😾",
        "😻",
        "🐱",
        "🐈️",
        "🐈‍⬛",
        "/bin/cat",
        "/usr/bin/cat",
        "el gato",
        "meow",
        "purr",
        "mrrp",
        "mreow",
        "mrew",
        "mew",
        "nya",
        "1984",
        "hiss",
    ):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://cataas.com/cat") as response:
                content: bytes = await response.content.read()
                file: str = (
                    f"{hashlib.sha256(content).hexdigest()}{mimetypes.guess_extension(response.headers['Content-Type'])}"
                )

                async with aiofiles.open(
                    file,
                    "wb",
                ) as fp:
                    await fp.write(content)

                await bot.api.send_image_message(  # type: ignore
                    room.room_id,
                    file,
                )

                await asyncio.to_thread(os.remove, file)


def main() -> int:
    """entry/main function"""

    bot.run()

    return 0


if __name__ == "__main__":
    assert main.__annotations__.get("return") is int, "main() should return an integer"
    raise SystemExit(main())
