# CodeAlpha Internship — Task 1: Basic Network Sniffer

A beginner-friendly Python packet sniffer using Scapy. It displays IPv4 source
and destination addresses, packet size, common protocols, ports, and a limited
hexadecimal payload preview.

## Requirements

- Windows 10/11
- Python 3.9 or newer
- Npcap for Windows: https://npcap.com/#download
- Administrator terminal (packet capture may require elevated privileges)

## Setup

1. Install Python and enable **Add Python to PATH**.
2. Install Npcap using its default options.
3. Open PowerShell or Command Prompt in this folder.
4. (Optional) Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

5. Install Scapy:

   ```powershell
   python -m pip install -r requirements.txt
   ```

## Run

Open Command Prompt or PowerShell as **Administrator**, navigate to this folder,
and run:

```powershell
python main.py
```

Generate normal traffic on your own device (for example, visit a website).
Press `Ctrl+C` to stop.

## Features

- Capture timestamp
- IPv4 source and destination addresses
- IP version and packet size
- TCP, UDP, and ICMP identification
- TCP/UDP source and destination ports
- Payload length and up to 80 bytes displayed in hexadecimal
- Non-IPv4 packet summary

## Troubleshooting

- **`python` is not recognized:** reinstall Python and enable Add Python to PATH.
- **No packets appear:** check Npcap, run as Administrator, and generate traffic.
- **Scapy import error:** run `python -m pip install -r requirements.txt`.
- **Capture interface issue:** check Npcap installation and available interfaces.

## Safety

Capture only traffic on your own device or a network for which you have explicit
permission. Do not intercept other people's communications. This program does
not print complete packet payloads.

## Project structure

```text
CodeAlpha_BasicNetworkSniffer/
├── main.py
├── requirements.txt
├── README.md
└── gitignore
```

## Submission evidence checklist

- [ ] Dependency installation screenshot
- [ ] Program startup screenshot
- [ ] Captured TCP traffic screenshot
- [ ] Captured UDP traffic screenshot, if observed
- [ ] Clean stop with Ctrl+C screenshot
- [ ] Verify the project on your Windows machine before submission
