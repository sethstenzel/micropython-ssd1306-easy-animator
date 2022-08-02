from display_pbm import *
import time

hw_pin_scl, hw_pin_sda = (4, 5)
i2c, lcd = setup_display(hw_pin_scl, hw_pin_sda)

while True:
    # SINGLE IMAGE DEMO
    display_image(lcd, "./img", "esp32+ssd1306.pbm", True)
    time.sleep(1)
    display_image(lcd, "./img", "ash-pikachu.pbm", True)
    time.sleep(2)

    # SLIDE SHOW DEMO
    display_slide_show(
        lcd=lcd,
        dir="./img",
        files=[
            "mario-kart.pbm",
            "pokemon.pbm",
            "tetris.pbm",
            "three-starters.pbm",
        ],
        inverted=True,
        disptime=1500,
        loops=0,
    )

    # ANIMATION DEMO
    display_animation(
        lcd=lcd,
        dir="./ani/mario_dance",
        inverted=True,
        disptime=66,
        framecount=23,
        duration=23,
        startframe=1,
        reverse=False,
    )
    display_animation(
        lcd=lcd,
        dir="./ani/streetf",
        inverted=True,
        disptime=33,
        framecount=38,
        duration=38,
        startframe=1,
        reverse=False,
    )
    yoshi_count = 5
    while yoshi_count:
        yoshi_count -= 1
        display_animation(
            lcd=lcd,
            dir="./ani/yoshi_walk",
            inverted=True,
            disptime=33,
            framecount=10,
            duration=10,
            startframe=1,
            reverse=False,
        )

    ld_count = 3
    while ld_count:
        display_animation(
            lcd=lcd,
            dir="./ani/light_to_dark",
            inverted=True,
            disptime=33,
            framecount=23,
            duration=23,
            startframe=1,
            reverse=False,
        )
        display_animation(
            lcd=lcd,
            dir="./ani/light_to_dark",
            inverted=True,
            disptime=33,
            framecount=23,
            duration=23,
            startframe=1,
            reverse=True,
        )
