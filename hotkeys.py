import sys
import requests
import tomli
from pynput import keyboard

class Hotkeys:

    TIMEOUT = 10
    url = ""
    paused: bool = False
    header = {}

    resume  = {"content": "m!resume"}
    pause   = {"content": "m!pause"}
    skip    = {"content": "m!s"}
    summon  = {"content": "m!summon"}
    foff    = {"content": "m!fuck off"}

    def __init__(self, arg) -> None:
        self.read_file(arg)

    def on_activate_pauseresume(self):
        if self.paused:
            self.paused = False
            requests.post(self.url, json=self.resume, headers=self.header, timeout=self.TIMEOUT)
            print("RESUME")
        else:
            self.paused = True
            requests.post(self.url, json=self.pause, headers=self.header, timeout=self.TIMEOUT)
            print("PAUSE")

    # def on_activate_pause(self):
    #     requests.post(self.url, json=self.pause, headers=self.header, timeout=self.TIMEOUT)
    #     print("PAUSE")

    # def on_activate_resume(self):
    #     requests.post(self.url, json=self.resume, headers=self.header, timeout=self.TIMEOUT)
    #     print("RESUME")

    def on_activate_skip(self):
        requests.post(self.url, json=self.skip, headers=self.header, timeout=self.TIMEOUT)
        print("SKIP")

    def on_activate_summon(self):
        requests.post(self.url, json=self.summon, headers=self.header, timeout=self.TIMEOUT)
        print("SUMMON")

    def on_activate_fuckoff(self):
        requests.post(self.url, json=self.foff, headers=self.header, timeout=self.TIMEOUT)
        print("FUCKOFF")

    def on_activate_terminate(self):
        sys.exit()

    def read_file(self, arg):
        try:
            with open(arg, "rb") as file:
                settings = tomli.load(file)
            for key, value in settings["header"].items():
                self.header[key] = value
            for _, value in settings["url"].items():
                self.url = value
        except Exception:
            raise Exception("Check .toml file.")

    def run(self):
        print("Hotkeys:")
        print("    ctrl + ä = pause and resume")
        print("    ctrl + ö = skip")
        print("    ctrl + l = summon")
        print("    ctrl + k = kick off")
        print("    ctrl + alt + q = terminate hotkeys")
        with keyboard.GlobalHotKeys({
            '<ctrl>+ä': self.on_activate_pauseresume,
            '<ctrl>+ö': self.on_activate_skip,
            '<ctrl>+l': self.on_activate_summon,
            '<ctrl>+k': self.on_activate_fuckoff,
            '<ctrl>+<alt>+q': self.on_activate_terminate
        }) as h: h.join()


if __name__ == "__main__":
    hotkeys = Hotkeys(sys.argv[1])
    hotkeys.run()