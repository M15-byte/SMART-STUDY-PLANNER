# ==============================================================================
# COURSEWORK PROJECT: SMART STUDY PLANNER
# Course: 1203 ST - Programming Fundamentals
# Student Name: LUWAGA BENEDICT
# Registration No: VU-BCS-2603-3388-DAY
# Programme: Bachelor of Science in Computer Science (BCS)
# Faculty: Faculty of Science and Technology
# Lecturer: Kinyonyi David Hope
# ==============================================================================

import os

# File used to store session records
DATA_FILE = "study_log.txt"


def classify_session(duration):
    """
    Classifies a study session based on its duration in minutes:
      - Short  : under 30 minutes (< 30)
      - Medium : 30 to 90 minutes (30 <= duration <= 90)
      - Long   : over 90 minutes (> 90)
    """
    if duration < 30:
        return "Short"
    elif duration <= 90:
        return "Medium"
    else:
        return "Long"


def load_sessions(filename=DATA_FILE):
    """
    Loads saved study sessions from a text file into a list of dictionaries.
    If the file does not exist, returns an empty list without raising an error.
    """
    sessions = []
    
    if not os.path.exists(filename):
        return sessions

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    if len(parts) == 4:
                        subject, topic, date_label, duration_str = parts
                        try:
                            duration = int(duration_str)
                            sessions.append({
                                "subject": subject.strip(),
                                "topic": topic.strip(),
                                "date": date_label.strip(),
                                "duration": duration
                            })
                        except ValueError:
                            continue
    except Exception as e:
        print(f"Error reading {filename}: {e}")

    return sessions


