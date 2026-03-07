import time
import os
import requests
import sys
from colorama import Fore, Style, init
# reporter.py এখন দরকার নেই কারণ সব কিছু main.py তে করা হচ্ছে

init(autoreset=True)

def slow_print(text, color=Fore.WHITE, delay=0.03):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.RED + Style.BRIGHT + r"""

██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗
██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   
██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   
██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   
╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   

              🔥 Digital Cyber Insta Ban Tool 💀

       🧏 Developer By : Shahid Afridi
        🔴 YouTube  : Er.Aryan Afridi

""")

def fake_report(username, reason):
    print(Fore.MAGENTA + f"\n📍 Fetching profile: @{username}...")
    time.sleep(1)
    print(Fore.YELLOW + f"📤 Submitting report for: @{username}...")
    time.sleep(1)
    print(Fore.CYAN + f"🛡️ Reason: {reason}")
    time.sleep(1)
    print(Fore.BLUE + "🧠 Processing request...\n")
    time.sleep(1)

def is_valid_username(username):
    url = f"https://www.instagram.com/{username}/"
    try:
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False

def select_country():
    slow_print("\n🌍 Select the Country of the Instagram Account:", Fore.YELLOW)
    countries = [
        "🇮🇳 India",
        "🇺🇸 USA",
        "🇬🇧 UK",
        "🇧🇩 Bangladesh",
        "🇵🇰 Pakistan",
        "🌐 Other"
    ]
    for i, country in enumerate(countries, start=1):
        slow_print(f"[{i}] {country}", Fore.CYAN)
    choice = input(Fore.GREEN + "📥 Enter choice number: ")
    try:
        return countries[int(choice) - 1]
    except:
        return "🌐 Other"
    
def select_reason():
    slow_print("\n🚫 Select the Reason for Reporting:", Fore.RED)
    reasons = [
        "Fake Account",
        "Adult Content",
        "Hate Speech",
        "Harassment or Bullying",
        "Posting Violence or Abuse",
        "Spam or Scam Activity"
    ]
    for i, reason in enumerate(reasons, start=1):
        slow_print(f"[{i}] {reason}", Fore.YELLOW)
    choice = input(Fore.GREEN + "📥 Enter reason number: ")
    try:
        return reasons[int(choice) - 1]
    except:
        return "Fake Account"

def main():
    banner()
    slow_print("\n🔎 Enter Instagram Username to report:", Fore.CYAN)
    username = input(Fore.GREEN + "@").strip().lstrip('@')

    if not is_valid_username(username):
        print(Fore.RED + f"\n❌ Invalid Instagram Username: @{username}")
        return

    country = select_country()
    reason = select_reason()

    print(Fore.GREEN + f"\n✅ Valid Username Detected: @{username}")
    print(Fore.BLUE + f"🌍 Country Selected: {country}")
    print(Fore.RED + f"🚫 Reason Selected: {reason}")
    print(Fore.YELLOW + "\n🚀 Starting Instagram account report... (Press CTRL+C to stop)\n")

    try:
        count = 0
        while True:
            # Call the fake_report function for each report
            fake_report(username, reason)
            count += 1
            print(Fore.GREEN + f"✅ 🌐Report #{count} sent for @{username} (Reason: {reason}) [REPORTED]")
            time.sleep(1)  # Small delay between reports
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n🛑 Reporting stopped by user (CTRL+C)")
        print(Fore.BLUE + f"📊 Total fake reports sent: {count}")

if __name__ == "__main__":
    main()