# wapt_suggester
A framework that suggests actions to perform during a web application penetration test, based on a multi-agent reinforcement learning environment

## Requirements
Python 2.7

## Installation
```
git clone https://github.com/catuhub/reinforced_xss.git

cd wapt_suggester

pip install -r requirements.txt

python app.py
```
Point your browser to localhost:5000

## Dockerfile
```
docker build . -t wapt_suggester

docker run -d -p 5000:5000 wapt_suggester
```

## Test with Wavsep
```
docker run -d -p 8080:8080 owaspvwad/wavsep
```
Point your browser to localhost:8080/wavsep/active/Reflected-XSS/RXSS-Detection-Evaluation-GET/

Pick a test case, follow the suggestions and check if you can find XSS vulnerabilities.
