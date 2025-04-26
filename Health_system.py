from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage
health_programs = []
clients = []

# Data Models
class HealthProgram:
    def __init__(self, name):
        self.name = name

class Client:
    def __init__(self, client_id, name, age):
        self.client_id = client_id
        self.name = name
        self.age = age
        self.enrolled_programs = []

# 1. Create a health program
def create_health_program(name):
    program = HealthProgram(name)
    health_programs.append(program)
    return program

# 2. Register a new client
def register_client(client_id, name, age):
    client = Client(client_id, name, age)
    clients.append(client)
    return client

# 3. Enroll client in programs
def enroll_client(client_id, program_names):
    client = find_client(client_id)
    if not client:
        return None

    for name in program_names:
        program = next((p for p in health_programs if p.name == name), None)
        if program and program.name not in client.enrolled_programs:
            client.enrolled_programs.append(program.name)
    return client

# 4. Search for a client
def find_client(client_id):
    return next((c for c in clients if c.client_id == client_id), None)

# 5. View client profile (used in the API below)

# 6. Expose client profile via API
@app.route("/api/client/<client_id>", methods=["GET"])
def get_client_profile(client_id):
    client = find_client(client_id)
    if not client:
        return jsonify({"error": "Client not found"}), 404

    profile = {
        "client_id": client.client_id,
        "name": client.name,
        "age": client.age,
        "enrolled_programs": client.enrolled_programs
    }
    return jsonify(profile)

# Example usage
if __name__ == "__main__":
    # Sample data setup
    create_health_program("HIV")
    create_health_program("Malaria")
    create_health_program("TB")

    register_client("001", "Alice", 30)
    register_client("002", "Bob", 24)

    enroll_client("001", ["HIV", "Malaria"])
    enroll_client("002", ["TB"])

    print("Health Information System running...")
    app.run(debug=True)
