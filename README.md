User-Level Network Utility (Windows)

A lightweight, Python-based command-line tool that provides essential network diagnostics and cache management features for Windows — all without requiring administrator privileges.
Features

    Check TCP Port Availability
    Test if a specific port is open on any host, ideal for server or application troubleshooting.

    View Active Network Connections
    Displays current TCP/UDP connections using netstat.

    Release and Renew IP Address
    Refresh your network adapter configuration safely.

    DNS and ARP Cache Management

        Flush the DNS resolver cache

        View DNS cache entries

        Display ARP cache information

    PowerShell Compatible
    Run the script through PowerShell even if Python is not installed system-wide.

Platform Support

    Windows 10 / 11

    Not compatible with Linux or macOS

Requirements

    Python 3.x (if running via Python)

        Uses only standard libraries: socket, subprocess, os, time, re

    Alternatively, launch the script through PowerShell (pre-installed on Windows)
Permissions and Safety

This tool:

    Does not require administrator privileges

    Accesses only non-sensitive system-level network information

    Is suitable for learning and local diagnostics

Use Cases

    Local connectivity troubleshooting

    Safe port and connection status checking

    Visualizing Windows DNS and ARP cache contents

License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0).
