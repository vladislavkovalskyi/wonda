from wonda.bot import Bot, Message, File, Token
from wonda.bot.rules import Command

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())


# Register a handler that will upload files.
@bot.on.message(Command("upload"))
async def upload_handler(msg: Message) -> None:
    # Upload a picture of fresh red apples.
    await msg.ctx_api.send_photo(
        chat_id=msg.chat.id,
        caption="Testing pictures!",
        # Open the file and pass its contents directly in `photo` param.
        photo=File.from_path("examples/high_level/assets/apples.webp"),
    )

    # Upload a recording of soothing melody.
    await msg.ctx_api.send_audio(
        chat_id=msg.chat.id,
        caption="Wonda for the win!",
        # Open the file and pass its contents directly in `audio` param.
        audio=File.from_path("examples/high_level/assets/music.mp3"),
    )

    # You can use raw bytes to create a file. Here we are downloading
    # some sample image from Lorem Picsum using built-in HTTP client.
    content = await msg.ctx_api.http_client.request_content("https://picsum.photos/500")

    # Now we are using the same file helper class, but it is being fed
    # an array of raw bytes. You can optionally set the name
    # for the resulting file.
    photo = File.from_bytes(content)

    # Now that we've created the file, let's send it.
    await msg.ctx_api.send_photo(
        caption="Look, mom! I pulled this photo from the Internet!",
        chat_id=msg.chat.id,
        photo=photo,
    )


# Run loop > loop.run_forever() > with tasks created in loop_wrapper before.
# The main polling task for bot is bot.run_polling()
bot.run_forever()
