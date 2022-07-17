# sophos-api-migrate-devices

Sophos Central Migrate Devices

A simple python script to enumerate devices from a central tenancy and set a migration job to swing devices
from one tenancy to another.

NOTE:   To limit any accidental usage of this tool you will need to enter a 'fuzzy'
        device search term.  You can enter in an explcit device hostname that you wish
        to migrate.  Be mindfull that any fuzzy string you enter WILL capture any and ALL
        devices with a corresponding match and migrate them

Usage:

 #> python3 migrate-devices.py

Things to come:
- Preview of devices to be migrated.
- Migrate devices from a list within a file
- Status of migration job.

Open license, no restrictions and not officially supported by Sophos.

Thanks for reading.
