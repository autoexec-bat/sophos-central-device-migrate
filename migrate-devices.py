#!/usr/bin/env python

# Sophos Central - Migrate Devices v.beta
# Aaron Bugal, Sophos, 2022
# This is not an officially supported script.
# Be kind to everyone, stay safe.
# Eat. Pray. Hack.
# I'm not a coder.
# This script has no error handling YOLO.
# Greets to 0xBennyV.

#import requests, json, getpass
import datetime
import requests 
import json
import getpass

# Welcome banner - totally redundant but a omage to nostalgic computing.
print("\nWelcome to...\n")
welcome_banner =  '''

 ▄████▄  ▓█████  ███▄    █ ▄▄▄█████▓ ██▀███   ▄▄▄       ██▓       ▓█████▄ ▓█████ ██▒   █▓ ██▓ ▄████▄  ▓█████ 
▒██▀ ▀█  ▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▓██▒       ▒██▀ ██▌▓█   ▀▓██░   █▒▓██▒▒██▀ ▀█  ▓█   ▀ 
▒▓█    ▄ ▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒██░       ░██   █▌▒███   ▓██  █▒░▒██▒▒▓█    ▄ ▒███   
▒▓▓▄ ▄██▒▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒██░       ░▓█▄   ▌▒▓█  ▄  ▒██ █░░░██░▒▓▓▄ ▄██▒▒▓█  ▄ 
▒ ▓███▀ ░░▒████▒▒██░   ▓██░  ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒░██████▒   ░▒████▓ ░▒████▒  ▒▀█░  ░██░▒ ▓███▀ ░░▒████▒
░ ░▒ ▒  ░░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░▓  ░    ▒▒▓  ▒ ░░ ▒░ ░  ░ ▐░  ░▓  ░ ░▒ ▒  ░░░ ▒░ ░
  ░  ▒    ░ ░  ░░ ░░   ░ ▒░    ░      ░▒ ░ ▒░  ▒   ▒▒ ░░ ░ ▒  ░    ░ ▒  ▒  ░ ░  ░  ░ ░░   ▒ ░  ░  ▒    ░ ░  ░
░           ░      ░   ░ ░   ░        ░░   ░   ░   ▒     ░ ░       ░ ░  ░    ░       ░░   ▒ ░░           ░   
░ ░         ░  ░         ░             ░           ░  ░    ░  ░      ░       ░  ░     ░   ░  ░ ░         ░  ░
░                                                                  ░                 ░       ░               
             ███▄ ▄███▓ ██▓  ▄████  ██▀███   ▄▄▄     ▄▄▄█████▓ ██▓ ▒█████   ███▄    █                        
            ▓██▒▀█▀ ██▒▓██▒ ██▒ ▀█▒▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █                        
            ▓██    ▓██░▒██▒▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒                       
            ▒██    ▒██ ░██░░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒                       
            ▒██▒   ░██▒░██░░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░                       
            ░ ▒░   ░  ░░▓   ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒                        
            ░  ░      ░ ▒ ░  ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░   ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░                       
            ░      ░    ▒ ░░ ░   ░   ░░   ░   ░   ▒    ░       ▒ ░░ ░ ░ ▒     ░   ░ ░                        
                   ░    ░        ░    ░           ░  ░         ░      ░ ░           ░                        
                                                                                                             

'''
print(welcome_banner)

# Set a chance to break this script if the user so desires.
print("\n\nPlease confirm that each statement below is TRUE!\n")
print("1. You have ENABLED Device Migration within the GLOBAL SETTINGS of the SENDING tenant.\n")
print("2. You have ENABLED Device Migration within the GLOBAL SETTINGS of the RECEIVING tenant.\n")
print("3. You have a device hostname to migrate.\n\n")
print("Type YES to continue or CTRL-C now to STOP and ABORT this process.\n")
input()

# Ask for the SENDING tenancy Client ID and Client Secret
# In the future we will use an external document or AWS secrets file to host credentials
print("\n\nPlease enter your Sophos Central API credentials - these are from your SENDING tenancy.\n\n")
send_client_id = input("Please enter your Client ID: ")
send_client_secret = getpass.getpass(prompt='Please enter your Client Secret: ')

