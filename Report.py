import subprocess
import logging


logging.basicConfig(filename='app.log',level=logging.INFO)

def eventLog():
        name = input("Report Name: ")
        logging.info(name)
        targetLogName = input("Target Log Name: ")
        logging.info(targetLogName)
        eventCount = input("Event Count: ")
        logging.info(eventCount)
        eventType = input("Event Type: ")
        logging.info(eventType)
        comando = "powershell -Executionpolicy ByPass -File ReportEvent.ps1 " \
                  " -ReportFile " + name + " -targetLogName " + targetLogName + "" \
                " -eventCount " + eventCount + " -eventType " + eventType
        logging.info(comando)
        runningProcesses = subprocess.check_output(comando)
        print(runningProcesses.decode())

# eventLog()

def process():
    size = input("Process Size: ")
    name = input("Report Name: ")
    comando = "powershell -Executionpolicy ByPass -File ReportProcess.ps1 -ReportFile " + name + " -Size " + size
    print(comando)
    runningProcesses = subprocess.check_output(comando)
    print(runningProcesses.decode())
# process()