def save_sessions(sessions, filename=DATA_FILE):
    """
    Saves all study session dictionaries to a pipe-delimited text file.
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for s in sessions:
                record = f"{s['subject']}|{s['topic']}|{s['date']}|{s['duration']}\n"
                file.write(record)
        print(f"\n[Saved] {len(sessions)} session(s) successfully written to '{filename}'.")
    except Exception as e:
        print(f"\n[Error] Unable to save records to '{filename}': {e}")


def add_session(sessions):
    """
    Prompts the user for session details (subject, topic, date/day, duration).
    Validates that duration is a positive integer (> 0), re-prompting until valid.
    Stores the session as a dictionary and appends it to the sessions list.
    """
    print("\n" + "=" * 50)
    print("             ADD A STUDY SESSION")
    print("=" * 50)

    # Subject validation
    while True:
        subject = input("Enter Subject Name: ").strip()
        if subject:
            break
        print("Subject name cannot be blank. Please enter a subject.")

    # Topic validation
    while True:
        topic = input("Enter Topic Covered: ").strip()
        if topic:
            break
        print("Topic cannot be blank. Please enter a topic.")

    # Date / Day label validation
    while True:
        date_label = input("Enter Date / Day (e.g. 2026-09-03 or Monday): ").strip()
        if date_label:
            break
        print("Date/Day label cannot be blank. Please enter a date or day.")

    # Duration validation: positive integer > 0
    while True:
        duration_input = input("Enter Duration (in minutes): ").strip()
        try:
            duration = int(duration_input)
            if duration > 0:
                break
            else:
                print("Duration must be a positive number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number for minutes.")

    # Store as dictionary
    session = {
        "subject": subject,
        "topic": topic,
        "date": date_label,
        "duration": duration
    }
    sessions.append(session)

    # Show confirmation
    category = classify_session(duration)
    print("\nSession recorded successfully:")
    print(f"  Subject : {subject}")
    print(f"  Topic   : {topic}")
    print(f"  Date/Day: {date_label}")
    print(f"  Duration: {duration} minutes ({category})")


def view_sessions(sessions):
    """
    Displays all logged study sessions in a formatted table.
    Shows Subject, Topic, Duration, and Short/Medium/Long classification.
    """
    print("\n" + "=" * 80)
    print("                         RECORDED STUDY SESSIONS")
    print("=" * 80)

    if not sessions:
        print("No study sessions logged yet.")
        print("=" * 80)
        return

    # Table Header
    print(f"{'No.':<4} | {'Date/Day':<14} | {'Subject':<22} | {'Topic':<20} | {'Mins':<6} | {'Classification'}")
    print("-" * 80)

    # Table Rows
    for i, s in enumerate(sessions, start=1):
        category = classify_session(s["duration"])
        sub_text = s["subject"][:20] + ".." if len(s["subject"]) > 22 else s["subject"]
        top_text = s["topic"][:18] + ".." if len(s["topic"]) > 20 else s["topic"]
        print(f"{i:<4} | {s['date']:<14} | {sub_text:<22} | {top_text:<20} | {s['duration']:<6} | {category}")

    print("=" * 80)
    print(f"Total sessions: {len(sessions)}")


def search_by_subject(sessions, subject=None):
    """
    Searches for sessions by subject name using case-insensitive matching.
    Displays matching sessions in a table and shows the total study time spent.
    If no sessions are found, displays a clear message.
    """
    print("\n" + "=" * 80)
    print("                       SEARCH SESSIONS BY SUBJECT")
    print("=" * 80)

    if not sessions:
        print("No study sessions recorded in the planner.")
        print("=" * 80)
        return

    if subject is None:
        subject = input("Enter subject name to search: ").strip()

    if not subject:
        print("Search subject cannot be empty.")
        print("=" * 80)
        return

    # Filter matching sessions (case-insensitive)
    matches = []
    for s in sessions:
        if s["subject"].strip().lower() == subject.strip().lower():
            matches.append(s)

    if not matches:
        print(f"\nNo sessions found for subject: '{subject}'.")
        print("Please check the subject spelling or view all sessions in Option 2.")
        print("=" * 80)
        return

    # Display matching sessions
    print(f"\nFound {len(matches)} session(s) for '{subject}':")
    print("-" * 80)
    print(f"{'No.':<4} | {'Date/Day':<14} | {'Subject':<22} | {'Topic':<20} | {'Mins':<6} | {'Classification'}")
    print("-" * 80)

    total_mins = 0
    for i, s in enumerate(matches, start=1):
        category = classify_session(s["duration"])
        sub_text = s["subject"][:20] + ".." if len(s["subject"]) > 22 else s["subject"]
        top_text = s["topic"][:18] + ".." if len(s["topic"]) > 20 else s["topic"]
        print(f"{i:<4} | {s['date']:<14} | {sub_text:<22} | {top_text:<20} | {s['duration']:<6} | {category}")
        total_mins += s["duration"]

    total_hours = total_mins / 60.0
    print("=" * 80)
    print(f"Summary for '{subject}':")
    print(f"  Total Sessions : {len(matches)}")
    print(f"  Total Time     : {total_mins} minutes ({total_hours:.2f} hours)")
    print("=" * 80)


def study_statistics(sessions):
    """
    Computes and displays:
      1. Total hours studied overall
      2. Total hours studied per subject
      3. Subject with least total study time (weakest area)
      4. Single longest session recorded
    """
    print("\n" + "=" * 60)
    print("                      STUDY STATISTICS")
    print("=" * 60)

    if not sessions:
        print("No study sessions recorded yet to compute statistics.")
        print("=" * 60)
        return

    # 1. Total hours studied overall
    total_mins = sum(s["duration"] for s in sessions)
    total_hours = total_mins / 60.0

    # 2. Total hours studied per subject
    subject_totals = {}
    subject_display_names = {}

    for s in sessions:
        key = s["subject"].strip().lower()
        if key not in subject_totals:
            subject_totals[key] = 0
            subject_display_names[key] = s["subject"].strip()
        subject_totals[key] += s["duration"]

    # 3. Subject with least total study time (weakest area)
    weakest_key = min(subject_totals, key=subject_totals.get)
    weakest_name = subject_display_names[weakest_key]
    weakest_mins = subject_totals[weakest_key]
    weakest_hours = weakest_mins / 60.0

    # 4. Single longest session recorded
    longest_session = max(sessions, key=lambda s: s["duration"])
    longest_category = classify_session(longest_session["duration"])

    # Output formatted results
    print(f"\n1. Overall Study Time:")
    print(f"   • Total Time: {total_mins} minutes ({total_hours:.2f} hours)")
    print(f"   • Total Sessions: {len(sessions)}")
    print(f"\n2. Total Study Time per Subject:")
    print(f"   {'-'*54}")
    print(f"   {'Subject':<30} | {'Minutes':<8} | {'Hours':<8}")
    print(f"   {'-'*54}")
    for key in sorted(subject_totals, key=subject_totals.get, reverse=True):
        name = subject_display_names[key]
        mins = subject_totals[key]
        hrs = mins / 60.0
        print(f"   {name:<30} | {mins:<8} | {hrs:<8.2f}")
    print(f"   {'-'*54}")

    print(f"\n3. Weakest Subject Area (Least Study Time):")
    print(f"   • Subject : {weakest_name}")
    print(f"   • Time    : {weakest_mins} minutes ({weakest_hours:.2f} hours)")
    print(f"   • Note    : More study time should be allocated to this subject.")

    print(f"\n4. Longest Single Session Recorded:")
    print(f"   • Subject  : {longest_session['subject']}")
    print(f"   • Topic    : {longest_session['topic']}")
    print(f"   • Date/Day : {longest_session['date']}")
    print(f"   • Duration : {longest_session['duration']} minutes ({longest_session['duration']/60.0:.2f} hours) [{longest_category}]")
    print("=" * 60)


def display_menu():
    """
    Displays the console menu options to the user.
    """
    print("\n" + "=" * 46)
    print("       SMART STUDY PLANNER - MAIN MENU")
    print("=" * 46)
    print("  1. Add a study session")
    print("  2. View all sessions")
    print("  3. Search sessions by subject")
    print("  4. View statistics")
    print("  5. Save and exit")
    print("=" * 46)


def main():
    """
    Main function that loads data, drives the interactive menu loop,
    and saves sessions upon exit.
    """
    print("==============================================")
    print("           SMART STUDY PLANNER                  ")
    print("==============================================")

    # Reload existing sessions on startup
    sessions = load_sessions(DATA_FILE)
    if sessions:
        print(f"[Loaded] {len(sessions)} session(s) loaded from '{DATA_FILE}'.")
    else:
        print(f"[Notice] No previous data file found. Starting with an empty log.")

    # Main menu loop
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_session(sessions)
        elif choice == "2":
            view_sessions(sessions)
        elif choice == "3":
            search_by_subject(sessions)
        elif choice == "4":
            study_statistics(sessions)
        elif choice == "5":
            save_sessions(sessions, DATA_FILE)
            print("\nProgram closed successfully. Good luck with your studies!\n")
            break
        else:
            print("\nInvalid choice. Please enter a valid number from 1 to 5.")


# Entry point guard
if __name__ == "__main__":
    main()



# ALL RIGHTS RESERVED © 2025 LUWAGA BENEDICT