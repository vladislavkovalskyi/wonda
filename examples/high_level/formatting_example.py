from wonda import Bot, Message, Token
from wonda.bot.rules import Command
from wonda.tools.text import ParseMode, html, markdown

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())


@bot.on.message(Command("markdown"))
async def markdown_formatting_handler(msg: Message) -> None:
    # Let's use Markdown to format our message.
    await msg.answer(
        # This text is perfectly valid and escaping it isn't mandatory.
        markdown.underline("This is an example of Markdown formatting:")
        + " "
        + markdown.bold(
            # You must escape the text if it contains
            # special characters like `*` or `_`. More details at
            # https://core.telegram.org/bots/api#markdownv2-style
            markdown.escape("This text is in bold and is also escaped. Wow!")
        )
        + " "
        + markdown.spoiler(markdown.escape("Oh no, a spoiler!")),
        parse_mode=ParseMode.MARKDOWN,
    )


@bot.on.message(Command("html"))
async def html_formatting_handler(msg: Message) -> None:
    # Let's use HTML to format our message.
    await msg.answer(
        # This text is perfectly valid and escaping it isn't mandatory.
        html.underline("HTML stands for Hyper Text Markup Language.")
        + " "
        + html.bold(
            # You may want to escape the text if it contains
            # special characters like `&`, `<` or `>`. More details at
            # https://core.telegram.org/bots/api#html-style
            html.escape(
                "The <html> tag represents the root of an HTML document. "
                "The <body> tag defines the document's content "
                "& the <head> element is a container for metadata."
            )
        ),
        parse_mode=ParseMode.HTML,
    )


@bot.on.message(Command("mention"))
async def mention_handler(msg: Message) -> None:
    await msg.answer(
        markdown.mention("Look who's mentioned in Markdown!", msg.from_.id),
        parse_mode=ParseMode.MARKDOWN,
    )
    await msg.answer(
        html.mention(
            "What a shame! You are mentioned again, this time in HTML!", msg.from_.id
        ),
        parse_mode=ParseMode.HTML,
    )


# Run loop > loop.run_forever() > with tasks created in loop_wrapper before.
# The main polling task for bot is bot.run_polling()
bot.run_forever()
