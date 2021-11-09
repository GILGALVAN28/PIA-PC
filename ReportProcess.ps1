<#
.synopsis
Processes Report

- User Specifies the size (greater than) for the script to search in the processes of the computer
- User Specifies the HTML Report Title

The script will produce an HTML output file containing details of processes greater then the size specified.

.parameter ReportFile
Specifies the HTML Report Title
.parameter size
Specifies the minimum number size in bytes processes to consider in the search

.example
ReportProcess
Execution of ReportProcess without parameters uses the default settings of
ReportFile Reporte.html"
size 100000000 (bytes)

.example
ReportProcess -ReporTitle "Report251021.html"

.example
ReportProcess -size 80000000

.example
ReportProcess -size 80000000 -ReportTitle "25-10-21.html"
#>

param([string]$ReportFile = "Reporte.html",
      [int]$Size = 10000000)

$targetComputer=$env:COMPUTERNAME

# Create HTML
$Header = @"
<style>
TABLE {
    border-width: 1px; border-style: solid; border-color: black; border-collapse: collapse;}
TD{border-width: 1px; padding: 3px; border-style: solid; border-color: black;}
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
<b> Event Log Report $reportDate </b>
<p>

<p>
Target Computer(s) Selection: <b> $targetComputer </b>
<p>
Processes Grater than: $Size bytes 
<p>
"@

# MAIN
Get-Process | Where-Object {$_.WorkingSet -gt $Size} | Sort-Object -Descending CPU |
ConvertTo-Html -Head $Header -Property CPU , Id, ProcessName | Out-File $ReportFile
