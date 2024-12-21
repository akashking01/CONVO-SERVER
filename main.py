import requests
import time
from datetime import datetime
from colorama import Fore, init
import random

# Colorama Initialization
init(autoreset=True)

# Light Colors for Random Selection
COLORS = [
    Fore.LIGHTCYAN_EX,
    Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTBLUE_EX,
    Fore.LIGHTGREEN_EX,
    Fore.LIGHTYELLOW_EX
]

# Welcome Logo
def print_welcome_logo():
    welcome_logo = '''
      __       __   ___       __        ________  __    __      
     /""\     |/"| /  ")     /""\      /"       )/" |  | "\     
    /    \    (: |/   /     /    \    (:   \___/(:  (__)  :)    
   /' /\  \   |    __/     /' /\  \    \___  \   \/      \/     
  //  __'  \  (// _  \    //  __'  \    __/  \\  //  __  \\     
 /   /  \\  \ |: | \  \  /   /  \\  \  /" \   :)(:  (  )  :)    
(___/    \___)(__|  \__)(___/    \___)(_______/  \__|  |__/     
                                                                
    '''
    print(Fore.LIGHTGREEN_EX + welcome_logo)

# Function to read token and message from file
def read_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

# Get token details (user and token status)
def get_token_details(access_token):
    url = "https://www.facebook.com/chandrajeet.yadav.965928"
    params = {"access_token": access_token, "fields": "name"}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("name", "Unknown"), "Token is valid"
    else:
        return "Unknown", "Invalid or expired token"

# Main Script
# Show Welcome Logo
print_welcome_logo()

# Token and Message file path inputs
token_file_path = input("Enter the path of the access token file: ").strip()
message_file_path = input("Enter the path of the message file: ").strip()

# Read Access Token
access_token = read_from_file(token_file_path)
if not access_token:
    exit("No Access Token available. Please check the token file.")

# Get user and token details
user_name, token_status = get_token_details(access_token)

# Get Target ID
target_id = input("Enter the Target ID: ").strip()
if not target_id:
    exit("Target ID cannot be empty. Please provide a valid ID.")

# Read Message from file
message = read_from_file(message_file_path)
if not message:
    exit("Message file is empty or missing. Please check the message file.")

# Optional: Haters Name and Owner Name inputs
haters_name = input("Enter the Haters Name (Optional): ").strip()

# Time Interval input
try:
    time_interval = int(input("Enter the time interval (in seconds) between messages: ").strip())
    if time_interval < 1:
        raise ValueError
except ValueError:
    exit("Invalid time interval. Please provide a positive integer.")

# Owner Name (Fixed as 'Akash King'')
owner_name = "Akash King")

# Loop to send messages with time intervals
while True:
    # Prepare the full message and API parameters
    full_message = f"{haters_name} {message.strip()}" if haters_name else message.strip()
    url = f"https://graph.facebook.com/v17.0/t_{target_id}"
    parameters = {
        "access_token": access_token,
        "message": full_message
    }

    # API Request
    response = requests.post(url, data=parameters)

    # Get Current Time and Date
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Select Random Color
    color = random.choice(COLORS)

    # Print Owner, Token, and Message Details
    print(f"\n{color}Owner: {owner_name}")
    print(f"{color}Token Owner: {user_name}")
    print(f"{color}Token Status: {token_status}")
    print(f"{color}Time: {current_time}")
    print(f"{color}Message Sent: {full_message}")  # Printing the message being sent

    # Check if message was sent successfully (without printing full response)
    if response.status_code == 200:
        print(f"{color}Message sent successfully.")
    else:
        print(f"{color}Failed to send message: {response.status_code}")

    # Wait for the specified time interval
    time.sleep(time_interval)