import boto3
import os
from parse_engine import ParseEngine
from pynamo import AccountModel
from get_account_numbers import ActiveAccounts

"""
main method to do the needful
"""
def main():
    # enter master credentials used for role switching
    profile = 'cdt'
    session = boto3.Session(profile_name=profile)
    sts = session.client('sts')

    # use CB accout for getting the Organizations account
    active_accounts = ActiveAccounts().get_active_account_ids('cb')

    for a in active_accounts:
        try:
            ddb_entry = AccountModel.get(a)
            do_stuff(session, sts, ddb_entry)
        except AccountModel.DoesNotExist:
            pass

"""
do-method to do whatever you want to do
"""
def do_stuff(session, sts_client, ddb_entry):
    ec2_client = fetch_client_with_temporary_credentials(
        session, sts_client, 'ec2', ddb_entry
        )
    print(ec2_client.describe_instances())

"""
Use the credentials from the profile entered in the main method to assume role with STS
for account information specified in the DynamoDB entry used as input
"""
def fetch_client_with_temporary_credentials(session, sts_client, client_type, ddb_entry):
    arn = "arn:aws:iam::" + ddb_entry.accountNbr + ":role/" + ddb_entry.roleName
    try:
        sts_response = sts_client.assume_role(
            DurationSeconds = 900,
            RoleArn = str(arn),
            RoleSessionName = 'CMSParseleySession'
        )
        client = session.client(
            client_type,
            aws_access_key_id = sts_response.get('Credentials').get('AccessKeyId'),
            aws_secret_access_key = sts_response.get('Credentials').get('SecretAccessKey'),
            aws_session_token = sts_response.get('Credentials').get('SessionToken')
        )
        return client
    except boto3.exceptions.botocore.errorfactory.ClientError as e:
        print(repr(e))

if __name__ == '__main__':
    main()