# Ask for the RECEIVING tenancy Client ID and Client Secret
# In the future we will use an external document or AWS secrets file to host credentials
print("\n\nPlease enter your Sophos Central API credentials - these are from your RECEIVING tenancy.\n\n")
rec_client_id = input("Please enter your Client ID: ")
rec_client_secret = getpass.getpass(prompt='Please enter your Client Secret: ')

# Get JWT for each tenancy and data regions to accurately target API routes
def CentralAuthSender():
    # Get the SENDER tenants BearerToken
    authurl = "https://id.sophos.com/api/v2/oauth2/token"
    auth_req = "grant_type=client_credentials" + "&client_id=" + send_client_id + "&client_secret=" + send_client_secret + "&scope=token"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'SophosCentralMigrateDevices/1.0'
        }
    response = requests.request("POST", authurl, headers=headers, data=auth_req)
    # Take the response and then slot just the access_token from the returned JSON into our BearerToken var
    response = json.loads(response.text)
    global SendBearerToken
    SendBearerToken = response.get('access_token')
    print("\nObtaining Sending tenancy API access token.\n")

def CentralWhoamISender():
    # Tenant_ID enumeration process is below
    whoamiurl = "https://api.central.sophos.com/whoami/v1"
    payload = {}
    headers = {
        'Authorization': 'Bearer ' + SendBearerToken +'',
        'User-Agent': 'SophosCentralMigrateDevices/1.0'
    }
    tenantresponse = requests.request("GET", whoamiurl, headers=headers, data=payload)
    # Take the tenantresponse and then slot the TenantID and DataRegion returned JSON into our respective vars
    tenantresponse = json.loads(tenantresponse.text)
    global SenderTenantID
    SenderTenantID = tenantresponse['id']
    global SenderDataRegion
    SenderDataRegion = tenantresponse['apiHosts']['dataRegion']
    # The data region is important per the API specification as your data is stored in a specific AWS geo
    print("Successfully obtained Sending tenancy authorisation.  Sending tenancy details are:\n")
    # Print out the sending tenancy and region.
    print(SenderDataRegion)
    print(SenderTenantID)

def CentralAuthReceiver():
    # Get the RECEIVER tenants BearerToken
    authurl = "https://id.sophos.com/api/v2/oauth2/token"
    auth_req = "grant_type=client_credentials" + "&client_id=" + rec_client_id + "&client_secret=" + rec_client_secret + "&scope=token"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'SophosCentralMigrateDevices/1.0'
        }
    response = requests.request("POST", authurl, headers=headers, data=auth_req)
    response = json.loads(response.text)
    global RecBearerToken
    RecBearerToken = response.get('access_token')
    print("\nObtaining Receiving tenancy API access token.\n")

def CentralWhoamIReceiver():
    # Tenant_ID enumeration process is below
    whoamiurl = "https://api.central.sophos.com/whoami/v1"
    payload = {}
    headers = {
        'Authorization': 'Bearer ' + RecBearerToken +'',
        'User-Agent': 'SophosCentralMigrateDevices/1.0'
    }
    tenantresponse = requests.request("GET", whoamiurl, headers=headers, data=payload)
    # Take the tenantresponse and then slot the TenantID and DataRegion returned JSON into our respective vars
    tenantresponse = json.loads(tenantresponse.text)
    # Print out the response for debug purposes
    # print(tenantresponse)
    global RecTenantID
    RecTenantID = tenantresponse['id']
    global RecDataRegion
    RecDataRegion = tenantresponse['apiHosts']['dataRegion']
    # The data region is important per the API specification as your data is stored in a specific AWS geo
    print("Sucessfully obtained Receiver tenancy details.  Receiving tenancy details are:\n")
    # Print out the Receiving Tenancy and region
    print(RecDataRegion)
    print(RecTenantID)

