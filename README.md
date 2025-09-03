# Python QR Code Validator — COMP 202

This project was developed as part of COMP 202 (Foundations of Programming) at McGill University.  
It implements a **QR Code validation system** in Python using Object-Oriented Programming.

## Highlights
- Implemented `helper.py` with utility functions:
  - `convert_date` for parsing and validating date strings.
  - `get_data` for reading binary QR code data from text files.
- Implemented `txtdata.py` with a `TxtData` class:
  - Stores and manipulates 2D QR data.
  - Includes methods for pixel counting, equality checks, and exporting a “pretty” QR code.
- Implemented `qrcode.py` with a `QRCode` class:
  - Stores QR metadata (owner, last update date, error correction).
  - Includes methods to validate corruption and compare QR codes.
- Applied **file input/output, exception handling, and modular OOP design**.

## Tech
- **Python 3**
- Object-Oriented Programming (OOP)
- File I/O and exception handling
- Nested lists & dictionaries

## Notes
- This repo includes only my authored Python files (`helper.py`, `txtdata.py`, `qrcode.py`).  
- Assignment test data (`.txt` files) and instructions are excluded per course policy.
