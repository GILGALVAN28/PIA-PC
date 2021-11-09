<#
.synopsis
Event Log Reprt 

- User Specified Target EventLog
- User Specifies the number of newest Log Entries to Report
- User Specifies the Entry Type to target, for example warning, error, information etc.
- User Specifies the HTML Report Title

The script will produce an HTML output report with EventLog information.

.parameter targetLogName
Specifies the name of the log file to process
.parameter eventCount
Specifies the number of newest events to consider
.parameter eventType
Specifies the eventType of interest
.parameter reportFile
Specifies the HTML Report Name

.example
EventProcessor
Execution of ReportEvent without parameters uses the default settings
targetLogName system
eventType Error
eventCount 20
ReportFile "Reporte.html"

.example
ReportEvent -targetLogName security

.example
ReportEvent -ReporTitle "Dalily Report"

.example
ReportEvent -targetLogName security -eventCount 35 -eventType Information
#>


param([string]$ReportFile = "Reporte.html",
      [string]$targetLogName = "system",
      [int]$eventCount = 20,
      [string]$eventType = "Error" )
 
$targetComputer=$env:COMPUTERNAME       

# Create HTML
$Header = @"
<style>
TABLE {border-width: 1px; border-style: solid; border-color: black; border-collapse: collapse;}
TD {border-width: 1px; padding: 3px; border-style: solid; border-color: black;}
th {
background: #eee;
font-family: Courier New
}
tr{
    font-family: Courier New
}
p{
    font-family: Courier New
}
</style>
<p>
<b> $reportTitle $rptDate </b>
<p>
Event Log Selection: <b>$targetLogName </b>
<p>
Target Computer(s) Selection: <b> $targetComputer </b>
<p>
Event Type Filter: <b> $eventType </b>
<p>
"@

# MAIN
Get-Eventlog -ComputerName $targetComputer -LogName $targetLogName -Newest $eventCount -EntryType $eventType | 
ConvertTo-Html -Head $Header -Property TimeGenerated, EntryType, Message | Out-File $ReportFile
