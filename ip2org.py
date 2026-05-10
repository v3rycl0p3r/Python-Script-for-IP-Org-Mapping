import pandas as pd
import requests
import time

# Load the Excel file
input_file = "ip.xlsx"  # Make sure this is in the same directory
df = pd.read_excel(input_file)

# Function to fetch organization from ipinfo.io
def get_organization(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=10)
        data = response.json()
        return data.get("org", "Unknown")
    except Exception as e:
        return "Error"

# Apply the function to each IP
df['organization'] = df['IP address'].apply(get_organization)
time.sleep(1)  # optional: pause to avoid rate limit if running many IPs

# Save the result to a new Excel file
output_file = "ip_with_organizations.xlsx"
df.to_excel(output_file, index=False)

print(f"✓ Organization info saved to: {output_file}")
