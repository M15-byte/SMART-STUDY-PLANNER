# Smart Study Planner

**Course:** 1203 ST - Programming Fundamentals  
**Faculty:** Faculty of Science and Technology  
**Level:** 1.2  
**Student Name:** LUWAGA BENEDICT  
**Student Reg / ID:** VU-BCS-2603-3388-DAY  
**Programme:** Bachelor of Science in Computer Science (BCS)  
**Examiner / Lecturer:** Kinyonyi David Hope  
**Moderator:** Rodgers Kimera

# 1. Project Overview

The **Smart Study Planner** is a console-based Python application developed to help university students log, review, and analyze their independent study sessions across different academic modules over the course of a semester.

## 2. Key Features

- **Menu-Driven Interface (`main`):** Clean command-line interface with options 1–5 that continues running until the user chooses to exit, rejecting invalid choices without crashing.
- **Session Logging (`add_session`):** Prompts for Subject, Topic, Date/Day label, and Duration (in minutes), validating that the duration is a positive number greater than 0.
- **Session Classification (`classify_session`):** Classifies sessions into **Short** (<30 mins), **Medium** (30-90 mins), and **Long** (>90 mins).
- **Tabular Display (`view_sessions`):** Displays all recorded sessions in a neat table showing Subject, Topic, Date, Duration, and Classification.
- **Subject Search (`search_by_subject`):** Allows searching by subject name (case-insensitive) and displays matching sessions along with total time spent on that subject.
- **Study Statistics (`study_statistics`):** Computes total overall study hours, study hours per subject, the weakest area (least studied subject), and the single longest study session.
- **File Persistence (`save_sessions` & `load_sessions`):** Automatically reloads records from `study_log.txt` on startup (handling missing file on first run without crashing) and saves all records on exit.

## 3. How to Run the Program

```bash
# Clone the repository
git clone https://github.com/M15-byte/SMART-STUDY-PLANNER.git

# Navigate to project folder
cd SMART-STUDY-PLANNER

# Run the Python script
python3 smart_study_planner.py
```

## 4. File Structure

```
├── smart_study_planner.py          # Python Source Code
├── smart_study_planner_report.docx   # Coursework Answer Sheet (Word)
├── smart_study_planner_report.md     # Coursework Report (Markdown)
├── study_log.txt                   # Persistent Data Storage File
└── README.md                       # Project Documentation
```

## 5. Author

- **Name:** LUWAGA BENEDICT
- **Student ID:** VU-BCS-2603-3388-DAY
- **Programme:** Bachelor of Science in Computer Science (BCS)
- **Faculty:** FST
- **Institution:** VICTORIA UNIVERSITY
