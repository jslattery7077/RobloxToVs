# RobloxToVS
Tool to convert local existing Roblox games into Rojo to keep sync in a full circle

# Using RobloxToVS
## Setup
Before you can use RobloxToVS, you need the following:

- Vs Code
- Python with pip
- Roblox Studio

## Porting Online Game
Before you can port your game into Vs Code, you need a place/model file. If you have an existing game that isn't exported:

- Go to studio, click on any place, and then click on File -> Save to file as.

- Note where you have that file.
### Steps to port the game:
1. Clone the repo to a folder
2. Launch a terminal in that folder.
3. Open folder in Vs Code.
4. Run `pip install -r requirements.txt` to install the dependencies, either through vs code terminal or cmd.
5. Install the followin extensions to vs code:
    - https://marketplace.visualstudio.com/items?itemName=Nightrains.robloxlsp - Vs Code Roblox LSP Extension, for intellisense in vs code.
    - https://marketplace.visualstudio.com/items?itemName=rojo-rbx.rojo - rojo extension for vs code.
    - https://marketplace.visualstudio.com/items?itemName=evaera.roblox-api-explorer - Roblox API Explorer.
6. Move that .rbxl file you saved earlier to the folder Scripts, and rename it to project.rbxl.
8. Double click to launch project.rbxl.
9. Install the following plugins.
    - https://www.roblox.com/library/123456789/RobloxToVS - RobloxToVS plugin.
    - https://create.roblox.com/marketplace/asset/6415005344/Rojo-7 - Rojo plugin.
10. Now, run watch.py by either double clicking it or running `python watch.py` in the terminal. - if step 4 was done in vs code you must run thoruogh the terminal.
11. A new window will open and show the rojo server output.
12. Add a new script into the game, and hit ctrl + s to save it to the file system and and wala, you have your first script in Vs Code!

Congratulations, you successfully synced Roblox Studio with Vs Code!

## For latest versions of the tools:
For the latest version of rblx-to-rojo: https://github.com/rojo-rbx/rbxlx-to-rojo/releases - Scripts/rbxlx-to-rojo.exe
For the latest version of rojo: https://github.com/rojo-rbx/rojo/releases - Scripts/rojo.exe


