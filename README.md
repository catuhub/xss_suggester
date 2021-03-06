# xss_suggester
A framework that suggests actions to perform during a web application penetration test, based on a multiobjective reinforcement learning environment. Currently supports XSS vulnerabilities detection. Try it on OWASP WAVSEP benchmark!

## Requirements
Python 2.7

## Installation
```
git clone https://github.com/catuhub/xss_suggester.git

cd xss_suggester

pip install -r requirements.txt

python app.py
```
Point your browser to localhost:5000

## Dockerfile
```
docker build . -t xss_suggester

docker run -d -p 5000:5000 xss_suggester
```

## Test with Wavsep
```
docker run -d -p 8080:8080 owaspvwad/wavsep
```
Point your browser to localhost:8080/wavsep/active/Reflected-XSS/RXSS-Detection-Evaluation-GET/

Pick a test case, follow the suggestions and check if you can find XSS vulnerabilities.
