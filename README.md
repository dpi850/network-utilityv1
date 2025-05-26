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

2.  **Running with Python (if Python is installed):**
    ```bash
    python network_utility.py --help
    ```
    *(Assuming your main script file is `network_utility.py`.)*

3.  **Running via PowerShell (for standalone use):**
    * Download the latest pre-compiled executable from the **Releases** page of this repository.
    * Open PowerShell and navigate to the directory where you saved the executable:
        ```powershell
        .\network_utility.exe --help
        ```
    *(You'll need to create a release with a compiled `.exe` using tools like PyInstaller.)*

```bash
# Check if port 80 is open on example.com
python network_utility.py --check-port example.com 80

# View active UDP connections
python network_utility.py --connections udp

# Flush the DNS cache
python network_utility.py --flush-dns

# Display ARP cache entries
python network_utility.py --view-arp
