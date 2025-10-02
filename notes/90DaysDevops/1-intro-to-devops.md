Day 1-7

## What is devops?

they don't actually make the app, but you should have a good understanding of the cocepts of how a dev works the systems.

At a high level, ou are going to know how the app is configured to talk to all its required services

Devops guy is responsible for the deployment. The app needs to run somewhere, on prem, cloud, serverless,, etc. the devops guy configures these servers and gets them ready for the app.

We will need some networking knowledge too.

## Devops Life cycle

there will be things like CD, testing, deploymnet, monitor, etc that will be brought up. This time we are taking a look at the high level view of the app form start to finish and back around again

**Development**
This part is self explanatory, the dev does it

**Testing**
At this stage, we need to make sure to test our code in all different environments that we have avaiable

This phase enables QA to test bugs, more frequently we see containers being used for simulating the test environment

This phase is likely automated as part of the next part which is integration

**integration**
With every commit, your app goes through automated testing phases and allows for early detection of issues.

**Deployment**
this stage wis where we deploy code on production servers.

Different app requires different hardware or configs, so application configuration management, and IaC could play a key part in the DevOps Lifecycle.

Your app might even be containerized an running on a vm, and orchestrated using kubernetes.

**monitoring**
we need to make sure the app is continuously being monitored.

reliability is a key factor here as well, at the end of the day we want our app to be available at all time. This then leads to other observability, security, data management areaas that should be continuously monitored.

## plan -> code -> build -> test -> release -> deploy -> operatae -> monitor

kind of self explanitory

Continuous Delivery: plan code build test
continuous integration: plan code build test release
continuous deploy: deploy operate monitor

## languages used for devops

Go is the next programming language for devops, and many tools and platforms for devopsa re written in GO, like docker kubernetes grafana and prometeus.

what makes GO so good?

Usually you want an interpreted language like pythong because of how fast it is to run, but go is compiled. However it is known for fast compilation.

GO programs are statically linked, meaning that when you compile a go program everything is included in a single binary executable. No external dependencies will be required.

This makes deployment of GO programs super easy comapred to python with external libraries when being ran.

Go is platform independent meaning that it will work on all machine. GO is also a lot faster than python and has a powerful large standard library.

Tomorrow (or tonight) will be setting up the environment and learning some actual GO skills
