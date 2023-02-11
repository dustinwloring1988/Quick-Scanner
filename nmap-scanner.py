# nmap.py

import os

def scan_type():
    print(" Selecte a number below to preform a detailed scan using nmap ajinst a ip and port list and save the results ")
    print("1. Web servers (ports 80, 443)")
    print("2. Database servers (ports 1433, 3306)")
    print("3. Mail servers (ports 25, 110, 143, 465, 587)")
    print("4. Virtualization hosts (ports 5900, 6633, 902)")
    print("5. Router Check for login")
    print("6. Check for open WP sites")
    print("7. Check for open printers")
    print("8. Check for docker hosts")
    print("9. Screenshot of service RDP")
    print("10. Screenshot of service SNMP")
    print("11. Screenshot of service Cameras")
    print("12. Screenshot of service SSH")
    print("13. Screenshot of service VPN")
    print("14. Screenshot of service FTP")
    print("15. Screenshot of service NAS")
    print("16. Screenshot of industrial control units services")
    print("17. Copmmon vulnerabilites for industrial control units services")
    print("99. This will exit the program")
    choice = input("Choose a scan type (1-1): ")
    return choice

def screenshot_RPD():
    with open("scan_results/results_RPD.txt") as f:
        for line in f:
            ip, port = line.strip().split()
            os.system(f"nmap -p {port} --script http-screenshot {ip} -oN screenshots/{ip}_{port}_screenshot.txt")

def screenshot_SNMP():
    with open("scan_results/results_SNMP.txt") as f:
        for line in f:
            ip, port = line.strip().split()
            os.system(f"nmap -p {port} --script http-screenshot {ip} -oN screenshots/{ip}_{port}_screenshot.txt")

def screenshot_Cameras():
    with open("scan_results/results_IP_camera.txt") as f:
        for line in f:
            ip, port = line.strip().split()
            os.system(f"nmap -p {port} --script http-screenshot {ip} -oN screenshots/{ip}_{port}_screenshot.txt")

def screenshot_SSH():
    with open("scan_results/results_SSH.txt") as f:
        for line in f:
            ip, port = line.strip().split()
            os.system(f"nmap -p {port} --script http-screenshot {ip} -oN screenshots/{ip}_{port}_screenshot.txt")

def screenshot_VPN():
    with open("scan_results/results_VPN.txt") as f:
        for line in f:
            ip, port = line.strip().split()
            os.system(f"nmap -p {port} --script http-screenshot {ip} -oN screenshots/{ip}_{port}_screenshot.txt")

def screenshot_FTP():
    with open("scan_results/results_FTP.txt") as f:
        for line in f:
            ip, port = line.strip().split()
            os.system(f"nmap -p {port} --script http-screenshot {ip} -oN screenshots/{ip}_{port}_screenshot.txt")

def screenshot_NAS():
    with open("scan_results/results_NAS.txt") as f:
        for line in f:
            ip, port = line.strip().split()
            os.system(f"nmap -p {port} --script http-screenshot {ip} -oN screenshots/{ip}_{port}_screenshot.txt")

def screenshot_ICU():
    with open("scan_results/results_industrial_control_units.txt") as f:
        for line in f:
            ip, port = line.strip().split()
            os.system(f"nmap -p {port} --script http-screenshot {ip} -oN screenshots/{ip}_{port}_screenshot.txt")

def web_servers():
    os.system("nmap -sV -p 80,443 -iL scan_results/web_servers.txt -oN vuln/web_servers_detailed.txt")

def database_servers():
    os.system("nmap -sV -p 1433,3306 -iL scan_results/database_servers.txt -oN vuln/database_servers_detailed.txt")

def mail_servers():
    os.system("nmap -sV -p 25,110,143,465,587 -iL scan_results/mail_servers.txt -oN vuln/mail_servers_detailed.txt")

def virtualization_hosts():
    os.system("nmap -sV -p 5900,6633,902 -iL scan_results/virtualization_hosts.txt -oN vuln/virtualization_hosts_detailed.txt")

def check_router_security():
    os.system("nmap -sV --script "auth and safe" -iL scan_results/results_Telnet.txt -oN vuln/vulnerable_routers.txt")

def check_wp_sites():
    os.system("nmap --script=http-enum,http-waf-detect,http-sql-injection,http-vuln-cve-2014-0160 -iL scan_results/wp_sites.txt -p 80,443 -oN vuln/wp_sites.txt")

def check_printers():
    os.system("nmap -p9100,515 -iL scan_results/printers.txt --script printer-info,pjl-hp-laserjet-info,cups-info --script-args=unsafe=1 -oA vuln/printers_scan_results")

def docker_version():
    os.system("nmap -sV --script=docker-version -iL scan_results/docker_hosts.txt -oG vuln/open_dockers.txt")

def vuln_ICU():
    os.system("nmap -p 502 --script ics-vulnerabilities.nse -iL scan_results/industrial_control_units.txt" -oG vuln/open_ICUs.txt)

if __name__ == "__main__":
    choice = scan_type()
    if choice == "1":
        web_servers()
    elif choice == "2":
        database_servers()
    elif choice == "3":
        mail_servers()
    elif choice == "4":
        virtualization_hosts()
    elif choice == "5":
        check_router_security()
    elif choice == "6":
        check_wp_sites()
    elif choice == "7":
        check_printers()
    elif choice == "8":
        docker_version()
    elif choice == "9":
        screenshot_RDP()
    elif choice == "10":
        screenshot_SNMP()
    elif choice == "11":
        screenshot_Cameras()
    elif choice == "12":
        screenshot_SSH()
    elif choice == "13":
        screenshot_VPN()
    elif choice == "14":
        screenshot_FTP()
    elif choice == "15":
        screenshot_NAS()
    elif choice == "16":
        screenshot_ICU()
    elif choice == "99":
        print("Quitting")
    else:
        print("Invalid selection. Try again.")
