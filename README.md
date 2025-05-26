# User-Level Network Utility (Windows)

A lightweight, Python-based command-line tool that provides essential network diagnostics and cache management features for Windows — **all without requiring administrator privileges.**

---

## Features

* **Check TCP Port Availability:** Test if a specific port is open on any host, ideal for server or application troubleshooting.
* **View Active Network Connections:** Displays current TCP/UDP connections using `netstat`.
* **Release and Renew IP Address:** Refresh your network adapter configuration safely.
* **DNS & ARP Cache Management:**
    * Flush the DNS resolver cache.
    * View DNS cache entries.
    * Display ARP cache information.
* **PowerShell Compatible:** Run the script through PowerShell even if Python is not installed system-wide (requires a pre-compiled executable, see **Installation** below).

---

## Getting Started

### Prerequisites

* **Python 3.x:** If you plan to run the script directly with Python.
    * Uses only standard libraries: `socket`, `subprocess`, `os`, `time`, `re`.
* **PowerShell:** Pre-installed on Windows and allows running the pre-compiled executable.

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```
    *(Remember to replace `https://github.com/your-username/your-repo-name.git` with your actual repository URL.)*


```bash
# Check if port 80 is open on example.com
python network_utility.py --check-port example.com 80

# View active UDP connections
python network_utility.py --connections udp

# Flush the DNS cache
python network_utility.py --flush-dns

# Display ARP cache entries
python network_utility.py --view-arp

# This project is licensed under the GNU General Public License v3.0 (GPL-3.0).
