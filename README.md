# Learning Python: Computer Engineering Foundations 🚀

This repository tracks my journey learning Python backend development and software stability during my first year as a Computer Engineering undergraduate.

## 📂 Repository Structure

*   `01_variables.py` to `03_deposit_logic.py` - Core arithmetic operations and variable scope.
*   `04_banking_menu.py` - Control flow optimization using conditional matching and loops.
*   `05_secure_receipt.py` - String slicing implementation for data privacy (account masking).
*   `06_transaction_history.py` - Array manipulation and data streaming using Python lists.
*   `07_user_profile.py` - Data mapping and dynamic records management with nested dictionaries.
*   `09_secure_banking.py` - Exception handling using `try...except` to create stable code.

---

## 🏆 Featured Capstone: Multi-User Core Banking System (`core_banking_system.py`)
A robust, terminal-based backend application simulating core banking operations for multiple concurrent users. This application combines all 9 foundational building blocks.

### 🛠️ Architecture & Concepts Applied
*   **Database Simulation:** Utilizes nested dictionaries to securely isolate independent customer record profiles.
*   **Ledger Streams:** Maps unique mutation arrays (lists) to track an immutable transaction audit history for each client.
*   **Crash-Proof Core:** Wraps critical user runtime inputs in proactive `try...except` frameworks to intercept `ValueError` disruptions.
*   **Data Masking:** Leverages string parsing syntax (`account[-4:]`) to dynamically secure customer account information.

### ⚙️ System Features
1. Multi-Account Authentication and validation.
2. Crash-proof balance updates (Deposits and Withdrawals).
3. Live statement generation with tracking loops.
