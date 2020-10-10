import boto3, json

#client = boto3.client('waf')
session = boto3.Session(profile_name='default')
#waf2_client = boto3.client('wafv2')
waf2_client=session.client('wafv2')
#name = 'Digital-Emerging-Dev-sizeconstraint5'
name = 'waftest1'
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

