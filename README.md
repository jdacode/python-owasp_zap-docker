## Scanning websites with python and owasp zap

## ALERT 

Warning!!!
```sh

     In many jurisdictions it is illegal to "test" web sites/applications without permission. 
     Please be aware that you should only use ZAP with targets that you have been specifically 
     given permission to test. 

```

## Requirements

- Python 3
- python-owasp-zap-v2.4
- owasp/zap2docker-stable


## Launch 

Starting a headless scan in ZAP
```sh

    docker pull owasp/zap2docker-stable
    docker run -p 8090:8090 -i owasp/zap2docker-stable zap.sh -daemon -port 8090 -host 0.0.0.0 -config api.addrs.addr.name=.* -config api.addrs.addr.regex=true -config api.disablekey=true

```

From a browser
```sh

    http://localhost:8090

```

From python
```sh

    python owasp.py

```

Reporting
```sh

    ./report.html
    ./report.xml

```