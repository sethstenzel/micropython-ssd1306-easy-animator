# micropython-ssd1306-easy-animator
## Setup
**If using Linux / Mac, use `python3` instead of `python`. Most commands here are on windows you may need to use the help functions of esptool.py to see the linux commands which should be simialr.**

1. Clone repo: `git clone https://github.com/seth-c-stenzel/micropython-ssd1306-easy-animator.git`
2. Create a new virtual env: `python -m venv env`
3. Activate env:
   - Windows: `env\Scripts\activate`
   - Linux/macOS: `source venv/bin/activate`
4. Install esptools: `python -m pip install esptool`
5. Install ampy: `python -m pip install adafruit-ampy`
6. Erase the esp32: `esptool.py --chip esp32 --port com8 erase_flash`
7. Flash new MicroPython binary image to the esp32: `esptool.py --chip esp32 --port com8 --baud 460800 write_flash -z 0x1000 bin\esp32-20220618-v1.19.1.bin`
8. Send project files with ampy:
   - `ampy.exe -p COM8 -b 115200 -d 0.75 put demo.py`, you will need to do each file individually.
   - You can also use the expirimental `sync_to_device.py` to sync multiple files and directories.
9.  You can verify files on the device with the command: `ampy.exe -p COM8 -b 115200 -d 0.75 ls`
   - To view the contents of a folder, list the folder after the `ls` command: `ampy.exe -p COM8 -b 115200 -d 0.75 ls ani/streef`
