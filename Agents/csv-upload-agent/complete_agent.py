# 1. We import necessary tools
from google.colab import files  # Tool to let us upload files in Google Colab inside the browser
import pandas as pd             # Tool to handle and analyze data (like spreadsheets)

def data_agent(command):
    # This function is our "Agent". We give it a command, and it does the work!
    
    # 2. Check if the command is "upload csv" (ignoring uppercase vs lowercase)
    if command.lower() == 'upload csv':
        print(' Agent: Starting CSV auto-upload...')
        
        # 3. This opens a file picker box so the user can select their CSV file
        uploaded = files.upload()
        
        # 4. If nothing was uploaded (maybe they clicked cancel)
        if not uploaded:
            print(' No file chosen. Try again.')
            return # Stop right here and go no further
        
        # 5. Look at each file they uploaded 
        # (usually it's just one, but we loop just in case!)
        for fn in uploaded.keys():
            print(f' Uploaded: {fn} ({len(uploaded[fn])} bytes)')
            try:
                # 6. Read the CSV file into pandas (which we call our dataframe, or 'df')
                df = pd.read_csv(fn)
                
                # 7. Print out some helpful details about the file
                print(f'\n Data Summary:')
                
                # 'shape' tells us (Number of Rows, Number of Columns)
                print(f'Shape: {df.shape}')
                
                # 'columns' tells us the names of the headers
                print(f'Columns: {df.columns.tolist()}')
                
                # 'dtypes' tells us what type of data is in each column (text, numbers, etc.)
                print(f'Dtypes:\n{df.dtypes}')
                
                # 8. Show the first 5 rows just to make sure it looks good!
                print('\n Preview:')
                print(df.head())
                
            except Exception as e:
                # 9. Oh no! If there is an error reading the file, tell the user what went wrong
                print(f' Load failed: {e}')
                print(' Tip: Try encoding="latin1" or check CSV format.')
    else:
        # 10. If the user typed anything other than "upload csv"
        print(" Command not recognized. Use: 'upload csv'")

# 11. Start our program here
if __name__ == "__main__":
    # Ask the user what they want to do
    cmd = input('Enter command: ')
    
    # Send their reply into our agent function
    data_agent(cmd)
