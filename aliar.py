import requests

# Replace these variables with your actual values
from credentials import *

# Namecheap API endpoint for adding an email alias
url = 'https://api.namecheap.com/xml.response'

# Parameters for the API call
params = {
    'ApiUser': api_user,
    'ApiKey': api_key,
    'UserName': username,
    'ClientIp': client_ip,
    'Command': 'namecheap.domains.dns.setEmailForwarding',
    'mailbox1': '1', 'ForwardTo1': alias_email,
    'mailbox2': '2', 'ForwardTo2': alias_email,
    'mailbox3': '3', 'ForwardTo3': alias_email,
    'mailbox4': '4', 'ForwardTo4': alias_email,
    'mailbox5': '5', 'ForwardTo5': alias_email,
    'mailbox6': '6', 'ForwardTo6': alias_email,
    'mailbox7': '7', 'ForwardTo7': alias_email,
    'mailbox8': '8', 'ForwardTo8': alias_email,
    'mailbox9': '9', 'ForwardTo9': alias_email,
    'mailbox10': '10', 'ForwardTo10': alias_email,
    'mailbox11': '11', 'ForwardTo11': alias_email,
    'mailbox12': '12', 'ForwardTo12': alias_email,
    'mailbox13': '13', 'ForwardTo13': alias_email,
    'mailbox14': '14', 'ForwardTo14': alias_email,
    'mailbox15': '15', 'ForwardTo15': alias_email,
    'mailbox16': '16', 'ForwardTo16': alias_email,
    'mailbox17': '17', 'ForwardTo17': alias_email,
    'mailbox18': '18', 'ForwardTo18': alias_email,
    'mailbox19': '19', 'ForwardTo19': alias_email,
    'mailbox20': '20', 'ForwardTo20': alias_email,
    'mailbox21': '21', 'ForwardTo21': alias_email,
    'mailbox22': '22', 'ForwardTo22': alias_email,
    'mailbox23': '23', 'ForwardTo23': alias_email,
    'mailbox24': '24', 'ForwardTo24': alias_email,
    'mailbox25': '25', 'ForwardTo25': alias_email,
    'mailbox26': '26', 'ForwardTo26': alias_email,
    'mailbox27': '27', 'ForwardTo27': alias_email,
    'mailbox28': '28', 'ForwardTo28': alias_email,
    'mailbox29': '29', 'ForwardTo29': alias_email,
    'mailbox30': '30', 'ForwardTo30': alias_email,
    'mailbox31': '31', 'ForwardTo31': alias_email,
    'mailbox32': '32', 'ForwardTo32': alias_email,
    'mailbox33': '33', 'ForwardTo33': alias_email,
    'mailbox34': '34', 'ForwardTo34': alias_email,
    'mailbox35': '35', 'ForwardTo35': alias_email,
    'mailbox36': '36', 'ForwardTo36': alias_email,
    'mailbox37': '37', 'ForwardTo37': alias_email,
    'mailbox38': '38', 'ForwardTo38': alias_email,
    'mailbox39': '39', 'ForwardTo39': alias_email,
    'mailbox40': '40', 'ForwardTo40': alias_email,
    'mailbox41': '41', 'ForwardTo41': alias_email,
    'mailbox42': '42', 'ForwardTo42': alias_email,
    'mailbox43': '43', 'ForwardTo43': alias_email,
    'mailbox44': '44', 'ForwardTo44': alias_email,
    'mailbox45': '45', 'ForwardTo45': alias_email,
    'mailbox46': '46', 'ForwardTo46': alias_email,
    'mailbox47': '47', 'ForwardTo47': alias_email,
    'mailbox48': '48', 'ForwardTo48': alias_email,
    'mailbox49': '49', 'ForwardTo49': alias_email,
    'mailbox50': '50', 'ForwardTo50': alias_email,

    'mailbox1000': 'bank', 'ForwardTo1000': alias_email,
    'mailbox1001': 'council', 'ForwardTo1001': alias_email,
    'mailbox1002': 'elctricity', 'ForwardTo1002': alias_email,

    'DomainName': domain
}

# Make the API call
response = requests.post(url, params=params)

# Check the response
if response.status_code == 200:
    print("Success: ", response.text)
else:
    print("Error: ", response.status_code, response.text)
