# Huds-Log-Sanitizer User Guide

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Main Features](#main-features)
4. [Using Hud-Log-Sanitizer](#using-hud-log-sanitizer)
   - [Log Reconnaissance](#log-reconnaissance)
   - [Sanitizing Log Files](#sanitizing-log-files)
5. [Configuration](#configuration)
6. [Troubleshooting](#troubleshooting)
7. [Contact](#contact)

---

## Introduction

Hud-Log-Sanitizer (HLS v2.0) is a powerful tool designed to help data analysts and organizations sanitize log files for external or public use. It ensures that sensitive information in log files is masked or replaced, enhancing data security while maintaining the usability of the log data.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following:
- A UNIX-based operating system
- Python installed on your system

### Installation

1. **Download Hud-Log-Sanitizer:**
   Visit the official website or repository and download the latest version of Hud-Log-Sanitizer.

2. **Install the Tool:**
   Extract the downloaded package to your preferred directory.

## Main Features

- **Log Reconnaissance:** Identify the structure and components of your log files.
- **Sanitization:** Replace sensitive information in log files with predefined values.
- **Customization:** Configure the tool to suit specific log formats and sanitization needs.

## Using Hud-Log-Sanitizer

### Log Reconnaissance

Before sanitizing log files, it is essential to understand their structure. Log reconnaissance allows you to view the components of your log files.

**Steps:**

1. Open your terminal.
2. Navigate to the Hud-Log-Sanitizer directory.
3. Run the reconnaissance command:
   ```sh
   python main.py --check --logfile /path/to/your/logfile
   ```
   Replace `/path/to/your/logfile` with the actual path to your log file.

**Outcome:**
The tool will display the different fields present in the log file, helping you understand what information needs to be sanitized.

### Sanitizing Log Files

Once you have identified the fields in your log files, you can proceed to sanitize them.

**Steps:**

1. Open your terminal.
2. Navigate to the Hud-Log-Sanitizer directory.
3. Run the sanitization command:
   ```sh
   python main.py --logfile /path/to/your/logfile --numbers
   ```
   Replace `/path/to/your/logfile` with the actual path to your log file.

**Outcome:**
The tool will process the log file and replace sensitive information with predefined values, producing a sanitized log file.

## Configuration

Hud-Log-Sanitizer allows you to customize which fields are sanitized and how they are replaced.

**Steps:**

1. Open the `vocabulary.py` file in the Hud-Log-Sanitizer directory.
2. Edit the file to specify the fields and their replacement values.

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
Modify the values as needed to match your log file's structure and the sanitization requirements.

## Troubleshooting

### Common Issues

1. **File Not Found:**
   Ensure the path to the log file is correct and the file exists.

2. **Permission Denied:**
   Ensure you have the necessary permissions to read and write the log file.

3. **Invalid Arguments:**
   Double-check the command-line arguments for typos or missing values. Use the help command for guidance:
   ```sh
   python main.py --help
   ```

## Contact

For any inquiries or support, please contact:

Hud Seidu Daannaa  
[www.daannaa.space](http://www.daannaa.space)  
[Email](mailto:info@daannaa.space)

---

Design By Hud Seidu Daannaa
