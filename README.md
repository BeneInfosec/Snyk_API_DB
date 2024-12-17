# Snyk_API_DB
The Snyk Vulnerability Database contains a comprehensive list of known security vulnerabilities. This provides the key security information used by Snyk products to find and fix code vulnerabilities.

To utilize the informations of the Database, I created a script that performs requests to search for vulnerabilities in the Snyk Vulnerability Database using specific keywords (e.g., log4j or react).
For each search, the script retrieves essential information, including:
- Vulnerability details
- Affected package
- Severity/Criticality

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/BeneInfosec/Snyk_API_DB.git
   cd Snyk_API_DB
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with Python:
```bash
python script.py
```
