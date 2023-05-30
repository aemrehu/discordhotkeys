from pynput import keyboard
import requests
import sys
import tomli

URL = ""

header = {}

resume = {
    "content": "m!resume"
}
pause = {
    "content": "m!pause"
}
skip = {
    "content": "m!s"
}
summon = {
    "content": "m!summon"
}

def on_activate_pause():
    requests.post(URL, json=pause, headers=header)
    print("PAUSE")

def on_activate_resume():
    requests.post(URL, json=resume, headers=header)
    print("RESUME")

def on_activate_skip():
    requests.post(URL, json=skip, headers=header)
    print("SKIP")

def on_activate_summon():
    requests.post(URL, json=summon, headers=header)
    print("SUMMON")

if __name__ == "__main__":
    try:
        with open(sys.argv[1], "rb") as file:
            settings = tomli.load(file)
        for key, value in settings["header"].items():
            header[key] = value
        for _, value in settings["url"].items():
            URL = value
    except Exception:
        raise Exception("Please provide proper settings.toml file.")

    with keyboard.GlobalHotKeys({
        '<alt_gr>+p': on_activate_pause,
        '<alt_gr>+o': on_activate_resume,
        '<alt_gr>+i': on_activate_skip,
        '<alt_gr>+å': on_activate_summon
    }) as h: h.join()
