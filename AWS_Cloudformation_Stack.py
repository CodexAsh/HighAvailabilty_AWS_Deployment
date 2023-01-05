import os
import subprocess
import sys

if len(sys.argv) != 4:

    print("This Script takes 3 Command line arguments. \
        1) Stack name \
            2) Main Infrastructure (yml) \
            3) Parameters file (yml)")

    print("Example -> python3 AWS_Cloudfromation_Stack.py Devops Main.yml Parameters.yml")
    print("Arguments supplied are not approicate. Please check")
else:
    error_string = "\nAn error occurred (ValidationError) when calling the DescribeStacks operation: Stack with id " + \
        sys.argv[1] + " does not exist"

    # Checking if the Stack exist

    checks = subprocess.getoutput(
        "aws cloudformation describe-stacks --stack-name " + sys.argv[1])

    if checks == error_string:
        print("We did not find any stack with that name. Creating Stack...")
        os.system("aws cloudformation create-stack --stack-name " +
                  sys.argv[1] + " --template-body file://"+sys.argv[2] + " --parameters file://"+sys.argv[3] + " --region=ap-south-1")
    else:
        print("We found the stack with that name. Updating Stack...")
        os.system("aws cloudformation update-stack --stack-name " +
                  sys.argv[1] + " --template-body file://"+sys.argv[2] + " --parameters file://"+sys.argv[3] + " --region=ap-south-1")
