# warp
Set markers in the file system to easily go to them.
## Usage
Add a marker in the current directory or anywhere else:
    warp add [name] Optional:[path]
List all markers
    warp list
Remove a marker
    warp remove [name]
Go to marker
    warp [name]
## Installation
Clone the repository
    git clone https://github.com/bergziegenmichi/warp.git ~/.warp
Create an empty markers.txt file
    touch ~/.warp/markers.txt
Source the shell script
    source ~/.warp/warp.sh
To do this automatically
    echo "\nsource ~/.warp/warp.sh\n" >> ~/.bashrc

