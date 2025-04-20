# Discord Clan Badge Changer

A simple Python script that automatically rotates between different Discord server badges on your profile.

## Features

- Automatically cycles through server badges/clans
- Customizable rotation time
- Simple setup and usage
- Shows the server name when changing badges

## Prerequisites

- Python 3.6+
- `requests` library

## Setup

1. Install the required package:
   ```
   pip install requests
   ```

2. Create a file named `clans.txt` in the same directory as the script
3. Add Discord server IDs (one per line) to the `clans.txt` file

Example `clans.txt`:
```
123456789012345678
987654321098765432
876543210987654321
```

## How to Get Your Discord Token

> ⚠️ **WARNING**: Never share your Discord token with anyone! Your token provides full access to your account.

1. Open Discord in your browser
2. Press `F12` to open developer tools
3. Go to the "Network" tab
4. Refresh the page (F5)
5. Click on any request to "discord.com"
6. Look for "Authorization" in the request headers
7. Copy the token value

## How to Get Server IDs

1. In Discord, go to User Settings → Advanced
2. Enable "Developer Mode"
3. Right-click on any server icon
4. Select "Copy ID"

## Usage

Run the script:
```
python clan.py
```

The script will:
1. Ask for your Discord token
2. Load server IDs from `clans.txt`
3. Cycle through each server badge every 30 seconds

To stop the script, press `Ctrl+C`.

## Legal Notice

This tool is meant for educational purposes only. Using this script might violate Discord's Terms of Service. Use at your own risk.

## License

MIT License

## Disclaimer

This project is not affiliated with or endorsed by Discord Inc.
