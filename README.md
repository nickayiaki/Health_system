# Health_system

A simple Health System built with Python and Flask.

This system allows doctors (users) to:
- Create health programs (e.g., TB, Malaria, HIV)
- Register new clients
- Enroll clients into health programs
- View client profiles and the programs they are enrolled in
- Expose client profiles through an API for integration with other systems

---
Features

- Add new health programs
- Register and manage client information
- Enroll clients into one or more health programs
- Search for client
---

 Getting Started

Requirements
- Python 3.x installed
- Flask installed

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/nickayiaki/Health_system/
    ```

2. Navigate into the project directory:
    ```bash
    cd health-info-system
    ```

3. Install Flask:
    ```bash
    pip install flask
    ```

4. Run the application:
    ```bash
    python Health_system.py
    ```

5. Open your browser and visit:
    ```
    http://127.0.0.1:5000/
    ```

---

##  API Endpoints

| Method | Endpoint | Description |
|:------|:---------|:------------|
| POST | `/api/program` | Create a new health program |
| POST | `/api/client` | Register a new client |
| POST | `/api/client/<client_id>/enroll` | Enroll a client into programs |
| GET  | `/api/client/<client_id>` | Get client profile information |


