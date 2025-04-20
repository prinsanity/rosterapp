# Role-Based Project Management System

## Graphical Abstract
![Graphical Abstract](path/to/graphical_abstract.png)  

---

## Purpose of the Software

## System Overview

**Enterprise-grade duty assignment system** with hierarchical approval workflow:
PLANNERS (Create) → EDITORS (Modify) → AGENTS (Execute)


Key Features:
- Role-based access control
- Full audit trail of all changes
- Custom duty templates
- Offline-capable interface
- Comprehensive reporting

| Role | Responsibilities | Actions |
|------|-----------------|---------|
| **PLANNERS** | Strategic assignment creation | • Create duty templates <br> • Set schedules <br> • Define requirements |
| **EDITORS** | Operational adjustment | • Modify assignments <br> • Balance workloads <br> • Add instructions |
| **AGENTS** | Task execution | • Confirm receipt <br> • View Tasks <br> • Report completion |

### Software Development Process
This project uses the **Waterfall Software Development Process**.

#### Why Waterfall?
- **Clear Requirements**: The project had well-defined requirements from the beginning, making Waterfall an ideal choice.
- **Sequential Phases**: Each phase (Requirement Gathering, Design, Development, Testing, Deployment) was completed before moving to the next, ensuring a structured and predictable development process.
- **High-Quality Output**: Since there are no competitors for this specific system, the focus was on delivering a polished and high-quality product.

### Possible Usage of the Software (Target Market)
- **Small and Medium Enterprises (SMEs)**: Teams in SMEs can use this tool to structure workflows between planners, editors, and viewers.
- **Educational Institutions**: Professors or course coordinators can use the system to delegate tasks and monitor progress.
- **Freelance Teams**: Freelancers can use this platform to manage projects requiring a structured workflow.

---

## Software Development Plan

### Development Process
The development process followed the **Waterfall Model**, which included the following phases:
1. **Requirement Gathering**: Defined the project workflow, roles, and functionality.
2. **Design**: Created the database schema, role-based access control logic, and user interface.
3. **Development**: Built the system using Django for the backend and HTML/CSS for the frontend.
4. **Testing**: Tested the system to ensure all workflows function correctly.
5. **Deployment**: Prepared the system for local and production environments.

### Members
This project was developed by a **single developer**, handling all roles and responsibilities.

| **Name**                |     **Role**             | **Responsibilities**                                 |
|----------------|----------------------|-----------------------------------------------------|
| Santos, Prince Joshuah Nelmida    | Developer & Designer| Full-stack development, system design, and testing  |

---

## Algorithm

### Workflow Algorithm
1. **Planning Role**:
   - Creates a new project.
   - Defines the table structure (columns/rows).
   - Saves the project and sends it to the Editor.

2. **Editor Role**:
   - Receives the project from Planning.
   - Makes updates to the project.
   - Saves the updated project and sends it to the Viewer.

3. **Viewer Role**:
   - Views the finalized project sent by the Editor.

4. **Permission Enforcement**:
   - Access is restricted based on user roles using Django's `Group` system.

---

## Current Status of the Software
- **Completed Features**:
  - Role-based access control (Planning, Editor, Viewer).
  - Project creation, editing, and viewing workflows.
  - User authentication and login/logout functionality.
  - Dashboard that displays user-specific projects.

---

## Future Plans
1. **Enhancements**:
   - Add more granular permissions for roles.
   - Extend the dashboard with advanced analytics (e.g., project completion stats).
2. **Scalability**:
   - Move from SQLite to a cloud database (e.g., PostgreSQL).
   - Deploy the application to a cloud platform (e.g., AWS or Heroku).
3. **Mobile Support**:
   - Create a responsive design for mobile users.
   - Develop a mobile app version of the system.

---

## Demo
A demo of the project is available on YouTube:  
[![Watch Demo](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)  

---

## Environments of the Software Development and Running

### Programming Language
- **Backend**: Python (Django Framework)
- **Frontend**: HTML, CSS, JavaScript

### Minimum Hardware/Software Requirements
- **Hardware**:
  - CPU: Dual-core processor
  - RAM: 4GB minimum
  - Storage: 500MB free space
- **Software**:
  - Python 3.8 or higher
  - Django 4.x
  - Web browser (e.g., Chrome, Firefox)

### Required Packages
- Django 4.x
- Pillow
- jsonfield
