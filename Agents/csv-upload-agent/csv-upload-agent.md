# CSV Upload Agent (Colab Execution)

This is the ready-to-run file for the **CSV Upload Agent**. 

### Instructions:
1.  Open [Google Colab](https://colab.research.google.com/).
2.  Create a new notebook.
3.  Copy the code block below and paste it into a cell.
4.  Run the cell and follow the prompts in the output.

---

### Python Implementation

```python
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
        self.df = None
        self.active_file = None
        print("\033[1;32m[SYSTEM] Agent: Online!\033[0m")
        print("I am your personal data science assistant.")
        print("Quick Tip: Type 'help' to see my skills.")

    def skill_upload(self):
        print("\n[PROCESS] Opening browser file picker...")
        uploaded = files.upload()
        if uploaded:
            self.active_file = list(uploaded.keys())[0]
            self.df = pd.read_csv(io.BytesIO(uploaded[self.active_file]))
            print(f"\033[1;34m[SUCCESS]\033[0m Loaded {self.active_file}")
            self.skill_preview()

    def skill_fetch(self, url):
        print(f"\n[PROCESS] Syncing with remote resource...")
        try:
            response = requests.get(url)
            response.raise_for_status()
            self.df = pd.read_csv(io.StringIO(response.text))
            self.active_file = url.split('/')[-1]
            print(f"\033[1;34m[SUCCESS]\033[0m Remote synchronization complete.")
            self.skill_preview()
        except Exception as e:
            print(f"\033[1;31m[ERROR]\033[0m Synchronization failed: {e}")

    def skill_drive(self):
        print("\n[PROCESS] Mounting Google Drive...")
        drive.mount('/content/drive')
        print("\033[1;34m[SUCCESS]\033[0m Cloud integration successful.")

    def skill_analyze(self):
        if self.df is None:
            print("\033[1;31m[LIMITATION]\033[0m No data in buffer. Please 'upload' first.")
            return

        print("\n" + "="*40)
        print("DATA AUDIT REPORT")
        print("="*40)
        print(f"File: {self.active_file}")
        print(f"Shape: {self.df.shape[0]} rows x {self.df.shape[1]} cols")
        
        print("\nMissing Data Check:")
        nulls = self.df.isnull().sum()
        if nulls.any():
            print(nulls[nulls > 0])
        else:
            print("Perfect! No missing values.")

        print("\nStatistical Insight:")
        print(self.df.describe().round(2))
        print("="*40)

    def skill_preview(self):
        if self.df is not None:
            print("\n[PREVIEW] Top 5 Rows:")
            display(self.df.head(5))

    def main_loop(self):
        while True:
            cmd = input("\n[OPERATOR] > ").strip().lower()
            
            if cmd == 'exit':
                print("\033[1;33m[OFFLINE]\033[0m Terminating session...")
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
                print("\nAVAILABLE SKILLS:")
                print("  - upload  : Pick a file from your PC")
                print("  - fetch   : Download from a web link")
                print("  - drive   : Connect to Google Drive")
                print("  - analyze : Automatic math & missing data audit")
                print("  - exit    : Shut down agent")
            else:
                print(f"Unrecognized command: '{cmd}'. Type 'help'.")

if __name__ == "__main__":
    agent = DataScienceAgent()
    agent.main_loop()
```

---

### Learning Resources
*   [Full System Guide](AGENT_SYSTEM_GUIDE.md) - How it works under the hood.
*   [Student Walkthrough](student_walkthrough.md) - A beginner's guide to building this.
