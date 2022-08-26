import click
import boto3

from decouple import config
from prettytable import PrettyTable


@click.command()
@click.argument('resource')
@click.option('--profile', default=config('DEFAULT_AWS_PROFILE', None),
              help='AWS CLI Profile to use.')
def main(resource, profile):
    if profile:
        boto3.setup_default_session(profile_name=profile)

    if resource == 'ec2':
        list_aws_instances()
    elif resource == 'rds':
        list_aws_rds()
    else:
        with click.get_current_context() as ctx:
            click.echo(ctx.get_help())
            ctx.exit()


def list_aws_instances():
    ec2 = boto3.resource('ec2')
    table = PrettyTable(align='l')
    table.field_names = ['State', 'Name', 'ID', 'Key Pair', 'Public IP',
                         'Public Address']

    for instance in ec2.instances.all():
        try:
            instance_name = [x for x in instance.tags if x['Key'] == 'Name']
            instance_name = instance_name[0]['Value']
        except TypeError:
            instance_name = '-'

        table.add_row([
            instance.state['Name'].title(),
            instance_name,
            instance.id,
            instance.key_name,
            instance.public_ip_address,
            instance.public_dns_name
        ])

    print(table)


def list_aws_rds():
    resource = boto3.client('rds')
    instances = resource.describe_db_instances()

    table = PrettyTable(align='l')
    table.field_names = ['State', 'Engine', 'Name', 'Type', 'Address',
                         'MasterUser']

    for instance in instances['DBInstances']:
        table.add_row([
            instance['DBInstanceStatus'].title(),
            instance['Engine'],
            instance['DBInstanceIdentifier'],
            instance['DBInstanceClass'],
            instance['Endpoint']['Address'],
            instance['MasterUsername']
        ])

    print(table)


if __name__ == '__main__':
    main()
