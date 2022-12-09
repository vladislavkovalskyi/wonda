from wonda import API, TelegramAPIError, Token

# Make an API with a token from an environment variable.
api = API(Token.from_env())


async def main() -> None:
    try:
        await api.send_message(1, "Hi bestie!")
    except TelegramAPIError[400]:
        print("Oops, bad request.")
    except TelegramAPIError[401, 404]:
        print("Oops, unauthorized.")
    except TelegramAPIError as e:
        print(f"An error {e.code} occured.")


# Run an example function in the current event loop.
__import__("asyncio").get_event_loop().run_until_complete(main())
