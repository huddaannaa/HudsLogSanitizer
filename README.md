# Huds-Log-Sanitizer Documentation

![HLST](./hudslogsanitizer.png)

## Table of Contents

1. [Introduction](#introduction)
2. [Benefits of Log Sanitization in Cyber Security](#benefits-of-log-sanitization-in-cyber-security)
3. [Software Requirements](#software-requirements)
4. [About the Program](#about-the-program)
5. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
6. [Directory Structure](#directory-structure)
   - [Directory Details](#directory-details)
7. [Usage](#usage)
   - [Command-Line Arguments](#command-line-arguments)
   - [Example Usage](#example-usage)
8. [Configuration](#configuration)
   - [Vocabulary Configuration](#vocabulary-configuration)
   - [Topology Configuration](#topology-configuration)
9. [Onboarding New Parsers](#onboarding-new-parsers)
   - [Step 1: Define Regex Pattern](#step-1-define-regex-pattern)
   - [Step 2: Create Topology](#step-2-create-topology)
   - [Step 3 (Optional): Modify Definitions](#step-3-optional-modify-definitions)
10. [Best Practices for Security Tools Documentation](#best-practices-for-security-tools-documentation)
11. [Troubleshooting](#troubleshooting)
    - [Common Issues](#common-issues)
12. [Contributing](#contributing)
13. [License](#license)
14. [Contact](#contact)

---

## Introduction

Hud-Log-Sanitizer (HLS v2.0) is a powerful log sanitization tool designed to enhance data security for organizations handling sensitive log data. In the era of increasing cyber threats, ensuring that sensitive information within log files is protected before sharing or analyzing externally is crucial. This tool helps by sanitizing log files, removing or obfuscating sensitive information, making it safe for external/public use without compromising security.

## Benefits of Log Sanitization in Cyber Security

Log sanitization plays a critical role in maintaining the confidentiality and integrity of an organization's data. Here are some of the key benefits:

1. **Data Privacy:** Sanitizing logs helps protect sensitive information such as IP addresses, user credentials, and other personal data from unauthorized access.
2. **Compliance:** Ensures adherence to regulatory requirements and standards such as GDPR, HIPAA, and other data protection laws by masking or removing sensitive information from logs.
3. **Security:** Reduces the risk of data breaches by ensuring that logs do not contain exploitable information that could be used by attackers.
4. **Data Sharing:** Enables safe sharing of logs with third parties, such as consultants or partners, by removing sensitive information that could compromise security.
5. **Incident Response:** Sanitized logs can be used in incident response without exposing sensitive data, facilitating quicker and safer analysis.

By implementing log sanitization, organizations can significantly enhance their cybersecurity posture and ensure that sensitive information is protected at all stages of log management.

## Software Requirements

- UNIX-based operating system
- Python

## About the Program

Hud-Log-Sanitizer (HLS v2.0) is a log sanitizer tool designed to help data analysts and entities working in log-defined environments. The goal is to boost data security by editing log files for external/public use outside a given organization. The tool converts a sample log to a sanitized file.

## Getting Started

### Prerequisites
Ensure you have the following installed:
- UNIX-based operating system
- Python

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/username/hud-log-sanitizer.git
    ```
2. Navigate to the project directory:
    ```sh
    cd hud-log-sanitizer
    ```

## Directory Structure

```
hud-log-sanitizer/
├── checker.py
├── clear-logs.sh
├── definitions.py
├── functions.py
├── get_parsers.py
├── LICENSE
├── main.py
├── parse.hud
├── README.md
├── sanitized/
├── topologies.py
└── vocabulary.py
```

### Directory Details
- **checker.py:** Responsible for log reconnaissance.
- **clear-logs.sh:** Script to clean the `sanitized` log directory.
- **definitions.py:** Contains mappings between topologies and patterns.
- **functions.py:** Contains custom or local functions for the program.
- **get_parsers.py:** Retrieves parsers from `parse.hud`.
- **LICENSE:** License information.
- **main.py:** Main entry point of the application.
- **parse.hud:** Contains regex patterns and mappings.
- **README.md:** Documentation for the application.
- **sanitized/:** Directory containing the final sanitized log files.
- **topologies.py:** Contains parser configurations for customization.
- **vocabulary.py:** Contains mappings for fields to be changed.

## Usage

### Command-Line Arguments

```sh
python -B main.py --help
```

**Output:**
```
usage: main.py [-h] [-l] -f [-c] [-n]

Hud-Log-Sanitizer (HLS v2.0) This is a log sanitizer tool designed by Hud
Seidu Daannaa, to help data analysts and entities working in a log-defined
environment. The goal is to boost data security by editing log files
(documents) for external/public use, outside a given organization. The tool
will convert a sample log to a sanitized file. For usage, refer to README.md.

optional arguments:
  -h, --help       Show this help message and exit.
  -l, --lines      Specify the number of lines (events) to sanitize; if not
                   specified, the tool will scan all lines in the specified
                   document.
  -f, --logfile    Specify the path of a log file to sanitize.
  -c, --check      Provides the analyst with the components (fields) of the
                   log file, using the log event with the highest amount of data.
  -n, --numbers    This will switch/replace (randomize) all numbers in the log
                   document.
```

### Example Usage

1. **Log Reconnaissance:**
    ```sh
    python -B main.py -c -f /path/to/logfile
    ```

2. **Sanitize Log File:**
    ```sh
    python -B main.py -f /path/to/logfile -n
    ```

## Configuration

### Vocabulary Configuration
Edit `vocabulary.py` to specify the fields you wish to replace or switch during the sanitization process.

**Example:**
```python
strings = {
    'local': 'xxx',
    'Local': 'xxx',
    'LOCAL': 'xxx',
    'Windows': 'mint',
    'server': 'ostname',
    'information': 'trollr',
    'domain': 'main',
    'systemprofile': 'yt'
}
```

### Topology Configuration
Topologies are defined in `topologies.py` and are used to customize or add additional functionalities.

**Example:**
```python
def x(parserx, patternx, elds, file_, variable):
    new = ''
    for field in re.findall(r'{}'.format(patternx), elds):
        sed(str(field.strip()), new, file_)
        print("[***] Replaced: ", old, " [//=] with: ", new)
```

## Onboarding New Parsers

### Step 1: Define Regex Pattern
**File:** `parse.hud`

Create a regex pattern to search for specific entities.

**Example:**
```python
strings = r'\b\w+\b'
```

### Step 2: Create Topology
**File:** `topologies.py`

Follow the template to create a topology.

**Example:**
```python
def x(parserx, patternx, elds, file_, variable):
    new = ''
    for field in re.findall(r'{}'.format(patternx), elds):
        sed(str(field.strip()), new, file_)
        print("[***] Replaced: ", old, " [//=] with: ", new)

# Details:
# parserx: Name of the parser (converted to a variable to access strings in vocabulary)
# patternx: Contains the regex sample
# elds: Event data from the log file being looped from main.py
# file_: Name of the original logfile (used for text replacement or naming)
```

### Step 3 (Optional): Modify Definitions
**File:** `definitions.py`

Override the automatic mapping if necessary.

**Example:**
```python
program['key'] = value
```
Where `key` is the defined parser/pattern and `value` is the function defined in topologies.

**Note:** This file does automatic mapping; the exception section redefines or overrides the automatic mapping.

## Best Practices for Security Tools Documentation

1. **Clarity and Precision:** Ensure that the instructions are clear, precise, and easy to follow.
2. **Code Examples:** Provide code examples to illustrate usage and configuration.
3. **Directory Structure:** Clearly explain the directory structure and the purpose of each file.
4. **Command-Line Usage:** Document all command-line arguments and their purpose.
5. **Configuration Details:** Explain configuration files and how to modify them.
6. **Error Handling:** Provide information on common errors and troubleshooting steps.
7. **Security Considerations:** Highlight any security considerations or best practices for using the tool.

## Troubleshooting

### Common Issues

1. **File Not Found:**
    Ensure the specified log file path is correct.
    ```sh
    python -B main.py -f /correct/path/to/logfile
    ```

2. **Permission Denied:**
    Ensure you have the necessary permissions to read/write the log file.
    ```sh
    sudo python -B main.py -f /path/to/logfile
    ```

3. **Invalid Arguments:**
    Check the command-line arguments for any typos or missing values.
    ```sh
    python -B main.py --help
    ```

## Contributing
1. Fork the repository.
2. Create a new branch.
    ```sh
    git checkout -b feature-branch
    ```
3. Make your changes.
4. Commit your changes.
    ```sh
    git commit -m "Add new feature"
    ```
5. Push to the branch.
    ```sh
    git push origin feature-branch
    ```
6. Create a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any inquiries, please contact:
Hud Seidu Daannaa  
[www.daannaa.space](http://www.daannaa.space)  
[Email](mailto:hdaannaa@gmail.com)
