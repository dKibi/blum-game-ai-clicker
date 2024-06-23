## Blum Game AI Clicker
Clicker to auto-collect stars in game and farm $BLUM automatically. Blum AI clicker works on object detection (stars, bombs, freeze), it means that there is no any interaction with Blum code or API itself.

Script intended to help with large numbers of games, it is not effective to run it for 2–3 games, that's why I advise you to accumulate 50+ tickets and then run the script.

# Getting started / Prerequisites 
- Supported OS: Windows

Required:
- Python 3.10+ https://www.python.org/downloads/
- BlueStacks https://www.bluestacks.com/download.html
- Git https://git-scm.com/downloads

**Please read the instruction below completely before running the script.**

1. Clone the repository to your machine (git should be installed on your machine)
    ```shell
    git clone https://github.com/dKibi/blum-game-ai-clicker.git
    ```

2. Create a virtual environment and activate it (for Windows)
    ```shell
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install project dependencies (run in venv) -
    `pip install -r requirements`

4. Download and install BlueStacks - https://www.bluestacks.com/download.html

5. Launch BlueStacks Multi Instance Manager and create a profile with the name you can identify an account (for example, Blum1).
6. Launch created instance and make sure you have horizontal orientation. 
7. Inside launched Android instance - install, launch and log in into Telegram app where you will run Blum bot.
8. Launch Blum and go to home page (if you have any other windows like daily bonus, close them all). You should be at home page where visible **Play** button exists. The lower the resolution, the better the software performance, the main thing is that the resolution is not too small and the **Play** and **Play again** buttons are always visible. 
9. Launch the script from project root with `python main.py` or `python3 main.py`. Launch and stop the script (it can crash itself, it's okay).
10. Project config should be generated in `files/config.yaml`. Open config (for example, with Notepad++) and edit screen resolution and window name according to your host. 
11. Wait a few seconds, and you will be prompted to enter how many games should be played. Be careful and do not enter more games than your account have, there is no system to detect that you are out of tickets.
12. Now Blum AI clicker will play as many games as you entered and than will be stopped. If you need to stop the script during the game, hold down the English key **q** for a few seconds.

## Liked the script? Support author
- MetaMask `0x79002fD8bA43a5BFd26CD237BaC0a3677fcA9e55`
- Phantom (Solana) `Fskayrpu1BQhPz333F6Q8WfQL3Kt2kWEv4U5y82gm5Hh`
