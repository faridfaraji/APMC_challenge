provider "aws" {
  region = "us-west-2"
}

resource "aws_medialive_input_security_group" "example" {
  whitelist_rules {
    cidr = "203.0.113.0/24" # Replace with your encoder's IP range
  }
}

resource "aws_medialive_input" "rtmp_input" {
  name = "MyRTMPInput"
  type = "RTMP_PUSH"

  input_security_group_ids = [
    aws_medialive_input_security_group.example.id,
  ]

  destinations {
    stream_name = "MyRTMPInput-stream"
  }
}
