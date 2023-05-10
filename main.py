def on_button_pressed_a():
    for index in range(4):
        basic.show_arrow(ArrowNames.NORTH, S)
        basic.show_arrow(ArrowNames.NORTH_EAST, S)
        basic.show_arrow(ArrowNames.EAST, S)
        basic.show_arrow(ArrowNames.SOUTH_EAST, S)
        basic.show_arrow(ArrowNames.SOUTH, S)
        basic.show_arrow(ArrowNames.SOUTH_WEST, S)
        basic.show_arrow(ArrowNames.WEST, S)
        basic.show_arrow(ArrowNames.NORTH_WEST, S)
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.show_icon(IconNames.ASLEEP)
S = 150