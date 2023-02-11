<!DOCTYPE html>
<html>
  <body>
    <h1>Quick-Scanner</h1>
    <p>Quick-Scanner is a simple command-line tool written in Python that allows users to quickly scan for open ports on a target IP address.</p>
    <h2>Installation</h2>
    <p>To install Quick-Scanner, follow these steps:</p>
    <ol>
      <li>Clone the repository: <code>git clone https://github.com/dustinwloring1988/Quick-Scanner.git</code></li>
      <li>Run the setup script: <code>python setup.py install</code></li>
    </ol>
    <p>Note that the installation process may vary depending on your system configuration.</p>
    <h2>Usage</h2>
    <p>To use Quick-Scanner, simply run the <code>masscan-scanner.py</code> script and provide an IP address as an argument:</p>
    <pre><code>python masscan-scanner.py</code></pre>
    <p>The script will then scan all ports on the specified IP address and print out a list of open ports.</p>
    <p>You can also use the <code>nmap-scanner.py</code> script to grab the banner for a specific service running on a port:</p>
    <pre><code>python mnmap-scanner.py</code></pre>
    <p>The script will attempt to grab the banner for the service running on port 80 and print it to the console.</p>
    <p>Note that the <code>masscan-scanner.py</code> and <code>nmap-scanner.py</code> scripts are also included in the repository and can be used to perform port scans using the Masscan and Nmap tools, respectively.</p>
    <h2>Excluding Ports</h2>
    <p>If you need to exclude certain ports from the scanning process, you can add them to the <code>exclude.txt</code> file in the repository.</p>
    <p>The file already contains a few commonly excluded ports, but you can add or remove ports from the list as needed.</p>
    <h2>License</h2>
    <p>Quick-Scanner is released under the MIT License.</p>
  </body>
</html>
