# Monke Swipe
This one night, I spent 20 minutes swiping on Tinder like a monke, and figured "why can't I have a bot that does this manual labor for me?" So here it is, the Monke Swipe bot.

## Setting Up the Runtime

### WebDriver

To run the project, first make sure you have the Chromium WebDriver [installed](https://chromedriver.chromium.org/).

For Mac OS, make sure the executable is moved to `/usr/local/bin`.

### Dependencies

Install whatever is in the requirements.txt with `pip install -r requirements.txt` either globally or in a virtualenv (recommended).

### Interface and Set Up

For automated logins, create a file called `login_cred.py` and enter credentials. (Alternatively, you can log in manually).

To set filter keywords, create a file called `filter_options.py`.

The formats required for each file can be found under `empty_configs/`.

Run program via `python -i Bot.py`.

Available automated processes are listed in the Bot class.

## Project Goals

- [x] Set up automated login.
- [x] Implement infinite swiping.
- [ ] Handle random popups.
- [ ] Grab text from displayed profiles.
- [ ] Implement keyword filtering.
- [ ] Implement better swipe heuristic functions.

## Optional Goals

- [ ] Output log files to track automated decisions.
- [ ] Implement CSV outputting for user selections to allow ML training.
- [ ] Integrate a ML somehow.
