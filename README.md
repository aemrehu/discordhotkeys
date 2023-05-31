# Simple script to control Jockie Music discord bot

## Usage from command line:

    python hotkeys.py settings.toml

## Settings file must be `.toml`, follow this syntax and can be named whatever:

    [url]
    URL = "https...."

    [header]
    "authorization" = "AUTHCODE"
    "content-type" = "application/json"

## I recommend creating a shortcut with this target:

    C:\Windows\System32\cmd.exe /c python Your\path\here\hotkeys.py Your\path\here\settings.toml