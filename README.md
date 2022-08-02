# micropython-ssd1306-easy-animator
## Setup
**If using Linux / Mac, use `python3` instead of `python`. Most commands here are on windows you may need to use the help functions of esptool.py to see the linux commands which should be simialr.**

1. Clone repo: `git clone https://github.com/seth-c-stenzel/micropython-ssd1306-easy-animator.git`
2. Create a new virtual env: `python -m venv env`
3. Activate env:
   1. Windows: `env\Scripts\activate`
   2. Linux/macOS: `source venv/bin/activate`
4. Install esptools: `python -m pip install esptool`
5. Erase the esp32: `esptool.py --chip esp32 --port com8 erase_flash`
6. Flash new MicroPython binary image to the esp32: `esptool.py --chip esp32 --port com8 --baud 460800 write_flash -z 0x1000 bin\esp32-20220618-v1.19.1.bin`
7. Install the RS-Thread MicroPython extension for VSCode.
8. In the bottom left, press the plug/connect buttom, and connect to correct com/device port. **This should give you REPL access**
9. Right click each file [root.py, delpbms.py, demo.py, ssd1306.py] and select the option `Download the file/folder to the device`.
10. Right click the `ani` folder and select the option `Download the file/folder to the device`.
11. In the REPL window, import the os module and then call the listdir function and confirm all files copied correctly:
```import os
os.listdir()```
