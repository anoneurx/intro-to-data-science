import os
import sys
import time

# We use an advanced library called Playwright to automate clicking buttons on websites!
from playwright.sync_api import sync_playwright  

def auto_upload_agent():
    print(" Agent: Premium Colab Uploader Booting...")
    
    # 1. Ask the user where their file is saved on their computer
    file_path = input("\n Please enter the full path to your CSV file: ").strip()
    
    # 2. Cleanup the path (remove quotes if they accidentally drag-and-dropped the file into the terminal)
    file_path = file_path.replace('"', '').replace("'", "")
    
    # 3. Check if the file actually exists where they said it does
    if not os.path.exists(file_path):
        print(f" Error: File not found at '{file_path}'")
        # If it doesn't exist, stop the program entirely
        return 

    print(f" Target acquired: {os.path.basename(file_path)}")

    # 4. Boot up Playwright (our browser automation robot tool)
    with sync_playwright() as p:
        print(" launching browser...")
        
        # 'headless=False' means the browser isn't invisible. 
        # We can actually WATCH the robot open the browser and click things!
        browser = p.chromium.launch(headless=False) 
        context = browser.new_context()
        page = context.new_page()

        print(" Navigating to Google Colab...")
        page.goto("https://colab.research.google.com/")

        # 5. Check if the user is signed into Google
        time.sleep(2) # Wait 2 seconds for the webpage to fully load

        # Try to find the "Sign in" button on the webpage
        if page.query_selector("text=Sign in"):
            print(" STOP: User is not signed in to Google.")
            print(" Please sign in to your Google account in the browser window that just opened.")
            print(" Waiting for you to sign in... (Script will continue once you are logged in)")
            
            # Periodically check to see if the "Sign in" button has disappeared (meaning they finally logged in)
            while page.query_selector("text=Sign in"):
                time.sleep(2)
            
            print(" Login detected. Proceeding...")

        # 6. Now that we are logged in, let's automatically create a newly blank Notebook
        print(" Creating New Notebook...")
        
        # We tell the robot to click the "File" menu, then click "New notebook"
        page.click("text=File")
        page.click("text=New notebook")
        
        # We must wait for the notebook to load up connection resources (this can take up to 60 seconds)
        page.wait_for_selector(".colab-connect-button", timeout=60000)
        print(" Notebook ready.")

        # 7. Open the folder structure on the left side of Colab
        print(" Accessing Files Sidebar...")
        # We look for the button labeled 'Files' and click it
        page.click('button[aria-label="Files"]', timeout=30000)
        
        print(" Triggering Upload...")
        
        # 8. We intercept the file upload box and inject our chosen CSV file into it
        # Playwright prepares to catch a file dialogue box
        with page.expect_file_chooser() as fc_info:
            # We command the robot to click the actual upload icon inside Colab
            page.click('button[aria-label="Upload to session storage"]')
        
        # Now we submit the file path into the popup box!
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)
        
        print(f" Uploading '{os.path.basename(file_path)}' to Colab storage...")
        
        # Give Colab 5 seconds to process the file and display it
        time.sleep(5)
        
        # 9. Victory!
        print("\n TASK COMPLETE!")
        print(f" File '{os.path.basename(file_path)}' is now in your Colab session storage.")
        print(" You can now use pandas to read your file by writing: df = pd.read_csv(\"" + os.path.basename(file_path) + "\")")
        
        # Keep the script paused and alive until the user hits enter
        input("\nPress Enter to close the browser and exit...")
        browser.close()

if __name__ == "__main__":
    try:
        # Launch our automation agent
        auto_upload_agent()
    except Exception as e:
        # If something crashes (like internet dies, or playwright stops working), we catch the error gracefully
        print(f" Critical Failure: {e}")
