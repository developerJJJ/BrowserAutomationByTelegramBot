from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import socket

# Set up the socket server to listen for incoming connections
host = "localhost"
port = 9226
# socket(AF_INET, SOCK_STREAM)
s = socket.socket()
s.bind((host, port))
s.listen(1)

# wait for a client to connect
print(f"Waiting for a client to connect at {host}:{port}")
conn, addr = s.accept()
print(f"Client connected from {addr[0]}:{addr[1]}")

# receive the URL from the client
url = conn.recv(1024).decode('utf-8').strip()

# Specify options to use existing profile
options = Options()
# Debugging options
options.add_experimental_option('debuggerAddress', f'localhost:9225')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Use the driver to navigate to a website and perform actions
print(f"url: {url}")
driver.get(url)

# Get website URL input from console
website_url = input("Enter website URL: ")

# Set up Chrome driver and open website
driver.get(website_url)

conn.close()
s.close()

# Keep the browser window open
input("Press any key to quit.")
driver.quit()