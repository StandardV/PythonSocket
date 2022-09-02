# PythonSocket
Connection Via LAN (Continue developing for Virtual Assistance on Raspberry pi)

## The First Thoughts
  Cliente.py will have the ability to connect to server.py via sockets connection as long as they have the right port and the right server Ipv4 address
  
  
  In short, sending CMDON from the server to client when they are connected will yield the server the ability to unlock popen, which mean cmd on the client, and the server can do any other command from it.
  
  FOR EXAMPLE:
  
    -cmd on ==> run popen feature on client.py allow the ability to type on it cmd
    -start chrome.exe ===> open google chrome
    -start chrome.exe -incognito --target URL ==> open google chrome in incognito and send it to a specific URL
    -start undefined.py ==> run a pre-written script on the host computer for example, OCRpython (https://github.com/StandardV/OCR-with-Pyautogui) , Ads autoclick (https://github.com/StandardV/Ads-Click-Automation)


## Development planning

  This script is still in the working phase so please pardon me of any mistake that I made.
  
  It is intended to work as a Virtual assistance on a Raspberry pi that will connect all household electronic, mainly the work computer. 
  
  It will have the abilities to:
    * Using Wake-On-Lan to send package from RP to wake the connected computer up from sleep mode
    * Any other Virtual Asistance feature, can answer time, say good morning, econ information...etc...
    * Able to Connect to few pre-defined client from WAN through socket, client can send command to raspberry pi and ask for it to do specific work, include Wake-On-Lan and control work computer via cmd
