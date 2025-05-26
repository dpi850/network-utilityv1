# User-Level Network Utility (Windows)

A lightweight, user-level, Python-based command-line tool that provides essential network diagnostics, and cache management features for Windows.
This project is released under the GNU Public License (GPL)

---

## Features

* **Check TCP Port Availability:** Test if a specific port is open on any host, ideal for server or application troubleshooting.
* **View Active Network Connections:** Displays current TCP/UDP connections using `netstat`.
* **Release and Renew IP Address:** Refresh your network adapter configuration safely.
* **DNS & ARP Cache Management:**
    * Flush the DNS resolver cache.
    * View DNS cache entries.
    * Display ARP cache information.
* **PowerShell Compatible:** Run the script through PowerShell even if Python is not installed system-wide.

---

## Getting Started

### Prerequisites

* **Python 3.x:** If you plan to run the script directly with Python.
    * Uses only standard libraries: `socket`, `subprocess`, `os`, `time`, `re`.
* **PowerShell:** Pre-installed on Windows and allows running the pre-compiled executable.
