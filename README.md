# HighAvailabilty_AWS_Deployment

A Highly Available Web Application Deployed on Amazon Web Services via Cloudformation ( IAC ).

Below is the Diagram of the Architecture we are deploying on AWS


![AWS Highly Available Web APP (1)](https://user-images.githubusercontent.com/48082346/210223535-72338653-ee11-4415-97fe-d61a0c94ad94.png)


Stragies to Provision this Architecture
1) We will be keeping in mind all the main Principles of IAC -> Reproducibility , Idempotency , Composability and 
Evolution
2) This Code can be taken as it will Produce the extact output as we are stating( Reprodcibilty).
3) You will be able to swap, add more resources (Compsobiltity)
4) There are Varibales use to Evoluton can be done effortlessely ( Evolution )
5) Idempotncy at the moement we are not so sure as it requires conditional checks when adding new reosurce. But will are 
looking into it.  

Points to Remember
1) We are deploying Architecture for Web App ( There is no Application on the Web Server yet) 
2) We are using 100% Cloudformation for this Deployment
3) In future we will update the Shell Scripts to create , update stack to Python to do little more advanced stuff

