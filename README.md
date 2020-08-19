# Account Manager Pro (CLI)

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Architecture: SOLID](https://img.shields.io/badge/Architecture-SOLID-orange.svg)](#)

A professional-grade, modular CLI application for managing web service accounts, developed with a focus on clean code, type safety, and architectural scalability.

## 🚀 Key Features

- **Modular Domain Models:** Distinct layers for `Service`, `Person`, and `Account` entities.
- **Dependency Injection (DI):** Decoupled database and business logic for maximum testability.
- **Robust Persistence:** SQLite wrapper with full CRUD support and safe parameter binding.
- **Smart UI:** Interactive CLI menu system with automated schema verification.
- **Security:** Built-in password masking for secure credential display.
- **Resilient Error Handling:** Custom decorators for unified exception management and logging.

## 🏗️ Architectural Overview

The project follows a modified **Active Record** pattern combined with **Dependency Injection**.

- **`databases.py` (Data Access Layer):** Low-level SQLite wrapper providing an abstraction over raw SQL.
- **`services.py`, `persons.py`, `accounts.py` (Domain Layer):** Business logic and entity state management.
- **`decorators.py` (Cross-Cutting Concerns):** Aspect-oriented approach to error handling.
- **`app.py` (Application Layer):** Orchestrates dependencies and handles the CLI loop.

## 🧪 Testing Suite

Quality is a first-class citizen in this project. We use `unittest` with `mock` to ensure logic is isolated from database side effects.

### Run Unit Tests
```bash
export PYTHONPATH=$PYTHONPATH:.
python3 -m unittest discover tests
```

The tests cover:
- Dependency injection integrity.
- Entity cache synchronization.
- Database interaction mocking.

## 🛠️ Getting Started

### Prerequisites
- Python 3.8 or higher.
- No external DB required (uses local SQLite).

### Installation
1. Clone the repository.
2. (Optional) Create a virtual environment:
   ```bash
   python3 -m venv venv && source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
Start the interactive CLI:
```bash
python3 app.py
```

## 📈 Future Roadmap
- [ ] Implement **Data Mapper** pattern to further decouple entities from persistence.
- [ ] Add **AES-256 encryption** for password storage.
- [ ] Export/Import functionality (JSON/CSV).
- [ ] Integration with HashiCorp Vault.

---
*Developed as a demonstration of Senior-level Python architectural patterns.*
