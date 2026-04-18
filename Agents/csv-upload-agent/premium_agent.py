import pandas as pd
import requests
import io
import os
from google.colab import files, drive

# 1. We use a 'Class' to organize what our Agent is and what it can do. 
# Think of a Class as a blueprint for a smart robot! By doing this, we bundle "data" and "skills" together.
class DataScienceAgent:
    """
     Automated Data Science Agent for Google Colab
    ----------------------------------------------
    A professional-grade agent developed to streamline data ingestion,
    preview, and analysis workflows.
    """
    
    # 2. '__init__' is the setup phase when we first turn the Agent on.
    def __init__(self):
        # 'self' allows the Agent to remember things over time.
        # 'self.df' will permanently store our data (dataframe) once it is loaded.
        self.df = None
        
        # 'self.active_file' stores the name of the last loaded file.
        self.active_file = None
        
        # When turned on, print a greeting
        print(" Agent: Online! I am your personal data science assistant.")
        print(" Quick Tip: Type 'help' to see what I can do for you.")

    # 3. Below are all of the Agent's "Skills" (also known as methods).
    def skill_upload(self):
        """Skill: Local File Ingestion"""
        print(" Opening browser file picker...")
        # Open a window so the user can upload a file directly into Colab
        uploaded = files.upload()
        
        # If they uploaded something
        if uploaded:
            # Save the file's name in the Agent's memory
            self.active_file = list(uploaded.keys())[0]
            
            # Convert the raw file data into a readable Pandas table
            self.df = pd.read_csv(io.BytesIO(uploaded[self.active_file]))
            print(f" Loaded {self.active_file} ({len(uploaded[self.active_file])} bytes)")
            
            # Trigger our other skill to preview the data
            self.skill_preview()

    def skill_fetch(self, url):
        """Skill: Remote URL Ingestion (True Automation)"""
        print(f" Synchronizing with remote resource: {url}...")
        try:
            # Go to the website URL and pull the text down
            response = requests.get(url)
            
            # Make sure there were no website errors (like a 404 Not Found)
            response.raise_for_status()
            
            # Read that raw text directly into our Pandas table
            self.df = pd.read_csv(io.StringIO(response.text))
            
            # Figure out the file name from the end of the URL
            self.active_file = url.split('/')[-1]
            print(f" Remote synchronization complete.")
            
            # Showcase the data visually
            self.skill_preview()
            
        except Exception as e:
            # If the website crashes or the URL is wrong
            print(f" Synchronization failed: {e}")

    def skill_drive(self):
        """Skill: Cloud Storage Integration"""
        print(" Mounting Google Drive ecosystem...")
        
        # Connects Google Drive so we can access our personal Google files in Colab
        drive.mount('/content/drive')
        print(" Cloud integration successful.")

    def skill_analyze(self):
        """Skill: Deep Neural Data Audit"""
        # If we haven't uploaded or fetched any data yet, we can't analyze anything
        if self.df is None:
            print(" Logic Error: No data found in buffer. Please 'upload' or 'fetch' data first.")
            return

        # 4. Display a clean, structured report of our currently loaded data
        print("\n" + "="*40)
        print(" DATA AUDIT REPORT (Beginner-Friendly)")
        print("="*40)
        
        print(f" Current File: {self.active_file}")
        
        # shape[0] gives us the number of Rows, shape[1] gives us Columns
        print(f" Size: {self.df.shape[0]} rows and {self.df.shape[1]} columns")
        
        print("\n Checking for Missing Data:")
        # Check if there are any blank/empty cells in our dataset
        nulls = self.df.isnull().sum()
        
        if nulls.any():
            print(" Note: Some columns have missing values:")
            print(nulls[nulls > 0]) # Only print the columns that actually have missing data
        else:
            print(" Perfect! No missing values found.")

        print("\n Fast Statistics (Averages, Min, Max):")
        # 'describe()' instantly calculates averages, maxes, mins, and percentiles for every column!
        print(self.df.describe().round(2))
        print("="*40)

    def skill_preview(self):
        """Skill: Visual Buffer Preview"""
        # If we have data, print the first 5 rows (using .head(5))
        if self.df is not None:
            print("\n Data Buffer Preview:")
            print(self.df.head(5))

    # 5. This is the endless loop that waits for user commands
    def main_loop(self):
        """Main Operator Interface"""
        while True:
            # Wait for user input. 
            # '.strip()' removes extra accidental spaces. '.lower()' makes it lowercase so capItaliZatiOn doesn't matter.
            cmd = input("\n[OPERATOR] > ").strip().lower()
            
            if cmd == 'exit':
                print(" Agent Offline. Terminating session...")
                break # 'break' shatters the loop and effectively ends the program!
                
            elif cmd == 'upload':
                # Fire the upload skill!
                self.skill_upload()
                
            elif cmd.startswith('fetch '):
                # Clean the command text to just keep the URL
                url = cmd.replace('fetch ', '')
                self.skill_fetch(url)
                
            elif cmd == 'drive':
                self.skill_drive()
                
            elif cmd == 'analyze':
                self.skill_analyze()
                
            elif cmd == 'help':
                # Show instructions
                print("\n AVAILABLE AGENT SKILLS:")
                print("  - upload  : Ingest local CSV file")
                print("  - fetch   : Ingest CSV from remote URL (e.g., fetch http://...)")
                print("  - drive   : Establish connection to Google Drive")
                print("  - analyze : Execute deep statistical audit")
                print("  - exit    : Shut down the agent system")
            else:
                # If they typed something random that we don't recognize
                print(f" Unrecognized command: '{cmd}'. Access 'help' for skill matrix.")

# 6. Actually start the agent and begin the loop
if __name__ == "__main__":
    # We "instantiate" the class. This means bringing our blueprint robot to life!
    agent = DataScienceAgent()
    
    # Now we let the agent start taking our commands
    agent.main_loop()
