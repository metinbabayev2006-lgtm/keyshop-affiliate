# Quick check if you are in the right folder
Write-Host "Current folder:" (Get-Location)
Write-Host "Files:" 
Get-ChildItem -Name

Write-Host "Python:" 
py --version
