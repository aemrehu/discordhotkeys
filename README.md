# Simple script to control Jockie Music discord bot

## Usage from command line:

    python hotkeys.py settings.toml

## Settings file must be `.toml`, follow this syntax and can be named whatever:

    [url]
    URL = "<THE CHANNEL URL WHERE COMMANDS ARE TO BE SENT>"

    [header]
    "authorization" = "<YOUR DISCORD ACCOUNT AUTH CODE>"
    "content-type" = "application/json"

## Shortcut for easy running:

I recommend creating a Windows shortcut with this target:

    C:\Windows\System32\cmd.exe /c python Your\path\here\hotkeys.py Your\path\here\settings.toml