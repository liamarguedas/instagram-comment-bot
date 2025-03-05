from src import Utils
from src import Bot

def main():
    """todo"""

    account = Utils().read_configuration()
    bot = Bot()
    bot.login(account["username"], account["password"])

if __name__ == "__main__":
    main()
