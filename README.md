# MyIpAddress
Easily get your public IP address along with LAN info and list all your open ports

myipar - Public IP, Network Interface Info, and Open Ports Viewer

This Python script (myipar.py) provides information about the public IP address, local network interface details, and open ports on your machine.
Usage:

  Install Dependencies:

  Before using the script, ensure that you have Python 3 installed. Additionally, you can run the provided install.sh script to automatically install the required psutil library:

  bash

    ./install.sh

The installation script will check for Python 3, install psutil if not present, and create a symbolic link to the script (myipar) in /usr/local/bin.

Run the Script:

After installation, you can use the following command to run the script:

bash

      myipar

The script will display the public IP address, local network interface information, and open ports on your machine.

Options:

  To list all open ports with service names, use the -p option:

  bash

      myipar -p


# Support

If you would like to supprot my efforts you can send me a few buck with BitCoin @ :`bc1qtezfajhysn6dut07m60vtg0s33jy8tqcvjqqzk`
