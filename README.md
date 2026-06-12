# 🚀 Internship & Job Tracking Dashboard

## 👥 GitHub Contribution Table
| Name | Username / ID | Tasks Completed |
| :--- | :--- | :--- |
| **Muhammad Yahya** | (GitHub Username / ID) | Docker Compose, Architecture setup, PostgreSQL Schema, Reports, Analytics Dashboard |
| **Muhammad Zeeshan** | (GitHub Username / ID) | Main Streamlit App, App Routing, Auth Module, README, Database Health Check |
| **Syed Minhal Naqvi**| (GitHub Username / ID) | Add, View, Update & Delete functionality, CSV Bulk Upload, Deadline Alerts |

## 🛠️ Setup Instructions
1. Run `docker compose up -d` to launch PostgreSQL, pgAdmin, and Streamlit.
2. Access the app at `http://localhost:8501`.
3. Access pgAdmin at `http://localhost:5050`. Connect to host `postgres_db` on port `5432`.

## 🐳 Docker Commands Guide
* `docker compose up -d` - Starts all the defined multi-container services in the background.
* `docker compose ps` - Shows the running services and mapped ports.
* `docker compose logs postgres_db` - Outputs the PostgreSQL container connection/error logs.
* `docker compose down -v` - Stops containers and securely deletes attached volumes (Data is lost).