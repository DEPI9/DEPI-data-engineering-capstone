# Project Documentation

## Project Planning

### Project Title
Real-time IoT Data Pipeline

### Overview
This project simulates IoT sensor data (temperature and humidity), processes it using Python and Docker containers, stores it in Azure SQL Database, and visualizes the results through Power BI dashboards. It demonstrates a complete modern data pipeline from generation to real-time analytics.

### Objectives
- Simulate real-time IoT data using Python.
- Clean and transform raw data through ETL processing.
- Identify anomalies and generate alerts when thresholds are exceeded.
- Store processed data in Azure SQL for long-term analytics.
- Visualize system metrics and insights using Power BI dashboards.

### Team Members & Roles
| Name | Role | Responsibilities |
|------|------|------------------|
| Yossef Amr Atwa | Team Leader / Dashboard Developer | Manage project, develop dashboard, prepare documentation |
| Ahmad Fawzi Elbayomi | Python Developer | Develop data generation script inside Docker |
| Eslam Mohamed Ahmed | Data Engineer | Build ETL script, clean data, handle alerts |
| Omar Ali Farag | SQL Developer | Create database schema and SQL queries |
| Hadeer Gamal Mahmoud | SQL Tester | Validate and test SQL queries |
| Salma Medhat Soliman | UI/UX Designer | Design Power BI dashboard and documentation layout |

### Tools & Technologies
- Python 3.10
- Docker
- Azure SQL Database
- Power BI
- Figma

### Timeline
| Phase | Description | Duration |
|--------|-------------|-----------|
| Phase 1 | Data generation script and Docker setup | 3 days |
| Phase 2 | ETL processing and alert logic | 4 days |
| Phase 3 | Database schema and SQL integration | 3 days |
| Phase 4 | Dashboard creation and testing | 4 days |
| Phase 5 | Final report and presentation | 2 days |

---

## Stakeholder Analysis

### Internal Stakeholders
| Stakeholder | Role | Interest | Impact |
|--------------|------|-----------|---------|
| Team Members | Development and testing | High | High |
| Team Leader (Yossef Amr Atwa) | Coordination, delivery, quality | Very High | High |
| Mentor / Instructor | Oversight and guidance | Medium | High |

### External Stakeholders
| Stakeholder | Role | Interest | Impact |
|--------------|------|-----------|---------|
| Evaluators | Review final demo and documentation | Medium | High |
| DEPI Management Team | Evaluate project outcomes | High | High |

---

## Database Design

### Database Name
IoT_DB

### Schema Overview

**Table: SensorData**
| Column | Type | Description |
|---------|------|-------------|
| id | INT (Primary Key) | Unique reading ID |
| timestamp | DATETIME | Time of reading |
| temperature | FLOAT | Temperature value |
| humidity | FLOAT | Humidity value |
| status | NVARCHAR(50) | “Normal” or “Alert” |

**Table: AlertLogs**
| Column | Type | Description |
|---------|------|-------------|
| alert_id | INT (Primary Key) | Unique alert ID |
| sensor_id | INT (Foreign Key → SensorData.id) | Related reading |
| alert_message | NVARCHAR(100) | Description of alert |
| alert_time | DATETIME | Time when alert occurred |

**ERD (Figma Link)**  
👉 [View Database ERD on Figma](https://www.figma.com/design/1tYSHGD2XNwaJZTkzNzLg2/IoT-Database-Design---ERD?t=fuxUir3ZytygONMe-1)

---

## UI/UX Design

### Dashboard Overview
The Power BI dashboard visualizes live IoT data from Azure SQL Database. It includes real-time analytics and alerts for abnormal temperature or humidity levels.

### Dashboard Components
- Line Chart: Temperature vs Time  
- Line Chart: Humidity vs Time  
- Cards: Average temperature, average humidity, total alerts  
- Pie Chart: Normal vs Alert readings  
- Filter: Date/time range for monitoring  

### Design Notes
- Theme: Minimalistic (gray, blue, green tones)  
- Typography: Clean sans-serif font for readability  
- Layout: 2-row grid – charts on top, KPIs below  

**Figma Design Link**  
👉 [View Dashboard UI on Figma](https://www.figma.com/design/UVpyJMRvIXmzIBgz9s4fVQ/IoT-Dashboard---UI-UX-Design?node-id=0-1&t=fuxUir3ZytygONMe-1)

---

### End of Documentation
