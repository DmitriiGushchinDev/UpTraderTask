# UpTrader Expanded Menu Taks
### 1. Clone repo and change directory 

```bash
git clone https://github.com/DmitriiGushchinDev/UpTraderTask.git
cd UpTraderTask
```
### 2. Create and activate virtual environment.
```bash
python -m venv .venv
source .venv/bin/activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run migratoins
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Create super user
```bash
python manage.py createsuperuser
```
### 6. Start the server
``bash
python manage.py runserver
```
