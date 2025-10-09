# network automation

### basics

why?

-   Elminate errors
-   reduce costs
-   achieve agility
-   ensure compliance
-   centralized management
    It is specifc for each business, there is no one size fits all. Focus is always on providing business value and end-user experience.

<br>
to break the down, you need to identify what exactly ou need to automate to improve end user experience. or business value benefits

define clear goals and do it in a step-by-step approach.

<br>
build concepts based on existing applications, theres no need to design the concepts round automation in a bubble because they need to be applied to your app, infra, etc.

so begin to build the concepts and model around your specific use case.

### approach to networking applicaiton

We should identify the tasks and make a discovery of network change requests so that you have the most common isseus and problems to automate a solution to.

-   make a list of things you do manually
-   determine the most common, time consuming and error prone activities
-   prioritize the requests by making a business driven approach.
-   This is the framework for building an automation process, what must be autoomated and what must not

we divide the tasks and analyze how different functions interact with each toerh. Here are some categories:

-   App optimization
-   app delivery controller
-   firewall
-   DDI (DNS, DHCP, IPAM)
-   Routing
-   Others

Identify various dependencies to add to address vusiness and cultural differences and bring in cross team collaboration

### stack

linux, ansible for config management, ansible tower, jenkins for CI/CD, git/github, python? for scripts, postman for api analyzation
