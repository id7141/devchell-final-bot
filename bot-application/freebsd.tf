provider "aws" {
  region = "eu-central-1"
}

resource "aws_security_group" "target" {
  name        = "target-security-group"
  description = "Allow HTTP, HTTPS and SSH traffic"

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTPS"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Terraform   = "true"
    Environment = "devchellange"
    Name        = "ex-machine freebsd"
  }
}


module "ex_machine" {
  source  = "terraform-aws-modules/ec2-instance/aws"
  version = "~> 3.0"

  name                   = "freebsd-target-vm"
  ami                    = "ami-06989cbd6b4926b18"
  instance_type          = "t2.micro"
  key_name               = "dev7141"
  vpc_security_group_ids = ["sg-001b41aaf078d6833"]
  subnet_id              = "subnet-0dca065db86fb9ef7"

  tags = {
    Terraform   = "true"
    Environment = "devchellange"
    Name        = "ex-machine freebsd"
  }
}
