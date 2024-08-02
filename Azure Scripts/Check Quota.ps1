# Prompt the user for the resource name
$ResourceName = Read-Host "Enter the resource name (e.g., NCADSA10v4)"

# Check if the resource name is empty
if ([string]::IsNullOrWhiteSpace($ResourceName)) {
    Write-Host "Resource name cannot be empty. Exiting."
    exit
}

# Prompt the user for the location
$Location = Read-Host "Enter the location (e.g., eastus)"

# Check if the location is empty
if ([string]::IsNullOrWhiteSpace($Location)) {
    Write-Host "Location cannot be empty. Exiting."
    exit
}

# Execute the Azure CLI command with the provided parameters
az vm list-usage --location $Location --query "[?contains(name.value, '$ResourceName')].{Name:name.value, CurrentValue:currentValue, Limit:limit}" --output table
