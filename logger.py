import sys
from colorama import init, Fore, Style

init(autoreset=True)

def info(msg):
    print(f"{Fore.CYAN}[*] {msg}{Style.RESET_ALL}")

def success(msg):
    print(f"{Fore.GREEN}[+] {msg}{Style.RESET_ALL}")

def error(msg):
    print(f"{Fore.RED}[!] {msg}{Style.RESET_ALL}", file=sys.stderr)

def raw_data(msg):
    print(f"{Fore.YELLOW}[>] {msg}{Style.RESET_ALL}")