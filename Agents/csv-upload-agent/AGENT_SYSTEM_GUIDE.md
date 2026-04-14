# Mission Control: The Data Science Agent System

Welcome to the **Anoneurx Data Science Agent** documentation. This guide explains how our autonomous data assistant operates and provides a step-by-step roadmap for students to build their own from scratch.

---

## 1. How the Agent Works (The Architecture)

Our system uses a **Dual-Agent Architecture** to bridge the gap between your local computer and the cloud (Google Colab).

### The Cloud Agent (`premium_agent.py`)
This is the "Brain" that lives inside your Google Colab notebook. It manages data in RAM and performs audits.

*   **Listener**: An infinite `while True` loop that keeps the agent alive.
*   **Processor**: A command parser that maps strings (like `upload`) to Python methods.
*   **Executor**: Functions that use `pandas` to transform or analyze data.
*   **Memory Buffer**: A class attribute `self.df` that keeps the dataset "warm" in memory so you don't have to reload it for every command.

### The Local Agent (`colab_auto_uploader.py`)
This is a "Bridge" agent that runs on your laptop. It uses **Playwright** (a browser automation tool) to:
1.  Open Chrome/Chromium automatically.
2.  Navigate to Google Colab.
3.  Simulate mouse clicks to upload files from your local hard drive into the web session.

---

## 2. Build Your Own Agent (Student Roadmap)

Building an agent is like building a LEGO set. Start with the foundation and add skills.

### Phase 1: The Foundation (Loop & Brain)
Create the class and the "heartbeat" (main loop) of the agent.

```python
class MyAgent:
    def __init__(self):
        self.df = None  # Storage for data
        print("Agent Initialized.")

    def run(self):
        while True:
            cmd = input("[AGENT] > ").lower()
            if cmd == 'exit': break
            elif cmd == 'help': print("Options: upload, analyze")
```

### Phase 2: Input Senses (Fetching Data)
Give the agent "Eyes" by connecting it to the internet or your local files.

```python
import requests
import io

def fetch_data(self, url):
    r = requests.get(url)
    self.df = pd.read_csv(io.StringIO(r.text))
    print("Remote synchronization successful.")
```

### Phase 3: Action Skills (Data Analysis)
Enable the "Hands" of the agent to manipulate the data.

```python
def analyze(self):
    if self.df is not None:
        print(f"I found {self.df.shape[0]} rows.")
        print(self.df.mean()) # Calculate averages automatically
```

---

## 3. Pro Tips for Students

*   **Modular Design**: Always keep your "Skills" separate from your "Main Loop". This allows you to test one piece at a time.
*   **Error Handling**: Use `try/except` blocks. If a user enters a broken URL, you don't want your whole agent to crash!
*   **Interactive UI**: Use clear separators (like `===`) to make your agent feel "premium" and easy to read.

---

## 4. Next Level: The Remote Agent
Our repository also includes a `colab_auto_uploader.py`. This is a **bridging agent** that runs on your laptop and talks to Google Colab.

1.  It watches your computer's files.
2.  It uses automation to bypass manual "Click to Upload" buttons.
3.  It demonstrates how agents can communicate across different systems.

---

> **Mission Objective:** Try adding a `skill_chart` to your agent today! Use `df.plot()` to see your data instantly.
