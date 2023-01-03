# HighAvailabilty_AWS_Deployment

A Highly Available Web Application Deployed on Amazon Web Services via Cloudformation ( IAC ).

Below is the Diagram of the Architecture we are deploying on AWS


![AWS Highly Available Web APP (1)](https://user-images.githubusercontent.com/48082346/210223535-72338653-ee11-4415-97fe-d61a0c94ad94.png)


Strategies to Provision this Architecture
1) We will be keeping in mind all the main Principles of IAC -> Reproducibility, Idempotency , Composability and 
Evolution
2) This Code can be taken as it will Produce the exact output as we are stating( Reproducibility).
3) You will be able to swap, and add more resources (Composability)
4) There are Variables use to Evolution can be done effortlessly ( Evolution )
5) Idempotency at the moment we are not so sure as it requires conditional checks when adding new resources. But will are 
looking into it.  


Points to Remember
1) We are deploying Architecture for Web App ( There is no Application on the Web Server yet) 
2) We are using 100% Cloudformation for this Deployment
3) In the future we will update the Shell Scripts to create, update the stack to Python to do a little more advanced stuff
