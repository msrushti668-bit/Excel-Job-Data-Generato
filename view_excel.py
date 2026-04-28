import pandas as pd
import webbrowser
import os

excel_path = 'c:/Users/prabu/Downloads/hur/Task1_Completed.xlsx'
html_path = 'c:/Users/prabu/Downloads/hur/Task1_Completed.html'

try:
    xls = pd.ExcelFile(excel_path)
    html_content = "<html><head><style>table {border-collapse: collapse; width: 100%; margin-bottom: 20px;} th, td {border: 1px solid black; padding: 8px; text-align: left;} th {background-color: #f2f2f2;}</style></head><body>"
    html_content += "<h2>Excel Viewer: Task1_Completed.xlsx</h2>"
    
    for sheet in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet)
        html_content += f"<h3>Sheet: {sheet}</h3>"
        html_content += df.to_html(index=False)
        
    html_content += "</body></html>"
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    print(f"Opening HTML viewer at {html_path}")
    webbrowser.open('file://' + os.path.abspath(html_path))
    
except Exception as e:
    print(f"Error: {e}")
