# Assignment Report: Loop Logic and Data Processing
**By: Muhammad Qasim**

For this assignment, I created two scripts that show how we can use loops to handle large amounts of data automatically. Instead of creating folders and files manually, I wrote code that does the hard work for me. Here is how my logic works:

---

### Phase 1: Splitting the Data (`solve_assignment.py`)
In the first part of my project, I wanted to simulate how data is often stored in different locations to keep things organized.

1.  **The Dataset**: I started with a simple list of numbers from 1 to 100.
2.  **Creating the Folders**: I used a `for` loop to create 10 subfolders (`part_1` to `part_10`). This shows how a single loop can perform structural tasks on a computer.
3.  **The Sliding Window Logic**: This was the most interesting part. Inside each folder, I created 3 CSV files. To make the data overlap, I used a **Modulo operator (`%`)**. 
    *   For example, Folder 1 contains numbers for 1-10, 11-20, and 21-30.
    *   This ensures that every folder has exactly three files, even when Wrapping around from the end of the list back to the beginning.
4.  **Mathematical Calculation**: For every number, I calculated its square ($X^2$) inside the loop and saved it into the CSV structure.

---

### Phase 2: Regenerating the Data (`regenerate_data.py`)
In the second part, I acted as a data scientist who needs to collect scattered data and turn it into a single clean report.

1.  **Scanning and Reading**: I used **Nested Loops** (a loop inside a loop). The first loop enters each folder, and the second loop reads every CSV file found inside.
2.  **Handling Duplicates with Dictionaries**: Since some numbers were saved in multiple files, I used a **Python Dictionary**. I explained to myself that since dictionaries can't have duplicate "Keys," simply adding the data to the dictionary automatically cleaned my dataset!
3.  **Final Aggregation**: After the loops finished, I sorted the data and saved all 100 unique rows into a master file called `complete_data.csv` inside a new `main` folder.

---

### What I Learned
Through this project, I learned that loops are not just for counting numbers; they are powerful tools for:
*   Creating and managing file systems.
*   Automating repetitive office tasks.
*   Cleaning and organizing datasets efficiently.

I used **GitHub** to manage my code, which helped me understand how developers work in professional, cloud-based environments.

Thank you for reviewing my work!
