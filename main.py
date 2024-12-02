import time
import requests
import socket
import paramiko


hostname = "192.168.56.2"  # Replace with the remote server's address
username = "vidhi"       # Replace with your username
password = "Changeme"       # Replace with your password

def print_local_datetime():
    print("Local Date and Time:", time.strftime("%Y-%m-%d %H:%M:%S"))

def show_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print("Local IP Address:", ip_address)

def list_remote_directory():
    ssh = paramiko.SSHClient()

    # Automatically add the remote server's SSH key (optional, use with caution)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the remote server
        ssh.connect(hostname, username=username, password=password)
        print(f"Connected to {hostname}")

        # Execute the command to list the home directory
        stdin, stdout, stderr = ssh.exec_command("ls -la ~")
        output = stdout.read().decode()  # Read the command's output
        error = stderr.read().decode()  # Read any errors

        # Print the directory listing
        if output:
            print("Home Directory Listing:\n", output)
        elif error:
            print("Error:\n", error)

    except Exception as e:
        print(f"Error connecting to the remote server: {e}")

    finally:
        # Close the SSH connection
        ssh.close()

def backup_remote_file():
    try:
        # Initialize SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the remote server
        ssh.connect(hostname, username=username, password=password)
        print(f"Connected to {hostname}")
        
        # Download the remote file and save it locally
        remote_file_path = input("Enter Full Path: ")
        remote_file_path_backup = remote_file_path + ".old"
        stdin, stdout, stderr = ssh.exec_command(f"cp {remote_file_path} {remote_file_path_backup}")

        print(f"File backed up successfully: {remote_file_path}")
        
        # Close the SCP connection

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the SSH connection
        ssh.close()

def save_web_page():
    url = input("Enter the URL of the web page: ")
    output_file = "saved_webpage.html"
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(response.text)
        print(f"Web page saved as {output_file}")
    except requests.exceptions.RequestException as e:
        print(f"Error saving web page: {e}")

# Main menu loop
while True:
    print("\nMenu:")
    print("1 - Print local date and time")
    print("2 - Show local IP address")
    print("3 - List Home Directory")
    print("4 - Backup remote file")
    print("5 - Save web page")
    print("Q - Quit")

    choice = input("Enter your choice: ").strip().upper()

    if choice == "1":
        print_local_datetime()
    elif choice == "2":
        show_ip_address()
    elif choice == "3":
        list_remote_directory()
    elif choice == "4":
        backup_remote_file()
    elif choice == "5":
        save_web_page()
    elif choice == "Q":
        print("Goodbye!")
        break
    else:
        print("Invalid option, please try again.")
