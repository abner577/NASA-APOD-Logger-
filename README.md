# 🌌 NASA APOD Snapshot Logger

A small, CLI-based Python application that fetches metadata from NASA’s **Astronomy Picture of the Day (APOD)** API and logs selected information to disk.  
This project is designed strictly as a **practice exercise** to reinforce Python fundamentals through a realistic but intentionally simple workflow.

---

## 🧭 Table of Contents
- [Purpose of This Project](#purpose-of-this-project)
- [Practiced Concepts](#practiced-concepts)
- [Application Flow](#application-flow)
- [Project Structure](#project-structure)
- [Required Configuration Setup](#required-configuration-setup)

---

## Purpose of This Project

Its primary goal is to improve familiarity with Python’s syntax, file-handling patterns, and concurrency model by applying concepts that are already familiar from other languages.

Certain design decisions (such as multithreading) are included **intentionally for educational value**, even though they do not provide a strong performance benefit in a small, single-user CLI application.

---

## 📝 Practiced Concepts

This project focuses on the following Python topics:

- File and directory detection
- Writing structured data to disk (CSV and JSON)
- Reading persisted data from files
- Working with dates and times
- Making HTTP requests to a public API
- Basic multithreading for I/O-bound tasks
- Thread coordination using queues and join semantics

---

## 🏗 Application Flow

1. The application starts and ensures all required storage locations exist.
2. A console menu is presented to the user:
   - Fetch today’s APOD
   - Fetch APOD for a specific date
   - Show the last N logged entries (entered by user)
   - Exit
3. When APOD data is successfully fetched:
   - The response is validated
   - A snapshot record is created
   - The snapshot is written to disk
4. Logged entries persist between runs.
5. The user may view a summary of previously logged snapshots at any time.

---

## 📁 Project Structure

| Path | Purpose |
|-----|--------|
| `main.py` | CLI entry point and overall program flow |
| `nasa_client.py` | Handles NASA APOD API requests and response validation |
| `storage.py` | File detection, reading, and writing logic |
| `data/apod_snapshots.jsonl` | Persistent JSON log (one snapshot per line) |
| `data/apod_snapshots.csv` | Persistent CSV log of snapshot data |
| `README.md` | Project documentation |

---

## ⚙️ Required Configuration Setup

Before running the application, ensure the following:

- All required Python dependencies are installed from `requirements.txt`

No additional environment variables or API keys are required.  
The application uses NASA’s public `DEMO_KEY` for API access.
