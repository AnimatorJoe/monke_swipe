# Monke Swipe
This one night, I spent 20 minutes swiping on Tinder like a monke, and figured "why can't I have a bot that does this manual labor for me?" So here it is, the Monke Swipe bot.

## Setting Up the Runtime

### Webdriver

To run the project, first make sure you have the Chromium Web Driver [installed](https://chromedriver.chromium.org/).

For Mac OS, make sure the executable is moved to `/usr/local/bin`.

### Dependencies

Install whatever is in the requirements.txt with `pip install -r requirements.txt` either globally or in a virtualenv (recommended).

## Interface and Set Up

For automated logins, create a file called `login_cred.py` and enter credentials, ex:

```
fb_username = "georgebush420@gmail.com"
fb_password = "bush-did-420"
```

Alternatively, you can log in manually.

Run program via `python -i Bot.py`.

Available automated processes are listed in the Bot class.

## Project Goals

- [x] Set up automated login.
- [x] Implement infinite swiping.
- [ ] Handle random popups.
- [ ] Grab text from displayed profiles.
- [ ] Implement keyword filtering.
- [ ] Implement better swipe heuristic functions. (maybe return continuous values in [0, 1] instead of a boolean)

## Optional Goals

- [ ] Output log files to track automated decisions.
- [ ] Implement CSV outputting for user selections to allow ML training.
- [ ] Integrate a ML somehow.
