# masscan.py

import os

print("Masscan Scanner")
print("Select a scan option by entering the corresponding number:")
print("1. Scan for Remote Desktop Protocol (RDP) servers")
print("2. Scan for Simple Network Management Protocol (SNMP) servers")
print("3. Scan for Internet Protocol (IP) cameras")
print("4. Scan for Secure Shell (SSH) servers")
print("5. Scan for virtual private network (VPN) servers")
print("6. Scan for file transfer protocol (FTP) servers")
print("7. Scan for network attached storage (NAS) devices")
print("8. Scan for Telnet servers or routers")
print("9. Scan the top 1000 ports")
print("10. Scan for web servers")
print("11. Scan for database servers")
print("12. Scan for mail servers")
print("13. Scan for virtualization hosts")
print("14. Scan for printers")
print("15. Scan for WP Sites")
print("16. Scan for Docker Hosts")
print("17. Scan for Industrial Control Units")
print("99. This will exit the program")

scan_choice = int(input("Enter your choice: "))

if scan_choice == 1:
    os.system("masscan 0.0.0.0/0 -p3389 --excludefile=exclude.txt --rate=10000 -oL scan_results/results_RDP.txt")
elif scan_choice == 2:
    os.system("masscan 0.0.0.0/0 -p161 --excludefile=exclude.txt --rate=10000 -oL scan_results/results_SNMP.txt")
elif scan_choice == 3:
    os.system("masscan 0.0.0.0/0 -p554 --excludefile=exclude.txt --rate=10000 -oL scan_results/results_IP_camera.txt")
elif scan_choice == 4:
    os.system("masscan 0.0.0.0/0 -p22 --excludefile=exclude.txt --rate=10000 -oL scan_results/results_SSH.txt")
elif scan_choice == 5:
    os.system("masscan 0.0.0.0/0 -p1723,1701 --excludefile=exclude.txt --rate=10000 -oL scan_results/results_VPN.txt")
elif scan_choice == 6:
    os.system("masscan 0.0.0.0/0 -p21 --excludefile=exclude.txt --rate=10000 -oL scan_results/results_FTP.txt")
elif scan_choice == 7:
    os.system("masscan 0.0.0.0/0 -p2049 --excludefile=exclude.txt --rate=10000 -oL scan_results/results_NAS.txt")
elif scan_choice == 8:
    os.system("masscan 0.0.0.0/0 -p23 --excludefile=exclude.txt --rate=10000 -oL scan_results/results_Telnet.txt")
elif scan_choice == 9:
    os.system("masscan --top-ports 1000 -oL scan_results/open_ports.txt --exclude-file exclude.txt 0.0.0.0/0")
elif scan_choice == 10:
    os.system("masscan --ports 80,443 -oL scan_results/web_servers.txt --exclude-file exclude.txt 0.0.0.0/0")
elif scan_choice == 11:
    os.system("masscan --ports 1433,3306 -oL scan_results/database_servers.txt --exclude-file exclude.txt 0.0.0.0/0")
elif scan_choice == 12:
    os.system("masscan --ports 25,110,143,465,587 -oL scan_results/mail_servers.txt --exclude-file exclude.txt 0.0.0.0/0")
elif scan_choice == 13:
    os.system("masscan --ports 5900,6633,902 -oL scan_results/virtualization_hosts.txt --exclude-file exclude.txt 0.0.0.0/0")
elif scan_choice == 14:
    os.system("masscan -p9100,515 --exclude-file exclude.txt 0.0.0.0/0 -oL scan_results/printers.txt")
elif scan_choice == 15:
    os.system("masscan --ports 80,443 --source-port 65535 --rate=1000 --script 'http-wordpress-enum.nse' -oL scan_results/wp_sites.txt --exclude-file exclude.txt 0.0.0.0/0")
elif scan_choice == 16:
    os.system("masscan --ports 2375 -oL scan_results/docker_hosts.txt --exclude-file exclude.txt 0.0.0.0/0")
elif scan_choice == 17:
    os.system("masscan 0.0.0.0/0 -p502 --excludefile=exclude.txt --rate=10000 -oL scan_results/results_industrial_control_units.txt")
elif scan_choice == 99:
    print("Quiting")
else:
    print("Invalid choice. Please select a number between 1 and 17.")
