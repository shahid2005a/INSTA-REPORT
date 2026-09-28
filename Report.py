import time
import os
import requests
import sys
import subprocess
from colorama import Fore, Style, init

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

def open_browser(url):
    """
    Android (Termux), Windows, Linux (Kali), Mac — sab me browser kholta hai
    """
    try:
        # Android Termux
        if "com.termux" in os.environ.get("PREFIX", ""):
            if subprocess.run(["which", "termux-open-url"],
                              capture_output=True).returncode == 0:
                subprocess.run(["termux-open-url", url], check=True)
                return True
            else:
                # Fallback: am start use karo
                subprocess.run(
                    ["am", "start", "-a", "android.intent.action.VIEW",
                     "-d", url],
                    check=True
                )
                return True

        # Windows
        elif os.name == "nt":
            os.startfile(url)
            return True

        # Linux (Kali, Ubuntu, etc.)
        elif sys.platform.startswith("linux"):
            if subprocess.run(["which", "xdg-open"],
                              capture_output=True).returncode == 0:
                subprocess.run(["xdg-open", url],
                               check=True,
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL)
                return True
            # Fallback browsers
            for browser in ["firefox", "google-chrome", "chromium",
                            "chromium-browser"]:
                if subprocess.run(["which", browser],
                                  capture_output=True).returncode == 0:
                    subprocess.Popen([browser, url],
                                     stdout=subprocess.DEVNULL,
                                     stderr=subprocess.DEVNULL)
                    return True
            return False

        # Mac
        elif sys.platform == "darwin":
            subprocess.run(["open", url], check=True)
            return True

    except Exception as e:
        print(Fore.RED + f"\n⚠️ Browser open nahi ho paya: {e}")
        print(Fore.YELLOW + f"👉 Manually ye link kholo:\n{Fore.CYAN}{url}")
        return False

    return False

def fake_report(username, reason):
    print(Fore.MAGENTA + f"\n📍 Fetching profile: @{username}...")
    time.sleep(0.8)
    print(Fore.YELLOW + f"📤 Preparing official report link for: @{username}...")
    time.sleep(0.8)
    print(Fore.CYAN + f"🛡️ Reason: {reason}")
    time.sleep(0.8)

    report_url = "https://help.instagram.com/contact/636276399721841"

    print(Fore.BLUE + "🧠 Opening Instagram official report form in browser...\n")
    time.sleep(0.5)

    # Browser open karo (fixed for Termux + Kali)
    opened = open_browser(report_url)

    if opened:
        print(Fore.GREEN + "✅ Browser me report form khul gaya!")
    else:
        print(Fore.YELLOW + "⚠️ Browser automatically nahi khula — link copy karke kholo")

    print(Fore.YELLOW + "\n📋 Ab form me ye details bharo:")
    print(Fore.WHITE + "   1️⃣  'Someone created an account pretending to be me' → select karo")
    print(Fore.WHITE + "   2️⃣  'Yes, I am the person being impersonated' → select karo")
    print(Fore.WHITE + "   3️⃣  Apna Full Name daalo")
    print(Fore.WHITE + "   4️⃣  Apna Email daalo")
    print(Fore.WHITE + "   5️⃣  Relationship: 'Myself' likho")
    print(Fore.CYAN  + f"   6️⃣  'Instagram username of reported account' me likho: " + Fore.GREEN + f"{username}")
    print(Fore.WHITE + "   7️⃣  Apni ID ki photo upload karo (Aadhaar/DL/Passport)")
    print(Fore.WHITE + "   8️⃣  Additional info me likho:")
    print(Fore.YELLOW + f"        'This account @{username} is impersonating me. Please remove it.'")
    print(Fore.WHITE + "   9️⃣  Send button dabao ✅\n")

    print(Fore.MAGENTA + "🔗 Public Report Link (copy & share):")
    print(Fore.CYAN + f"   {report_url}")
    print(Fore.GREEN + f"\n   Target Username: @{username}")
    print(Fore.GREEN + f"   Reason: {reason}\n")


def is_valid_username(username):
    url = f"https://www.instagram.com/{username}/"
    try:
        headers = {
            "User-Agent": ("Mozilla/5.0 (Linux; Android 10) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/120.0 Mobile Safari/537.36")
        }
        response = requests.get(url, headers=headers, timeout=10,
                                allow_redirects=True)
        # 200 = exists, 302 sometimes = exists
        return response.status_code in (200, 302)
    except Exception:
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

    if not username:
        print(Fore.RED + "\n❌ Username khali hai!")
        return

    if not is_valid_username(username):
        print(Fore.RED + f"\n❌ Invalid Instagram Username: @{username}")
        return

    country = select_country()
    reason = select_reason()

    print(Fore.GREEN + f"\n✅ Valid Username Detected: @{username}")
    print(Fore.BLUE + f"🌍 Country Selected: {country}")
    print(Fore.RED + f"🚫 Reason Selected: {reason}")
    print(Fore.YELLOW + "\n🚀 Opening official Instagram report form...\n")

    count = 0
    try:
        while True:
            fake_report(username, reason)
            count += 1
            print(Fore.GREEN + f"✅ Report form opened #{count} for @{username} [BROWSER OPENED]")
            print(Fore.YELLOW + "⏎ Press ENTER to open again, or CTRL+C to stop...")
            input()
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n🛑 Reporting stopped by user (CTRL+C)")
        print(Fore.BLUE + f"📊 Total report forms opened: {count}")

if __name__ == "__main__":
    main()
