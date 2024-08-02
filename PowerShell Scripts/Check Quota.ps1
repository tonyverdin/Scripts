# Prompt the user for the resource name
$ResourceName = Read-Host "Enter the resource search term (default, returns all values)"

# Prompt the user for the location
$Location = Read-Host "Enter the location (default, eastus)"

# Check if the location is empty
if ([string]::IsNullOrWhiteSpace($Location)) {

    $Location = "eastus"
}

# Execute the Azure CLI command with the provided parameters
if([string]::IsNullOrWhiteSpace($ResourceName))
{
    az vm list-usage --location $Location --output table
}
else
{
    az vm list-usage --location $Location --query "[?contains(name.value, '$ResourceName')].{Name:name.value, CurrentValue:currentValue, Limit:limit}" --output table
}