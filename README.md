# Navigator-API-Server
2020 Presidential Hackathon - WayFic team

This RestFUL api server is built for integrating with the navigator designed by KingWay Technology
## Install Guide
> Under your python env (>3.7)
Ensure you have requirement module
```python
pip install -r requirement.txt
```
Then
```python
cd navigator
```
Run the server
```python
python __main__.py
```
Init database
```python
python manage.py db init
```
Then migrate
```python
python manage.py db migrate
```
Upgrade
```python
python manage.py db upgrade
```
If you want to use flask command, please specify config
```python
export FLASK_ENV=development
export FLASK_APP=__main__.py
```
Then test the command.
```python
python -m flask run
```
## Swagger UI
**http://0.0.0.0:8080/api/v1/ui/**

## Health check
**http://0.0.0.0:8080/api/v1/task/1**
