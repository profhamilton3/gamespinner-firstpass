input.onButtonPressed(Button.A, function on_button_pressed_a() {
    for (let index = 0; index < 4; index++) {
        basic.showArrow(ArrowNames.North, S)
        basic.showArrow(ArrowNames.NorthEast, S)
        basic.showArrow(ArrowNames.East, S)
        basic.showArrow(ArrowNames.SouthEast, S)
        basic.showArrow(ArrowNames.South, S)
        basic.showArrow(ArrowNames.SouthWest, S)
        basic.showArrow(ArrowNames.West, S)
        basic.showArrow(ArrowNames.NorthWest, S)
    }
})
basic.showIcon(IconNames.Asleep)
let S = 150
