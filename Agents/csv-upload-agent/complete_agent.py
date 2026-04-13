from google.colab import files
import pandas as pd

def data_agent(command):
    # \"\"\"Auto CSV Upload Agent for Google Colab - Enhanced for students.\"\"\"
    
    if command.lower() == 'upload csv':
        print(' Agent: Starting CSV auto-upload...')
        uploaded = files.upload()
        
        if not uploaded:
            print(' No file chosen. Try again.')
            return
        
        for fn in uploaded.keys():
            print(f' Uploaded: {fn} ({len(uploaded[fn])} bytes)')
            try:
                df = pd.read_csv(fn)
                print(f'\n Data Summary:')
                print(f'Shape: {df.shape}')
                print(f'Columns: {df.columns.tolist()}')
                print(f'Dtypes:\n{df.dtypes}')
                print('\n Preview:')
                print(df.head())
            except Exception as e:
                print(f' Load failed: {e}')
                print(' Tip: Try encoding="latin1" or check CSV format.')
    else:
        print(\" Command not recognized. Use: 'upload csv'\")

# Run agent
if __name__ == \"__main__\":
    cmd = input('Enter command: ')
    data_agent(cmd)
