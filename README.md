<!DOCTYPE html>
<html>
  <body>
    <h1>Quick-Scanner</h1>
    <p>Quick-Scanner is a simple command-line tool written in Python that allows users to quickly scan for open ports on a target IP address.</p>
    <p>Quick-Scanner simplifies network scanning and makes it accessible to everyone. Try it out today and see how it can benefit you. </p>
    <h2>Installation</h2>
    <p>To install Quick-Scanner, follow these steps:</p>
    <ol>
      <li>Clone the repository: <code>git clone https://github.com/dustinwloring1988/Quick-Scanner.git</code></li>
      <li>Run the setup script: <code>python setup.py</code></li>
    </ol>
    <p>Note that the installation process may vary depending on your system configuration.</p>
    <h2>Usage</h2>
    <p>To use Quick-Scanner, simply run the <code>masscan-scanner.py</code> then selecte a scan to run. It will save teh results for later</p>
    <pre><code>python masscan-scanner.py</code></pre>
    <p>The script will run and you will just selecte from an option available</p>
    <p>Next you would use the <code>nmap-scanner.py</code> script to use the target list that you generated in the script above:</p>
    <pre><code>python mnmap-scanner.py</code></pre>
    <p>The script will run and you will just selecte from an option available</p>
    <h2>Excluding Ports</h2>
    <p>If you need to exclude certain ports from the scanning process, you can add them to the <code>exclude.txt</code> file in the repository.</p>
    <p>The file already contains a few commonly excluded ports, but you can add or remove ports from the list as needed.</p>
    <h2>License</h2>
    <p>Quick-Scanner is released under no License as it was made by AI.</p>
  </body>
</html>
