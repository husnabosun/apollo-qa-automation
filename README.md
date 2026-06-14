# Apollo QA Automation Project

Selenium + PyTest based end-to-end UI test framework for Practice Software Testing.

---

## Tech Stack & Architecture

* **Language:** python 3.11.5 or 3.11+
* **Test Runner:** pytest
* **Automation Tool:** selenium webdriver
* **Web driver manager:** automatic Chrome binary management
* **Configuration Management:** python-dotenv

##  Repository Structure

```text
apollo-qa-automation/
├── .vscode/
├── tests/
│   ├── test_add_to_cart.py      # Product search + add cart flow
│   ├── test_login_invalid.py    # Invalid login scenario
│   ├── test_login_success.py    # Successful login flow
│   └── test_register.py        # New account creation
│
├── utils/
│   └── driver.py               # Headless Chrome factory
│
├── conftest.py                 # PyTest fixtures (browser setup/teardown)
├── .env.example                # Environment variable template
├── .gitignore
└── requirements.txt
```

## Notes
* ```utils/driver.py``` — Keeps browser config separate from test logic.
* ```conftest.py``` — Handles browser open/close for each test automatically. A short delay between teardowns prevents port conflicts.
* Explicit waits — Uses WebDriverWait + expected_conditions instead of ```time.sleep```.

## Setup
1. Clone the tracking repository onto your local path and access the working project root directory
```bash
git clone https://github.com/husnabosun/apollo-qa-automation.git
cd apollo-qa-automation
```
2. Deploy an isolated local virtual ecosystem to containerize development boundaries:
```bash
# On Windows
python -m venv venv
.\venv\Scripts\Activate

# On macOS / Linux
python3 -m venv venv
source venv/bin/activate
```
3. Sync the active execution footprint against the required ecosystem baseline binaries
```bash
pip install -r requirements.txt
```
4. Generate your local explicit configuration properties out of the distributed global template:
```bash
# Windows
cp .env.example .env

# macOS / Linux
cp .env.example .env
```
Note : Populate the generated ```.env``` file with functional targeted portal account credentials if customized baseline validation paths are preferred.

## Test Execution
The execution pipeline parameters are optimized to run fully headlessly to balance speed and local processing performance.

### -Run All Automation Suites Sequentially
```bash
python -m pytest -v -s
```
### - Run Scenario Test Paths Individually
By changing the file name each test can be executed individually.
```bash
python -m pytest tests/test_login_success.py -v -s
```

## Evaluation Status
The operational behavior successfully meets structural targets, showing absolute resilience across repeated framework evaluations.
```bash
tests/test_add_to_cart.py::test_add_to_cart PASSED
tests/test_login_invalid.py::test_login_invalid_credentials PASSED
tests/test_login_success.py::test_login_success PASSED
tests/test_register.py::test_register_success PASSED

======================= 4 passed in 36.24s =======================
```
