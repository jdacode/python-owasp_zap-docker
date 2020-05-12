# *********************************************************************
# ********************** CONFIGURATION ********************************
# *********************************************************************
import time
from pprint import pprint
from zapv2 import ZAPv2

# RUN FIRST OWASP ZAP ON YOUR COMPUTER
# GO TO MENU>TOOLS>OPTIONS>API
# THERE YOU CAN FIND Api Key AND OWASP ZAP LOCAL ADDRESS

# The value of api must match api.key when running the daemon
apiKey = ''

# Define the target to scan:
target = 'http://172.17.0.3:5000'

# Also if you are not running ZAP on port 8080 then you must include the line below
# with the correct port numbers.
zap = ZAPv2(apikey=apiKey, proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})

zap.urlopen(target)
# *********************************************************************
# ********************** CONFIGURATION ********************************
# *********************************************************************

''''''
# *********************************************************************
# ********************** SPIDERING ************************************
# *********************************************************************
print("*** Spidering start ***")
print('Spidering target {}'.format(target))
# The scan returns a scan id to support concurrent scanning
scanID = zap.spider.scan(target)
while int(zap.spider.status(scanID)) < 100:
    # Poll the status until it completes
    print('Spider progress %: {}'.format(zap.spider.status(scanID)))
    time.sleep(1)
print("*** Spidering completed ***")

# Prints the URLs the spider has crawled
print('\n'.join(map(str, zap.spider.results(scanID))))
# If required post process the spider results

# TODO: Explore the Application more with Ajax Spider or Start scanning the application for vulnerabilities

# *********************************************************************
# ********************** SPIDERING ************************************
# *********************************************************************


# *********************************************************************
# ********************** ACTIVE SCAN **********************************
# *********************************************************************
print("*** Performing active scan ***")
# TODO : explore the app (Spider, etc) before using the Active Scan API, Refer the explore section
print('Active Scanning target {}'.format(target))
scanID = zap.ascan.scan(target)
print(scanID)
while int(zap.ascan.status(scanID)) < 100:
    # Loop until the scanner has finished
    print('Scan progress %: {}'.format(zap.ascan.status(scanID)))
    time.sleep(5)
print('*** Active Scan completed ***')
# *********************************************************************
# ********************** ACTIVE SCAN **********************************
# *********************************************************************


# *********************************************************************
# ********************** PASSIVE SCAN *********************************
# *********************************************************************
print("*** Performing passive scan ***")
# TODO : explore the app (Spider, etc) before using the Passive Scan API, Refer the explore section for details
print('Passive Scanning target {}'.format(target))
while int(zap.pscan.records_to_scan) > 0:
    # Loop until the passive scan has finished
    print('Records to passive scan : ' + zap.pscan.records_to_scan)
    time.sleep(2)
print('*** Passive Scan completed ***')
# *********************************************************************
# ********************** PASSIVE SCAN *********************************
# *********************************************************************


# Print vulnerabilities found by the scanning
print('Hosts: {}'.format(', '.join(zap.core.hosts)))
print('Alerts: ')
pprint(zap.core.alerts(baseurl=target))


# *********************************************************************
# ********************** REPORTING ************************************
# *********************************************************************
# HTML
with open('report.html', 'w') as f:
    f.write(zap.core.htmlreport())

# XML


with open('report.xml', 'w') as f:
    f.write(zap.core.xmlreport())    


# *********************************************************************
# ********************** REPORTING ************************************
# *********************************************************************
