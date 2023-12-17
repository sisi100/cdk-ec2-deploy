import aws_cdk as cdk

app = cdk.App()
stack = cdk.Stack(app, "cdk-ec2-deploy-stack")

VPC_CIDR = "10.111.0.0/16"

vpc = cdk.aws_ec2.Vpc(
    stack,
    "VPC",
    cidr=VPC_CIDR,
    max_azs=1,
    subnet_configuration=[
        cdk.aws_ec2.SubnetConfiguration(
            name="Private",
            cidr_mask=24,
            subnet_type=cdk.aws_ec2.SubnetType.PUBLIC,
        )
    ],
)


app.synth()
