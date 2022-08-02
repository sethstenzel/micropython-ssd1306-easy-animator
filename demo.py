from display_pbm import *
import time

hw_pin_scl, hw_pin_sda = (4 , 5)
i2c, lcd = setup_display(hw_pin_scl, hw_pin_sda)

# SINGLE IMAGE DEMO
display_image(lcd, "./img", "ash-pikachu.pbm", False)
time.sleep(2)

# SLIDE SHOW DEMO
display_slide_show(lcd, "./img", ["mario-kart.pbm", "pokemon.pbm", "tetris.pbm", "three-starters.pbm"], False, 2, 1)

# ANIMATION DEMO
display_animation(lcd, "./ani/mario_dance", False, 1/15, 23, 6, 1)
display_animation(lcd, "./ani/streetf", False, 1/30, 38, 15, 1)
display_animation(lcd, "./ani/yoshi_walk", False, 1/30,  5, 10, 1)


