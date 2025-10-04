# Bash scripting

-   the first line of the bash script would hbe the path to your bash binary.
    for me this is #!/usr/bin/bash
-   you can add comments with the #
-   then just type in the commands that you want to execute line by line

when you try to run it it would say that the access is denied

-   you can check the permission of the file using the `ls -al` command
-   to update this, type in chmod +x myFile to make it executable

## variables in bash

to add a variable, add it like how we do in python: so `days = 90`

we can also use echo to print something. and in order to print a variable, we can include the $ just like our template literals
`Hi, this challenge is $days days long`

you can also read user input using the read keyword

```
echo "Enter your name"
read name
```

to take parameters, just use $1 $2 $3 etc.

## conditionals

```
if [condition]
then
   asdfasdfasdf
elif [condition]
then
   asdfasdfasdf
else
  asdfasdf
fi
```

the condition can be like `$days -eq 90` which means days == 90.

here are the options: eq(equal), ne(not equal), gt(greater), ge(>=), lt(<), le(<=)

there are also other file conditionals
-d file: true if it is a directory
-e file: true if exists
-f file: true if provided string is a file
-g true if group id is set on a file
-r true if file is readable
-s true if it is no zero

# configs

## dot files

these dotfiels are configuration files for your linux system and applications. they all start with a `.`

so far we have been using bash for our shell with things like bashrc and bash_profile.

## zsh

zsh has some benefits over bash. It has features like tab completion, automated file search, regex, shorthand, and a good theme engine

We can use our apt package manageer to install zsh.

didn't do it yet will do next time
