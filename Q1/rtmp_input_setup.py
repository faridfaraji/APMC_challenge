import boto3


def create_input_security_group(cidr_list, region='us-west-2'):
    """
    Creates an AWS MediaLive Input Security Group with the provided CIDR list.
    Parameters:
      cidr_list (list): List of CIDR strings to whitelist (e.g., ["203.0.113.0/24"]).
      region (str): AWS region.
    Returns:
      str: The Security Group ID if creation is successful; None otherwise.
    """
    client = boto3.client('medialive', region_name=region)
    try:
        # Prepare whitelist rules in the required format.
        whitelist_rules = [{'Cidr': cidr} for cidr in cidr_list]
        response = client.create_input_security_group(
            WhitelistRules=whitelist_rules
        )
        security_group_id = response['SecurityGroup']['Id']
        print("Input Security Group created successfully. ID:", security_group_id)
        return security_group_id
    except Exception as e:
        print("Error creating input security group:", e)
        return None


def create_rtmp_input(input_name, security_group_id, region='us-west-2'):
    """
    Creates an AWS MediaLive RTMP input using an existing security group.
    Parameters:
      input_name (str): The name for the MediaLive input.
      security_group_id (str): The MediaLive Input Security Group ID.
      region (str): AWS region.
    Returns:
      dict: The response from AWS MediaLive API if successful; None otherwise.
    """
    client = boto3.client('medialive', region_name=region)
    try:
        response = client.create_input(
            Name=input_name,
            Type='RTMP_PUSH',
            InputSecurityGroups=[security_group_id],
            Destinations=[
                {'StreamName': f"{input_name}-stream"}
            ]
        )
        print("RTMP Input created successfully. Input ID:", response['Input']['Id'])
        return response
    except Exception as e:
        print("Error creating RTMP Input:", str(e))
        return None


if __name__ == "__main__":
    input_name = "APMC_RTMPInput"
    # Replace with the appropriate CIDR range(s) that should be allowed to stream.
    cidr_list = ["203.0.113.0/24"]
    # First, create the input security group.
    security_group_id = create_input_security_group(cidr_list)
    # If the security group was created successfully, create the RTMP input.
    if security_group_id:
        create_rtmp_input(input_name, security_group_id)
