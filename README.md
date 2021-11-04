# Phendrana
A All-in-One Automatic Pentest and Reporting System

# Description
Phendrana APRS aim to be a fully automated Pentest and Reporting System developped in Python.</br>
It's goal is to automate one or more phases such as Recon or Data gathering, it will aswell search for vulnerability and set all KPI / KRI to a dashboard.</br>
Developpement begins the 29th October 2021</br>

# Author
MERAOUMIA Rachid / Shashka</br>Cybersecurity Engineer
Copyright Rachid Meraoumia AKA Shashka</br>Distributed under license CC-BT-NC-SA 4.0</br>All rights Reserved

# To-Do

- 👁 WEB RECON
  - [ ] Gather Information from web (keyword based search with a bot)
  - [ ] Gather Information Actively (Mailing System ?)
- 🔎 LOCAL RECON SCANNER
  - Network Scanner
    - [X] Add a network detection and probing system
    - [ ] Add a Cartography system (Once all machine of the network has been discovered)
    - [ ] Show it in dashboard 
  - Port Scanner
    - [X] Add a banner grabber
    - [X] Report to a CSV All Ports (Open closed filtered) and the service found if so
  - Subdomains Scanner
    - [X] Recover all domain found with server Code into a CSV file
    - [ ] Show them in Dashboard
  - Vuln scanner
    - [ ] Get all vuln found
    - [ ] Report to a CSV to populate the dashboard
    - [ ] Show Potential solution to patch and fix the vuln
    - [ ] Ask Aubin for a potential Sysmon Integration 
- 📝 SYNTHESIS AND RESULTS
  - [ ] Implement a Dashboard
  - [ ] Design Dashboard 
  - [ ] Create Layout
  - [ ] Add a Login Page
  - [ ] Create Callback function to populate the dashboard
  - [ ] Make a report based on the systhesis of the dashboard
