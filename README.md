# Python Security Log Analyzer

A command-line cybersecurity learning project built with Python. The tool scans log files for IP addresses, compares them against an authorized IP allowlist, and records the results in a report. It also uses SHA-256 hashing to verify the integrity of the authorized IP file before scanning.

This project was developed to practise Python programming concepts through a practical security-focused application.

## Features

- **Command-line interface:** Accepts a log file or directory and an authorized IP file as arguments.
- **Recursive log scanning:** Searches directories for `.log` files using `pathlib`.
- **IP extraction:** Uses regular expressions to extract IPv4-shaped strings from log entries.
- **Allowlist comparison:** Compares extracted IP addresses against a set of authorized addresses.
- **SHA-256 integrity check:** Calculates the hash of the authorized IP file and compares it against a predefined expected hash.
- **File handling:** Processes log files line by line to avoid loading entire log files into memory.
- **Error handling:** Handles common file access and filesystem errors.
- **Scan reporting:** Appends authorized and unauthorized IP findings to `logger.txt`.
- **Virtual environment exclusion:** Skips files located inside `venv` and `.venv` directories.

## Technologies Used

- Python 3
- `pathlib` — filesystem navigation
- `re` — regular expressions
- `sys` — command-line arguments
- `hashlib` — SHA-256 hashing

All listed modules are part of Python's standard library.

## Requirements

- Python 3
- A text-based log file or directory containing `.log` files
- An authorized IP file containing IP addresses
- A matching SHA-256 hash configured in the script

No third-party Python packages are required.

## Project Structure

```text
python-security-log-analyzer/
├── ipan.py
├── c.txt              # Authorized IP allowlist
├── logger.txt         # Generated scan report
├── logs/              # Sample log files
└── README.md
```

The filenames and directory structure can be adjusted to suit your environment.

## Installation

Clone the repository:

```bash
git clone <YOUR_REPOSITORY_URL>
```

Navigate into the project directory:

```bash
cd python-security-log-analyzer
```

Make sure Python 3 is installed:

```bash
python --version
```

On some systems, use `python3` instead.

## Usage

Pass two arguments to the script:

1. The path to a log file or directory.
2. The path to the authorized IP file.

### Scan a directory

```bash
python ipan.py "./logs" "./c.txt"
```

### Scan a single log file

```bash
python ipan.py "./logs/server.log" "./c.txt"
```

Use paths appropriate for your operating system.

## How It Works

1. **Verify integrity:** The program calculates the SHA-256 hash of the authorized IP file and compares it with the expected hash.
2. **Validate arguments and paths:** It checks that the required command-line arguments and paths are present.
3. **Load the allowlist:** The authorized IP addresses are extracted and stored in a Python set.
4. **Discover log files:** The program finds `.log` files recursively or processes a single specified file.
5. **Extract IP candidates:** Each log line is processed using a regular expression.
6. **Compare addresses:** Each extracted candidate is checked against the authorized IP set.
7. **Write results:** Findings are appended to `logger.txt`.

## Example Output

```text
Authorized : 192.168.1.10
NOT AUTHORIZED : 192.168.1.25
Authorized : 10.0.0.5
```

These results indicate whether an extracted IP address appears in the supplied allowlist. An unauthorized result does not automatically mean the IP is malicious.

## Current Limitations

- The regular expression extracts IPv4-shaped candidates but does not yet validate whether every candidate is a valid IPv4 address.
- The authorized IP file's expected SHA-256 hash is hardcoded in the script.
- The current hash verification checks integrity against a predefined value; the expected hash must itself be obtained and stored securely.
- The scanner identifies addresses absent from the allowlist, not necessarily malicious addresses.
- Results are appended to `logger.txt`, so repeated runs may add duplicate findings.
- The tool is a learning project, not a replacement for a production SIEM or endpoint detection system.

## Planned Improvements

- [ ] Add strict IPv4 validation using Python's `ipaddress` module.
- [ ] Improve scan reporting with timestamps and file references.
- [ ] Add summary statistics for unique authorized and unauthorized addresses.
- [ ] Improve handling of large datasets and repeated findings.

## Learning Outcomes

This project provided practical experience with:

- Python file I/O and context managers
- Filesystem traversal with `pathlib`
- Loops, conditions, lists, and sets
- Regular expressions and text parsing
- Command-line argument handling
- Exception handling
- SHA-256 hashing and file integrity verification
- Basic security log analysis and allowlist matching

## Disclaimer

This project is intended for educational use and authorized defensive analysis. Use it only with log files and data you have permission to examine.

## Author

Developed as a personal Python-for-cybersecurity learning project.
