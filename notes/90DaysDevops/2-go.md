# Day 2

Today I will be setting up my environment and learning some GO. This was quite easy since I have already done a class where we had to use GO.

go is a compiled language that gets turned into an EXE

## what are packages

a collection of source files in the same directory that are compiled together. To simplify, it is just a bunch of go files in the same directory.

We use packages to reuse other code.

## the go workspace

you got 3 folders, source, bin and pkg.

src is where all the writte code lives
the pkg has the packages that you install, and
bin is where the comiled files live.

**compiling and running code**
we can compile by runnig these commands

    go build
    go install
    go run

-   go run - This command compiles and runs the main package comprised of the .go files specified on the command line. The command is compiled to a temporary folder.
-   go build - To compile packages and dependencies, compile the package in the current directory. If Go project contains a main package, it will create and place the executable in the current directory if not then it will put the executable in the pkg folder, and that can be imported and used by other Go programs. go build also enables you to build an executable file for any Go Supported OS platform.
    go install - The same as go build but will place the executable in the bin folder.

## learn go in 12 minutes

a go project is different becuse it always lives in your workspace, which is the go folder in your home directory

in the src folder in that worksplace you can make sub folders for your projects

The root file is often called main.go but it can be anything.

to import, you type import() and put the things in the brackets, like
import ("fmt")

use func to define a function. like func main() {}

to make a variable you do it like this: var name type. so var x int

you can assign at the same time like this: var x int = 7

A better way is to infer it. x := 7 type is auto determined

var := [5]int{1,2,3,4,5} defines the array
slices are an abstraction over array and does not have a set length.
you make one by not defining the length

you can use appent
a = append(a, 13)

map is a dictionary. mam[keyType]valueType

so verticies := make(map[string]int)

fmt.PrintLn to print
delete to delete

Only loop type is for loop.
for i := 0; i<5; i++ {

}

and for a while loop:
for i<5{

}

to iterate over array:
for index, value ;+ range arr{

}
you can do the same for key and value in a dict.

to make another function
func name(param type, param2 type2) returnType{

}

go function can have multiple return types, so we can return (foal64, error) to return an error if it fails.

you can then return result, nil if no error, and nil, error if error.

Go has no exceptions

type myTpe struct{
item type
item2 type2

}

Pointers
if we do
i := 7
print(&i) prints the memory address to it

a funciton can take a pointer like this. we need to dereerence it

func inc(x *int){
*x++ //this dereferences and actually increments the value
}
