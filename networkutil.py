import subprocess
import socket
import time
import re
import os

# --- Helper Functions (from previous individual scripts) ---

def check_port_status(host, port, timeout=1):
    """
    Checks if a given port is open on a host from a user's perspective.
    This does not require administrator privileges.
    """
    if not isinstance(port, int) or not (1 <= port <= 65535):
        return False, "Invalid port number. Must be between 1 and 65535."

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        sock.connect((host, port))
        return True, f"Port {port} on {host} is OPEN (TCP connection established)."
    except socket.timeout:
        return False, f"Port {port} on {host} is CLOSED or connection timed out."
    except ConnectionRefusedError:
        return False, f"Port {port} on {host} is CLOSED (connection refused by target)."
    except socket.gaierror:
        return False, f"Could not resolve hostname: {host}. Check the host name or IP address."
    except socket.error as e:
        return False, f"An unexpected socket error occurred: {e}"
    finally:
        sock.close()

def get_current_connections():
    """
    Lists active network connections visible to a standard user.
    This does not require administrator privileges.
    """
    print("\n--- Current Network Connections (User View) ---")
    print("Protocol  Local Address          Foreign Address        State")
    print("--------  ---------------------  ---------------------  -----------")

    command = ["netstat", "-an"]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=False, encoding='utf-8', creationflags=subprocess.DETACHED_PROCESS)
        # Using check=False to handle cases where netstat might return non-zero (e.g., no connections)
        # Using creationflags=subprocess.DETACHED_PROCESS can sometimes help prevent the console window from flashing briefly on older systems.

        if result.returncode != 0:
            print(f"Error running netstat: {result.stderr}")
            if "requested operation requires elevation" in result.stderr.lower():
                print("Note: Running as administrator might provide more detailed information (e.g., process IDs).")
            return

        lines = result.stdout.splitlines()
        data_start_index = -1
        for i, line in enumerate(lines):
            if line.strip().startswith("Proto"):
                data_start_index = i + 1
                break

        if data_start_index == -1:
            print("Could not parse netstat output.")
            return

        for line in lines[data_start_index:]:
            parts = line.strip().split()
            if len(parts) >= 4:
                protocol = parts[0]
                local_address = parts[1]
                foreign_address = parts[2]
                state = parts[3] if len(parts) > 3 else ""
                print(f"{protocol:<8}  {local_address:<21}  {foreign_address:<21}  {state:<11}")

    except FileNotFoundError:
        print("Error: netstat command not found. Make sure it's in your PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def flush_dns_cache():
    """
    Flushes the DNS resolver cache. This does not require administrator privileges.
    """
    print("\n--- Flushing DNS Resolver Cache ---")
    command = ["ipconfig", "/flushdns"]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True, encoding='cp437', creationflags=subprocess.DETACHED_PROCESS)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error flushing DNS cache:\n{e.stderr}")
    except FileNotFoundError:
        print("Error: ipconfig command not found. Make sure it's in your PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def display_dns_cache():
    """
    Displays the contents of the DNS resolver cache.
    This does not require administrator privileges.
    """
    print("\n--- Displaying DNS Resolver Cache ---")
    command = ["ipconfig", "/displaydns"]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True, encoding='cp437', creationflags=subprocess.DETACHED_PROCESS)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error displaying DNS cache:\n{e.stderr}")
    except FileNotFoundError:
        print("Error: ipconfig command not found. Make sure it's in your PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def release_and_renew_ip():
    """
    Releases and renews the IP address for all network adapters.
    This does not require administrator privileges.
    """
    print("\n--- Releasing IP Address ---")
    release_command = ["ipconfig", "/release"]
    try:
        result = subprocess.run(release_command, capture_output=True, text=True, check=False, encoding='cp437', creationflags=subprocess.DETACHED_PROCESS)
        print(result.stdout)
        if result.returncode != 0:
            print(f"Warning/Error during IP release: {result.stderr}")
    except FileNotFoundError:
        print("Error: ipconfig command not found. Make sure it's in your PATH.")
        return
    except Exception as e:
        print(f"An unexpected error occurred during release: {e}")
        return

    print("\n--- Waiting a moment before renewing... ---")
    time.sleep(2)

    print("\n--- Renewing IP Address ---")
    renew_command = ["ipconfig", "/renew"]
    try:
        result = subprocess.run(renew_command, capture_output=True, text=True, check=True, encoding='cp437', creationflags=subprocess.DETACHED_PROCESS)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error renewing IP address:\n{e.stderr}")
        if "No operation can be performed on all adapters" in e.stderr:
            print("This might happen if your network adapter is disabled or disconnected.")
    except FileNotFoundError:
        print("Error: ipconfig command not found. Make sure it's in your PATH.")
    except Exception as e:
        print(f"An unexpected error occurred during renew: {e}")

def display_arp_cache():
    """
    Displays the ARP (Address Resolution Protocol) cache.
    This typically does not require administrator privileges.
    """
    print("\n--- Displaying ARP Cache ---")
    command = ["arp", "-a"]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True, encoding='utf-8', creationflags=subprocess.DETACHED_PROCESS)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error displaying ARP cache:\n{e.stderr}")
    except FileNotFoundError:
        print("Error: arp command not found. Make sure it's in your PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

# --- Sub-menu for Cache Management ---
def cache_management_menu():
    """Displays the cache management sub-menu."""
    while True:
        clear_screen()
        print("+" + "="*30 + "+")
        print("|" + " " * 4 + "Network Cache Management" + " " * 4 + "|")
        print("+" + "="*30 + "+")
        print("| 1. Flush DNS Cache             |")
        print("| 2. Display DNS Cache           |")
        print("| 3. Display ARP Cache           |")
        print("| 4. Back to Main Menu           |")
        print("+" + "="*30 + "+")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            flush_dns_cache()
        elif choice == '2':
            display_dns_cache()
        elif choice == '3':
            display_arp_cache()
        elif choice == '4':
            break # Exit sub-menu
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

        input("\nPress Enter to return to the cache management menu...")


# --- Main Script Logic ---

def main_menu():
    """Displays the main menu and handles user input."""
    while True:
        clear_screen()
        print("+" + "="*40 + "+")
        print("" + " " * 8 + "User-Level Network Utility v1")
        print("+" + "="*40 + "+")
        print("| 1. Check Port Availability             |")
        print("| 2. View Current Network Connections    |")
        print("| 3. Release and Renew IP Address        |")
        print("| 4. Network Cache Management            |")
        print("| 5. Exit                                |")
        print("+" + "="*40 + "+")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            host = input("Enter host (e.g., 127.0.0.1 or google.com): ").strip()
            try:
                port = int(input("Enter port number: ").strip())
                status, message = check_port_status(host, port)
                print(f"\nResult: {'Open' if status else 'Closed'}. {message}")
            except ValueError:
                print("\nInvalid port number. Please enter an integer.")
            except Exception as e:
                print(f"\nAn error occurred during port check: {e}")
        elif choice == '2':
            get_current_connections()
        elif choice == '3':
            release_and_renew_ip()
        elif choice == '4': # Call the new cache management sub-menu
            cache_management_menu()
        elif choice == '5':
            print("Exiting User-Level Network Utility. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.") # Updated range

        input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    main_menu()