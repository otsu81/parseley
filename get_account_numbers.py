import boto3

class ActiveAccounts:
    def get_active_account_ids(self, profile):    
        # create organizations session with valid credentials
        session = boto3.Session(profile_name=profile)
        org = session.client('organizations')

        # create array for account IDs, get first response
        account_ids = []
        response = org.list_accounts()

        # at least once, get all IDs from all accounts to account_ids
        while True:
            accounts = response.get('Accounts')
            for account in accounts:
                # if status ACTIVE, append to list
                if account.get('Status') == 'ACTIVE':
                    account_ids.append(account.get('Id'))
            next_token = response.get('NextToken')
            # if there is a NEXT token, repeat until there is no NextToken
            if next_token != None:
                response = org.list_accounts(NextToken=response.get('NextToken'))
            else:
                break
            
        return account_ids
