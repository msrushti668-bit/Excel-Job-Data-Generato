# Excel Job Data Generator and Viewer

This project contains two Python scripts designed to work together. The first script generates an Excel file populated with job data, and the second script provides a simple way to view this data in a web browser.

## Files

*   `generate_excel.py`: This script creates an Excel file named `Task1_Completed.xlsx`. It contains multiple sheets with job listings from different organizations (AAU, CSIR, NHM, NTPC, TANUVAS) and an additional sheet with AI feature ideas.

*   `view_excel.py`: This utility reads the `Task1_Completed.xlsx` file, converts its content into an HTML format, and opens it in your default web browser for easy viewing.

## Prerequisites

Ensure you have Python installed. You will also need the following libraries, which can be installed using pip:

```bash
pip install pandas openpyxl
```

## How to Use

1.  **Generate the Data:**
    First, run the `generate_excel.py` script. This will create the `Task1_Completed.xlsx` file in the current directory.
    ```bash
    python c:\Users\prabu\Downloads\hur\generate_excel.py
    ```

2.  **View the Data:**
    Once the Excel file is created, run the `view_excel.py` script to see the data presented in your browser.
    ```bash
    python c:\Users\prabu\Downloads\hur\view_excel.py
    ```