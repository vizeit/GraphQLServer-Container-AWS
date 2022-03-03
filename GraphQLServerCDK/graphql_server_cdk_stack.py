from aws_cdk import (
    Stack,
    aws_autoscaling as autoscaling,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecspatterns,
    CfnOutput
)
from constructs import Construct

class GraphQlServerContainerAwsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #prefix for name of all resources
        nameprefix = "GraphQLContainer"
        
        #create VPC
        vpc = ec2.Vpc(
                    self, 
                    nameprefix + "VPC",
                    max_azs=2)
        
        #create cluster
        cluster = ecs.Cluster(
                    self,
                    nameprefix + "Cluster",
                    vpc=vpc)

        #create autoscaling group
        asg = autoscaling.AutoScalingGroup(
                    self,
                    nameprefix + "ASG",
                    instance_type=ec2.InstanceType("t2.micro"),
                    machine_image=ecs.EcsOptimizedImage.amazon_linux2(),
                    vpc=vpc)
        
        capacityprovider = ecs.AsgCapacityProvider(
                    self,
                    nameprefix + "ASGCP",
                    auto_scaling_group=asg)

        cluster.add_asg_capacity_provider(capacityprovider)

        #create ecs fargate from local image
        ecsfargateservice = ecspatterns.NetworkLoadBalancedFargateService(
                    self,
                    nameprefix + "FargateService",
                    cluster=cluster,
                    task_image_options={
                        'image':ecs.ContainerImage.from_asset('./GraphQLAPI')
                    })
        
        ecsfargateservice.service.connections.security_groups[0].add_ingress_rule(
                    peer=ec2.Peer.ipv4(vpc.vpc_cidr_block),
                    connection=ec2.Port.tcp(80),
                    description="Allow HTTP inbound from VPC"
        )

        #output load balancer DNS
        CfnOutput(self, nameprefix + "LoadBalancerDNS", value=ecsfargateservice.load_balancer.load_balancer_dns_name)
