#  Welcome to Your First Data Science Agent!

Hello! This guide is designed for **beginners** who want to learn how to automate data tasks using Python. We will build a "Data Agent" that lives in Google Colab and helps you handle files automatically.

---

##  What is a Data Agent?
Think of an agent as a small robot  that waits for your commands. Instead of clicking many buttons manually, you just type a word like **'analyze'**, and the agent does the hard work for you!

---

##  How the Agent "Thinks" (The Plan)

Here is a simple map of how our agent processes your requests:

![How the Agent Works](architecture_diagram.png)

1.  **Listener**: The agent waits for you to type something.
2.  **Processor**: It checks your word against its list of "Skills".
3.  **Executor**: It performs the action (like loading a file or showing a chart).

---

##  Level 1: The Simple Uploader
Inside Google Colab, we use a special tool to pick files from your computer.

**The Code:**
```python
from google.colab import files
uploaded = files.upload() # This opens the "Select File" box!
```

---

##  Level 2: The Web Fetcher (Super Fast!)
Instead of downloading a file and then uploading it, our agent can "fetch" it directly from a website link. This is much faster!

**Try this command in the agent:**
`fetch https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv`

---

##  Level 3: The Auto-Pilot (Advanced)
We also have a special script called [colab_auto_uploader.py](colab_auto_uploader.py). This one is for your **laptop terminal**. It will automatically open your browser and upload files for you!

**How to use it:**
1.  Open your terminal or command prompt.
2.  Type: `python colab_auto_uploader.py`
3.  Paste the path to your CSV file (you can drag the file into the terminal window).

---

##  Your First Challenge: Add a New Skill!
Can you make the agent say "Hello"?

**Steps:**
1.  Open [premium_agent.py](premium_agent.py).
2.  Find the `main_loop` section.
3.  Add these lines:
    ```python
    elif cmd == 'hello':
        print(" Hello Student! I am ready to help.")
    ```
4.  Run it and type **'hello'**!

---

##  Helpful Links for New Students
*   [What is Pandas?](https://pandas.pydata.org/docs/getting_started/index.html) (The tool we use to read data)
*   [Google Colab Guide](https://colab.research.google.com/notebooks/intro.ipynb) (Where we run our code)

### Happy Coding! Remember, every expert was once a beginner.
