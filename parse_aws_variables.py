"""
Parses an AWS credentials file and create a dictionary with 
K:profilename V:{AWS_ACCESS_KEY_ID;AWS_SECRET_ACCESS_KEY}
"""
import os

class ParseAWSEnvVariables():
    
    creds = {}

    def __init__(self, credentials_file):
        with (open(credentials_file, 'r')) as f:
            for line in f:
                line = line.strip()
                if line.startswith('[') and line.endswith(']'):
                    profile_name = line[1:-1]
                    ak = f.readline().strip().replace(' ','').split('=')
                    sak = f.readline().strip().replace(' ','').split('=')
                    keys = {ak[0].upper(): ak[1], sak[0].upper(): sak[1]}
                    self.creds[profile_name] = keys
                    
    def get_credentials(self, profile_name):
        return self.creds.get(profile_name)