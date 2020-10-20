import boto3, json

#client = boto3.client('waf')
session = boto3.Session(profile_name='default')
#waf2_client = boto3.client('wafv2')
waf2_client=session.client('wafv2')

name = 'StandardIPList1'
def create_ip_set():
    response = waf2_client.create_ip_set(
        Name=name,
        Scope='REGIONAL',
        Description='this is description on ip set',
        IPAddressVersion='IPV4',
        Addresses=[
            '10.0.0.0/32'
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
create_ip_set()

response = waf2_client.list_ip_sets(
    Scope='REGIONAL',
    Limit=1
)
Ipset_ARN = response.get("IPSets")[0].get("ARN")


#name = 'Digital-Emerging-Dev-sizeconstraint5'
scope = 'REGIONAL'
transfr_type='NONE'
import sys
rulefile=sys.argv[1]
with open(rulefile) as rule_file:
    rule=json.load(rule_file)
    print(rule)
updated_rule={}
updated_rule=rule.copy()
for each in updated_rule:
    each["Name"]=f'{name}-{each["Name"]}'
    if each.get("Priority")==9:
        each.get("Statement").get("IPSetReferenceStatement")["ARN"]=Ipset_ARN
name = 'Labtest5'
def sizeconstraint_statement(name=name,rules=[]):
    response = waf2_client.create_web_acl(
        Name=name,
        Scope= scope,#'CLOUDFRONT','REGIONAL',
        DefaultAction={
            'Block': {}
        },
        Description='sample description123',
        Rules=rules,
        VisibilityConfig={
            'SampledRequestsEnabled': True,
            'CloudWatchMetricsEnabled': True,
            'MetricName': 'samplemetricname'
        }
    )
    print(response)

#below function call will create all rules in single webacl
# command -- python sizeconstraintstatement.py 'sizeconstraintrule.json'
sizeconstraint_statement(name = name, rules=updated_rule)
#uncomment below function call if we don't want the empty webacl with zero rules
#command--  python sizeconstraintstatement.py 'sizeconstraintrule.json'
sizeconstraint_statement(name = 'sizeconemptyrule')

#regexset
#client = boto3.client('waf')
waf2_client = boto3.client('wafv2')
name = 'test-regex1'
scope = 'REGIONAL'
transfr_type='NONE'
response = waf2_client.create_regex_pattern_set(
    Name=name,
    Scope=scope,
    Description='string',
    RegularExpressionList=[
        {
            'RegexString': '<!DOCTYPE\s+[^\s]+\s+(?:SYSTEM|PUBLIC)'
        },
        {
            'RegexString': '<!ENTITY\s+[^\s]+\s+(?:SYSTEM|PUBLIC)'
        }
    ],
    Tags=[
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
)
#uncomment below to create regex pattern set
print(response)


