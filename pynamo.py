from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute, UnicodeSetAttribute, UTCDateTimeAttribute
)
from pynamodb.indexes import (
    GlobalSecondaryIndex, AllProjection, LocalSecondaryIndex
)
from datetime import datetime
from parse_aws_variables import ParseAWSEnvVariables
import os

"""The PynamoDB model for the account database"""
class AccountModel(Model):
    
    variables = ParseAWSEnvVariables(os.environ['HOME'] + '/.aws/credentials')
    profile = 'cmslab'
    os.environ['AWS_ACCESS_KEY_ID'] = variables.get_credentials(profile).get('AWS_ACCESS_KEY_ID')
    os.environ['AWS_SECRET_ACCESS_KEY'] = variables.get_credentials(profile).get('AWS_SECRET_ACCESS_KEY')

    class Meta:
        table_name = "cms-accounts"
        region = 'eu-west-1'

    accountNbr = UnicodeAttribute(hash_key=True)
    roleName = UnicodeAttribute(default=0)
    description = UnicodeAttribute(default=None)
    timestamp = UTCDateTimeAttribute(default=None)

if not AccountModel.exists():
        AccountModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)