For permanent access:
- Windows add your API keys in `System Properties - Environment Variables - New` Restart your PC if needed.
- Use PyCharm - Edit Configurations - Environment variables.

For one-time access:
- Windows -> use scripts
- Linux `export PASSWORD=supersecret`

### Configuration
- Add environment variables like:
- - `REPORT_KEY="YOUR_REPORT_KEY"`
- - `MY_SQL_SERVER="YOUR_SQL_SERVER"` 
- - `MY_SQL_PORT="YOUR_SQL_PORT"` 
- - `PHP_MY_ADMIN_USER="YOUR_USER"`
- - `PHP_MY_ADMIN_PASSWORD="YOUR_PASSWORD"`
- app/app_config.py

### Installing and running

For permanent access Linux:
- Linux add your API keys in .bashrc
or
- Add your API key into environment variables.
- On linux:
- `sudo echo "REPORT_KEY="YOUR_REPORT_KEY"" >> /etc/environment && source /etc/environment`