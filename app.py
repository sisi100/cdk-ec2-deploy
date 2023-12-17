import aws_cdk as cdk

app = cdk.App()
stack = cdk.Stack(app, "cdk-ec2-deploy-stack")

VPC_CIDR = "10.111.0.0/16"
vpc = cdk.aws_ec2.Vpc(
    stack,
    "VPC",
    cidr=VPC_CIDR,
    max_azs=1,
)
# デフォルトではnatgatewayが作られてkコストがかかる。

app.synth()
