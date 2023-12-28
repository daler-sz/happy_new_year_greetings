import asyncio
import configparser
import logging
from dataclasses import dataclass

from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message,
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from greetings_generation import generate_greeting, GREETINGS

dp = Dispatcher()


@dataclass
class Config:
    token: str


def load_config() -> Config:
    config = configparser.ConfigParser()
    config.read("config.ini")

    return Config(
        token=config["bot"]["token"],
    )


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Привет! Введи /generate и я "
        f"сгенерирую новогоднее поздравление для твоих друзей "
        f"(видимо, не особо близких). "
        f"Или воспользуйся inline режимом.",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Inline mode", switch_inline_query=""
                    )
                ]
            ]
        ),
    )


@dp.message(Command("generate"))
async def command_generate_handler(message: Message) -> None:
    await message.answer(generate_greeting(GREETINGS))


@dp.inline_query()
async def inline_query_handler(query: InlineQuery) -> None:
    results = []

    for i in range(5):
        greeting = generate_greeting(GREETINGS)

        results.append(
            InlineQueryResultArticle(
                id=str(i),
                title="Новогоднее поздравление для твоих друзей",
                description=greeting,
                input_message_content=InputTextMessageContent(
                    message_text=greeting
                ),
            )
        )

    await query.answer(results=results)


async def main() -> None:
    config = load_config()

    bot = Bot(config.token, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
