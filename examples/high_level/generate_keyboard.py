from wonda.tools.keyboard import Button, Keyboard

# The simplest way of generating keyboard is using non-builder interface.
# Use <.add(Button(...))> to add button to the last row, then <.row()> to add row.
KEYBOARD_STANDARD = Keyboard(resize_keyboard=True)
KEYBOARD_STANDARD.add(Button(text="Button 1"))
KEYBOARD_STANDARD.add(Button(text="Button 2"))
KEYBOARD_STANDARD.row()
KEYBOARD_STANDARD.add(Button(text="Button 3"))

# <.add()> and <.row()> methods return the instance of Keyboard,
# so you can use it as a builder
KEYBOARD_WITH_BUILDER = (
    Keyboard(resize_keyboard=True)
    .add(Button(text="Button 1"))
    .add(Button(text="Button 2"))
    .row()
    .add(Button(text="Button 3"))
)

# Check that the two keyboards are the same.
assert KEYBOARD_STANDARD == KEYBOARD_WITH_BUILDER
