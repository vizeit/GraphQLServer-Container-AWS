
# GraphQL Server - Container - AWS

Boilerplate [Serverless](https://en.wikipedia.org/wiki/Serverless_computing) [Container](https://opencontainers.org/) implementation of [GraphQL](https://graphql.org/) server in [Python](https://www.python.org/) using [AWS ECS](https://aws.amazon.com/ecs/) and [AWS Fargate](https://aws.amazon.com/fargate/) 

## Features
- Containerized
- Infrastructure as code
- Schema-first approach
- Implemented in Python
- Serverless
- Hosting on AWS
- Modular
- Test-driven Development

## Quickstart
### Prerequisites
- Active [AWS](https://aws.amazon.com/) account
- Local development environment setup for [AWS](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html), [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) and [Docker](https://www.docker.com/get-started)

### Steps
1. Clone the repo,

```
git clone https://github.com/vizeit/GraphQLServer-Container-AWS.git
```

2. Create a virtual environment

```
$ python3 -m venv .venv
```

3. After the init process completes and the virtual environement is created, you can use the following
step to activate it

```
$ source .venv/bin/activate
```

4. Once the virtual environment is activated, you can install the required dependencies

```
$ pip install -r requirements.txt -r ./GraphQLAPI/requirements.txt
```

5. Run unit tests for GraphQL API and AWS CDK

```
pytest
```

6. At this point you can synthesize the CloudFormation template for this code.

```
$ cdk synth
```

7. After successful synthesize, bootstrap the stack

```
cdk bootstrap
```

8. Deploy the stack to your AWS account

```
cdk deploy
```

9. Once the deployment is complete, copy *LoadBalancerDNS* and launch it in a browser to load GraphQL playground