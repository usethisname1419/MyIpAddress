#!/bin/bash


if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3 and try again."
    exit 1
fi


if ! python3 -c "import psutil" &> /dev/null; then
    echo "Installing 'psutil'..."
    python3 -m pip install psutil
    if [ $? -ne 0 ]; then
        echo "Error: Failed to install 'psutil'. Please install it manually and try again."
        exit 1
    fi
    echo "'psutil' installed successfully."
fi


ln -s "$(pwd)/myipar.py" /usr/local/bin/myipar

echo "Installation completed. You can now use 'myipar' from the terminal."
