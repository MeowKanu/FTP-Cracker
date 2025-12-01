# FTP Cracker Tool

This project includes two FTP brute-force tools: a basic version and an advanced multithreaded version. These scripts attempt username–password combinations against an FTP server to identify valid login credentials.

## Features

### Basic Version (ftp_brute.py)
- Hardcoded host, username, and password list
- Uses multithreading for faster brute-force
- Saves valid credentials to credentials.txt
- Simple and beginner-friendly

### Advanced Version (advanced_ftp_brute.py)
- Userlist + password list support
- Password generation using itertools
- argparse CLI interface
- Multithreaded brute-force
- Saves valid credentials
- Colored terminal output (colorama)

## Project Structure

ftp-cracker/
│── ftp_brute.py
│── advanced_ftp_brute.py
│── userlist.txt
│── passlist.txt
└── README.md

shell
Copy code

## Installation

Install colorama:

pip install colorama

shell
Copy code

## Usage

### Basic Version
python ftp_brute.py

shell
Copy code

### Advanced Version (Wordlists)
python advanced_ftp_brute.py --host 127.0.0.1 -U userlist.txt -P passlist.txt

shell
Copy code

### Advanced Version (Password Generation)
python advanced_ftp_brute.py --host 127.0.0.1 --generate --min 1 --max 3

pgsql
Copy code

## Notes

- Use on authorized systems only.
- Test on local FTP servers (vsftpd recommended).
- Large brute-force lengths take time.

## License

MIT License
