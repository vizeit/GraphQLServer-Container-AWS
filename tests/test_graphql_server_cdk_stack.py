import aws_cdk as core
import aws_cdk.assertions as assertions

from GraphQLServerCDK.graphql_server_cdk_stack import GraphQlServerContainerAwsStack

app = core.App()
stack = GraphQlServerContainerAwsStack(app, "graph-ql-server-container-aws")
template = assertions.Template.from_stack(stack)

def test_vpc():
    
    template.resource_count_is("AWS::EC2::VPC", 1)

    template.has_resource_properties("AWS::EC2::VPC", {
        "EnableDnsSupport": True,
        "EnableDnsHostnames": True
        })

def test_cluster():
    template.resource_count_is("AWS::ECS::Cluster", 1)

def test_autoscalinggroup():
    template.resource_count_is("AWS::AutoScaling::LaunchConfiguration", 1)
    template.resource_count_is("AWS::AutoScaling::AutoScalingGroup", 1)

    template.has_resource_properties("AWS::AutoScaling::LaunchConfiguration", {
        "InstanceType": "t2.micro"
    })

def test_ecsfargate():
    template.resource_count_is("AWS::ECS::Service", 1)

    template.has_resource_properties("AWS::ECS::Service", {
        "LaunchType": "FARGATE"
    })