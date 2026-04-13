import os
import sys
import time
from playwright.sync_api import sync_playwright

def auto_upload_agent():
    print(" Agent: Premium Colab Uploader Booting...")
    
    # 1. Ask for file path
    file_path = input("\n Please enter the full path to your CSV file: ").strip()
    
    # Cleanup path (remove quotes if user drag-and-dropped)
    file_path = file_path.replace('"', '').replace("'", "")
    
    if not os.path.exists(file_path):
        print(f" Error: File not found at '{file_path}'")
        return

    print(f" Target acquired: {os.path.basename(file_path)}")

    with sync_playwright() as p:
        print(" launching browser...")
        # Use channel='chrome' or 'msedge' if available for better compatibility with Google accounts
        browser = p.chromium.launch(headless=False) 
        context = browser.new_context()
        page = context.new_page()

        print(" Navigating to Google Colab...")
        page.goto("https://colab.research.google.com/")

        # 2. Check for Sign In
        # Sign in button usually has text "Sign in"
        time.sleep(2) # Wait for dynamic load
        if page.query_selector("text=Sign in"):
            print(" STOP: User is not signed in to Google.")
            print(" Please sign in to your Google account in the browser window that just opened.")
            print(" Waiting for you to sign in... (Script will continue once you are logged in)")
            
            # Periodically check if "Sign in" button is gone
            while page.query_selector("text=Sign in"):
                time.sleep(2)
            
            print(" Login detected. Proceeding...")

        print(" Creating New Notebook...")
        # Click 'File' then 'New notebook'
        page.click("text=File")
        page.click("text=New notebook")
        
        # Wait for the notebook to load (check for the 'Connect' button or similar)
        page.wait_for_selector(".colab-connect-button", timeout=60000)
        print(" Notebook ready.")

        print(" Accessing Files Sidebar...")
        # The folder icon in the sidebar
        page.click('button[aria-label="Files"]', timeout=30000)
        
        print(" Triggering Upload...")
        # We need to trigger the file chooser. 
        # In Colab, the 'Upload to session storage' button is a div/button with icon
        # A more reliable way is to find the hidden file input
        
        with page.expect_file_chooser() as fc_info:
            # Click the upload icon (usually the first button in the files toolbar)
            page.click('button[aria-label="Upload to session storage"]')
        
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)
        
        print(f" Uploading '{os.path.basename(file_path)}' to Colab storage...")
        
        # Give it a moment to show up in the list
        time.sleep(5)
        
        print("\n TASK COMPLETE!")
        print(f" File '{os.path.basename(file_path)}' is now in your Colab session storage.")
        print(" You can now use 'pd.read_csv(\"" + os.path.basename(file_path) + "\")' in your notebook.")
        
        input("\nPress Enter to close the browser and exit...")
        browser.close()

if __name__ == "__main__":
    try:
        auto_upload_agent()
    except Exception as e:
        print(f" Critical Failure: {e}")