def CentralGetMigrateTargets():
    # Search for the migration targets using a fuzzy search term, can be explicit
    print("\nA device or list of devices needs to be built to create the migration job.  You will now be asked")
    print("to define a fuzzy search term that will be used to search within HOSTNAMES of all devices within")
    print("your sending Central tenancy.  Be mindful of the term you use.")
    print("\nYou're about to SEARCH within the HOSTNAME, GroupName, AssociatedPerson and IP Address fields!\n")
    SearchKeyword = input("What is your search term: ")

    print("\nSearching for devices...  please hold...")
    DeviceHostnameSearch = SenderDataRegion + '/endpoint/v1/endpoints?search=' + SearchKeyword + '&view=basic'
    headers = {
        'X-Tenant-ID': SenderTenantID,
        'Authorization': 'Bearer ' + SendBearerToken +'',
        'User-Agent': 'SophosCentralMigrateDevices/1.0',
        'content-type': 'application/json'
    }
    
    global endpointdataresponse
    endpointdataresponse = requests.get(DeviceHostnameSearch, headers=headers)
    # Yep, let's yeet thru some more JSON
    global alldevicedata
    alldevicedata = json.loads(endpointdataresponse.text)
    # Type DICT returned.  Uncomment next line to visualise the targets on screen
    # print(alldevicedata)
    
    ep_values = []
    for ep in alldevicedata['items']:
        val: str
        if 'hostname' in ep:
            val = ep['id'] + ' | ' + ep['hostname']
        else:
            val = ep['id'] + ' | '
        ep_values.append(val)
    global logger_values
    logger_values = ep_values
    return ep_values

def CentralRefinedTargets():
    global target_list
    target_list = []
    for ep in alldevicedata['items']:
        val2: str
        val2 = ep['id']
        target_list.append(val2)
    return target_list
    
def CentralPOSTMigrateReceiveJob():
    # POST a receiver job within the receiving tenant using ALL of the enumerated clients from the previous step
    print("\nSetting' the targets...\n")
    url = RecDataRegion + '/endpoint/v1/migrations?mode=receiving'
    payload = json.dumps({
    "fromTenant": SenderTenantID,
    "endpoints": target_list
    })
    print(payload)
    headers = {
    'X-Tenant-ID': RecTenantID,
    'Authorization': 'Bearer ' + RecBearerToken +'',
    'Content-Type': 'application/json'
    }
    global ReceiverJobData
    ReceiverJobData = requests.request("POST", url, headers=headers, data=payload)
    # Get id of receive job and store it in a global.
    global ReceiveJobDetails
    ReceiveJobDetails = json.loads(ReceiverJobData.text)
    # Yeet thru JSON for Receiver job token.  Seems important.
    global ReceiveJobID
    ReceiveJobID = ReceiveJobDetails['id']
    global ReceiveJobToken
    ReceiveJobToken = ReceiveJobDetails['token']

def CentralPUTMigrateSendJob():
    # PUT a send job within the sending tenant to execute pushing the clients to their new forever home.
    print("\nExecute the Migration... good luck!")
    url = SenderDataRegion + "/endpoint/v1/migrations/" + ReceiveJobID
    payload = json.dumps({
    "token": ReceiveJobToken,
    "endpoints": target_list
    })
    headers = {
    'X-Tenant-ID': SenderTenantID,
    'Authorization': 'Bearer ' + SendBearerToken +'',
    'Content-Type': 'application/json'
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response.text)

CentralAuthSender()
CentralWhoamISender()
CentralAuthReceiver()
CentralWhoamIReceiver()
CentralGetMigrateTargets()
CentralRefinedTargets()
CentralPOSTMigrateReceiveJob()
CentralPUTMigrateSendJob()

# Now finish up and report to user.
print("\n")
print("\nProcess Completed.\n")
with open('migrate_data_report.txt', 'a') as logger:
        logger.write('\n')
        logger.write('Migration Job Started at: ' + datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))
        logger.write('\n')
        logger.write('Target devices:\n')
        for item in logger_values:
            logger.writelines([item])
            logger.writelines('\n')
        logger.write('Job Complete.\n\n')
