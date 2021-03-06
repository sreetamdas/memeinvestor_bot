import time
import logging

import praw

import config
import message
from main import reply_wrap

praw.models.Submission.reply_wrap = reply_wrap
logging.basicConfig(level=logging.INFO)


def main():
    reddit = praw.Reddit(client_id=config.client_id,
                         client_secret=config.client_secret,
                         username=config.username,
                         password=config.password,
                         user_agent=config.user_agent)

    logging.info("Starting checking submissions...")
    while True:
        try:
            for submission in reddit.subreddit('+'.join(config.subreddits)).stream.submissions(skip_existing=True):
                logging.info("New submission: %s" % submission)
                submission.reply_wrap(message.invest_place_here).\
                    mod.distinguish(how='yes', sticky=True)
        except Exception as e:
            logging.error(e)
            time.sleep(10)


if __name__ == "__main__":
    main()
