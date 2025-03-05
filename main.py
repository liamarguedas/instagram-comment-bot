from src import Utils
from src import Bot

def main():
    """todo"""

    account = Utils().read_configuration()
    bot = Bot()
    bot.login(account["username"], account["password"])
    bot.read_and_send_comments()

if __name__ == "__main__":
    main()
