import requests
import json
import time
import os
import random
from pathlib import Path


cookies = {}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/json',
    'Authorization': input("🔒 Enter your discord token: "),
    'Origin': 'https://discord.com',
    'Alt-Used': 'discord.com',
    'Connection': 'keep-alive',
    'Referer': 'https://discord.com/channels/@me',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

def read_clan_ids(file_path="./clans.txt"):
    try:
        with open(file_path, 'r') as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"File clans.txt not found g")
        return []

def get_clan_info(clan_id, headers, cookies):
    try:
        response = requests.get(f'https://discord.com/api/v9/guilds/{clan_id}', 
                            headers=headers, cookies=cookies)
        


        if response.status_code == 200:
            guild_data = response.json()
            return guild_data.get("name", "Unknown")
        else:
            return "Unknown"
    except:
        return "Unknown"
            
def update_clan(clan_id, headers, cookies):
    clan_name = get_clan_info(clan_id, headers, cookies)
    
    data = json.dumps({
        "identity_guild_id": clan_id,
        "identity_enabled": True
    })
    



    response = requests.put('https://discord.com/api/v9/users/@me/clan', 
                          cookies=cookies, headers=headers, data=data)
    
    if response.status_code == 200:
        print(f"Profile now showing clan: {clan_name}")
        return True
    else:
        print(f"Failed to change clan (Error {response.status_code})")
        return False

def main():
    ids = read_clan_ids()
    
    if not ids:
        print("No clan IDs found in the file")
        return
    
    print(f"Found {len(ids)} clan IDs in clans.txt")
    
    try:
        while True:
            for clan_id in ids:
                print(f"\nSwitching to clan ID: {clan_id}")
                success = update_clan(clan_id, headers, cookies)
                
                if not success:
                    print("Failed to update clan")
                
                time_u_gotta_wait = 30 #30 secs 
                print(f"{time_u_gotta_wait} seconds before clan badge change")
                time.sleep(time_u_gotta_wait)
    
    except KeyboardInterrupt:
        print("\nScript stopped now")

if __name__ == "__main__":
    main()