import pandas as pd
import requests
import io
import os
from google.colab import files, drive

class DataScienceAgent:
    """
     Automated Data Science Agent for Google Colab
    ----------------------------------------------
    A professional-grade agent developed to streamline data ingestion,
    preview, and analysis workflows.
    """
    
    def __init__(self):
        # self.df will store our data once it is loaded
        self.df = None
        # self.active_file stores the name of the last loaded file
        self.active_file = None
        print(" Agent: Online! I am your personal data science assistant.")
        print(" Quick Tip: Type 'help' to see what I can do for you.")

    def skill_upload(self):
        """Skill: Local File Ingestion"""
        print(" Opening browser file picker...")
        uploaded = files.upload()
        if uploaded:
            self.active_file = list(uploaded.keys())[0]
            self.df = pd.read_csv(io.BytesIO(uploaded[self.active_file]))
            print(f" Loaded {self.active_file} ({len(uploaded[self.active_file])} bytes)")
            self.skill_preview()

    def skill_fetch(self, url):
        """Skill: Remote URL Ingestion (True Automation)"""
        print(f" Synchronizing with remote resource: {url}...")
        try:
            response = requests.get(url)
            response.raise_for_status()
            self.df = pd.read_csv(io.StringIO(response.text))
            self.active_file = url.split('/')[-1]
            print(f" Remote synchronization complete.")
            self.skill_preview()
        except Exception as e:
            print(f" Synchronization failed: {e}")

    def skill_drive(self):
        """Skill: Cloud Storage Integration"""
        print(" Mounting Google Drive ecosystem...")
        drive.mount('/content/drive')
        print(" Cloud integration successful.")

    def skill_analyze(self):
        """Skill: Deep Neural Data Audit"""
        if self.df is None:
            print(" Logic Error: No data found in buffer. Please 'upload' or 'fetch' data first.")
            return

        print("\n" + "="*40)
        print(" DATA AUDIT REPORT (Beginner-Friendly)")
        print("="*40)
        print(f" Current File: {self.active_file}")
        print(f" Size: {self.df.shape[0]} rows and {self.df.shape[1]} columns")
        
        print("\n Checking for Missing Data:")
        nulls = self.df.isnull().sum()
        if nulls.any():
            print(" Note: Some columns have missing values:")
            print(nulls[nulls > 0])
        else:
            print(" Perfect! No missing values found.")

        print("\n Fast Statistics (Averages, Min, Max):")
        print(self.df.describe().round(2))
        print("="*40)

    def skill_preview(self):
        """Skill: Visual Buffer Preview"""
        if self.df is not None:
            print("\n Data Buffer Preview:")
            print(self.df.head(5))

    def main_loop(self):
        """Main Operator Interface"""
        while True:
            cmd = input("\n[OPERATOR] > ").strip().lower()
            
            if cmd == 'exit':
                print(" Agent Offline. Terminating session...")
                break
            elif cmd == 'upload':
                self.skill_upload()
            elif cmd.startswith('fetch '):
                url = cmd.replace('fetch ', '')
                self.skill_fetch(url)
            elif cmd == 'drive':
                self.skill_drive()
            elif cmd == 'analyze':
                self.skill_analyze()
            elif cmd == 'help':
                print("\n AVAILABLE AGENT SKILLS:")
                print("  - upload  : Ingest local CSV file")
                print("  - fetch   : Ingest CSV from remote URL (e.g., fetch http://...)")
                print("  - drive   : Establish connection to Google Drive")
                print("  - analyze : Execute deep statistical audit")
                print("  - exit    : Shut down the agent system")
            else:
                print(f" Unrecognized command: '{cmd}'. Access 'help' for skill matrix.")

if __name__ == "__main__":
    agent = DataScienceAgent()
    agent.main_loop()
