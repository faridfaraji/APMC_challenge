import os
import boto3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_cidr_list_from_env():
    """
    Retrieves the CIDR list from the CIDR_LIST environment variable.
    The variable should contain a comma-separated list of CIDR strings.
    Returns:
      list: A list of CIDR strings.
    """
    cidr_env = os.getenv("CIDR_LIST", "")
    if cidr_env:
        # Split by comma and remove extra whitespace
        return [cidr.strip() for cidr in cidr_env.split(",") if cidr.strip()]
    else:
        logger.error("CIDR_LIST environment variable is not set or empty.")
        return []


def create_input_security_group(cidr_list, region='us-west-2'):
    """
    Creates an AWS MediaLive Input Security Group with the provided CIDR list.
    :param cidr_list: List of CIDR strings to whitelist.
    :param region: AWS region.
    :return: Security Group ID if successful; None otherwise.
    """
    client = boto3.client('medialive', region_name=region)
    whitelist_rules = [{'Cidr': cidr} for cidr in cidr_list]
    try:
        response = client.create_input_security_group(WhitelistRules=whitelist_rules)
        security_group_id = response['SecurityGroup']['Id']
        logger.info("Input Security Group created successfully. ID: %s", security_group_id)
        return security_group_id
    except Exception as e:
        logger.error("Error creating input security group: %s", e)
        return None


def create_rtmp_input(input_name, security_group_id, region='us-west-2'):
    """
    Creates an AWS MediaLive RTMP input using an existing security group.
    :param input_name: The name for the MediaLive input.
    :param security_group_id: The MediaLive Input Security Group ID.
    :param region: AWS region.
    :return: API response if successful; None otherwise.
    """
    client = boto3.client('medialive', region_name=region)
    try:
        response = client.create_input(
            Name=input_name,
            Type='RTMP_PUSH',
            InputSecurityGroups=[security_group_id],
            Destinations=[{'StreamName': f"{input_name}-stream"}]
        )
        # The destination URLs may be nested differently depending on the API version
        destinations = response.get('Input', {}).get('Destinations', [])
        logger.info("RTMP Input created successfully. Ingest URLs: %s", destinations)
        return response
    except Exception as e:
        logger.error("Error creating RTMP Input: %s", e)
        return None


if __name__ == "__main__":
    input_name = "APMC_RTMPInput"
    # Retrieve the CIDR list from the environment variable
    cidr_list = get_cidr_list_from_env()
    if cidr_list:
        # Create the input security group.
        security_group_id = create_input_security_group(cidr_list)
        if security_group_id:
            create_rtmp_input(input_name, security_group_id)
    else:
        logger.error("No valid CIDR list provided. Exiting script.")
