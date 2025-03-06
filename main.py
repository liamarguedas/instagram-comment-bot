from src import Utils 
from src import Bot
import time

def main():
    """todo"""

    account = Utils().read_configuration()

    bot = Bot(headless=True)
    bot.login(account["username"], account["password"])

    while True:

        time.sleep(60*10)

        if bot.new_comment_recieved():
            
            bot.read_and_send_comments()


if __name__ == "__main__":
    main()
