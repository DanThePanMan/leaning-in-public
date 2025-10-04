## go part 2

we use fmt.scan to get the user input
<br>

what is a **pointer?**
<br>
a pointer is a special variable that points to the memory address of another variable. You can use them to store some data at a particular memory address of the system. It is always in hexadecimal starting with 0x, so like 0xFFAAF

<br>
what is the need for it?
to understand this we need to first understand variables. Variables are names given to a memory location where the actual data is stored. To access stored tat awe need the address of that particular memory location.

It is difficult to remember all the memory addresses manually so we use variables to store data and variables can be access by just their names.

Go also allows saving a hexadecimal number into a variable using a literal expression (starts with 0x)

when you make a pointer, you are storing the memory address in another variable

# skipping to some quick linux related notes

rmdir removes the directory. Only work if nothing is in the folder

mv moves files but it can also be used to rename folders
rm -R is recursive and um -R -f forces removal.

cp copies

cat is used to concatenate. we can do cat fileName to see the contents inside the file.

grep is used to search for a specific word:
cat file | grep "keyword"

history shows history and history -c clears it

leearn about permissions. or look it up when needed

# vagrant

CLI util that manages the lifecycle of your vm. You can use this to spin up or down a vm across many different platforms.

we are pairing this with virtualbox

## our first vagrantfile

the VAGRANTFILE describes the type of macine we want to deploy. It also defines the config and provisioning for this machine

The person saves them in their workspace.

```
Vagrant.configure("2") do |config|

  config.vm.box = "chenhan/ubuntu-desktop-20.04"

  config.vm.provider :virtualbox do |v|

   v.memory  = 8096

   v.cpus    = 4

   v.customize ["modifyvm", :id, "--vram", "128"]

end

end
```

this is a simple VAGRANTFILE that says

-   we want a specific box, being possible either a public image or private build of the system that you are looking for
-   next like says we want to use a specific provider (virtualbox)
-   we also deifne the machine's memory to be 8gb with 4 cpus.

now that we are ready, we can cd into where the VAGRANTFILE is, and then type `vagrant up`

another thing to add is that the network will be set to NAT ont he viratual machine.

once `vagrant up` is done, we can now use vagrant ssh to jump into the terminal of our new vm

oh btw the username is vagrant and the password is vagrant

# SSH and web servers

This aprt mostly talk about 3 things:

-   setting up a connection with SSH
-   transferring files
-   create your private key

SSH: provides a secure tunnel between client and server. We can connect as a clinet with connect credentials or SSh key.

lets say we have a vm as the ssh serer and we are going into it from windows:

-   on the vm, run sudo apt install OpenSSH-server

0. sudo systemctl enable ssh
   sudo systemctl start ssh

    verify: sudo systemctl status ssh

now that the SSH server is listening on port 22 for any inocming connection request and we have added the bridged networking we could use putty or an ssh client to connect to the system using ssh

https://github.com/MichaelCade/90DaysOfDevOps/blob/main/2022/Days/day18.md this link has pics but follow step by step

1. click open and then enter the username and password (both vagrant) (if it is a vagrant vm)

2. at this stage we are connected to our vm from our remote client and we can issue our commands on the system

3. use `ip addr show` to get the ip

4. and then do ssh dan@ip to get in, the ip is the one under inet and is like 10.10.x.x

---

going to recap the steps here with the non vagrant machine, will be diff with vagrant obviously

1. start it up

```
sudo systemctl enable ssh
sudo systemctl start ssh
```

2. `ip addr show` and get the one under inet.

3. ssh dan@ip to get in

## ssh key

SSH keys means that we provide a key pair so boht the client and the server know that this is a trusted device

creatinga key is easy,k we can do this ssh-keygen -t ed25519
then there will be a key stoerd in our .ssh folder under users/dan

to link this with our linux VM we need to copy the key. We can do this by using the ssh-copy-id vagrant@192.168.169.135. note that this does not work on powershell.
After setting it up, you will notice that you no longer need a password.
ssh vagrant@192.168.169.135 straight up connectts us to it

we coudl secure thi further by ussing a passphrase, this is all under the etc/ssh/sshd_config file
