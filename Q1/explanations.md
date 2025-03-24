

### **Python (Boto3)**  
```python
import boto3

# Initialize MediaLive client
client = boto3.client(
    'medialive',
    region_name=region,  # Replace with your region
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY'
)

# Create RTMP input
response = client.create_input(
    Name=input_name,
    Type='RTMP_PUSH',
    InputSecurityGroups=[security_group_id],
    Destinations=[
        {'StreamName': f"{input_name}-stream"}
    ]
)

# Print RTMP ingest URLs
print("RTMP Push URLs:", response['Destinations'])
```
Alternatively you could use Terraform to create the resources (rtmp input) and its associated security. But the python script works just fine.

### **Python (Boto3)** 
In the ffmpeg command the rtmp://<MEDIALIVE_RTMP_URL>/app/APMC_RTMPInput-stream: is the MediaLive RTMP URL returned to us by the python script
```
ffmpeg -i aspect43.mp4 -vf "scale=-1:720, pad=1280:720:(1280-iw)/2:0" "rtmp://<MEDIALIVE_RTMP_URL>/app/APMC_RTMPInput-stream"
```


### ** security **

if the IP address changes we need to change the input security group to have the new cidr, this could be a problem instead we can rely on the stream key to authenticate the user. Allow RTMP/RTMPS traffic from any IP (0.0.0.0/0).

Define a unique stream name (e.g., secret-stream-key-123) as part of the RTMP URL

The stream key (secret-stream-key-123) acts as the authentication token.
Use rtmps:// (RTMP over SSL/TLS) to encrypt the connection and protect the key.

Security Best Practices
Rotate Keys: Periodically update the stream key.
Restrict Access: Use AWS IAM policies to limit who can view/update the MediaLive input.
Monitor: Use CloudWatch to detect unauthorized access attempts.



