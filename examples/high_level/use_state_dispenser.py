from wonda import Bot, BaseStateGroup, Message, Token
from wonda.bot.rules import Command, State, Text
from wonda.tools.keyboard import Button, Keyboard

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())

# Create a new state group
# describing the flow of the conversation.
class MenuState(BaseStateGroup):
    START, BUY = "start", "buy"


MENU_KEYBOARD = (
    Keyboard(resize_keyboard=True)
    .add(Button(text="About us"))
    .add(Button(text="Buy a drink"))
)
BEVERAGE_KEYBOARD = (
    Keyboard(one_time_keyboard=True, resize_keyboard=True)
    .add(Button(text="Espresso"))
    .add(Button(text="Cappuccino"))
)


@bot.on.message(Command("start") | Command("return"))
async def menu_handler(msg: Message) -> None:
    await msg.answer(
        "Welcome to our coffee house! What can we make for you today?",
        reply_markup=MENU_KEYBOARD,
    )
    await bot.state_dispenser.set(msg.chat.id, MenuState.START)


@bot.on.message(Text("about us", ignore_case=True) & State(MenuState.START))
async def about_us_handler(msg: Message) -> None:
    await msg.answer(
        "Our company was founded all the way back into seventies. "
        "We were inspired to sell high-quality coffee and other goods. "
        "Now we serve espresso, latte, juices and drinks, both hot and cold.\n\n"
        "Thank you for attention! You can now /return to menu. "
    )


@bot.on.message(
    Text("buy a drink", ignore_case=True) & State(MenuState.START),
)
async def buy_drink_handler(msg: Message) -> None:
    await msg.answer(
        "We sure have 'em in stock! Choose a beverage "
        "or just /return to menu if you don't want anything.",
        reply_markup=BEVERAGE_KEYBOARD,
    )
    await bot.state_dispenser.set(msg.chat.id, MenuState.BUY)


@bot.on.message(
    Text(["cappuccino", "espresso"], ignore_case=True), State(MenuState.BUY)
)
async def choose_beverage_handler(msg: Message) -> None:
    await msg.answer(
        f"Thanks! The order for {msg.text} is now placed. "
        "Please /return to menu and wait a couple of minutes."
    )


# Run loop > loop.run_forever() > with tasks created in loop_wrapper before.
# The main polling task for bot is bot.run_polling()
bot.run_forever()
