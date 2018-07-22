# A Basic Flask Website

This is a basic Flask app that resembles the functionality of EasyBib/Citation Machine. 

# Instructions

To use the code in this folder you need to do a few things first.

## Step Zero
I'll give a brief overview here, then go into detail.

1) Make sure your're in the folder **/citation_machine**.
2) Create a virtual enviroment and activate it.
3) Install the **requirements.txt** file.
4) Now you can run the program.

## Step 1
Make sure your terminal is open to the folder **/citation_machine**. Use the command **cd** to change into it on the command line. 
```
$ cd citation_machine
```

## Step 2

Inside the folder **/citation_machine** create a virtual enviroment. Make sure you are using Python 3.5 or above.
```
$ python3 -m venv venv
```
This creates a folder called **venv** which we will now activate. Windows and Unix based machines are a little different.

### Mac/Linux
```
$ source venv/bin/activate
```
### Windows
```
> venv\Scripts\activate
```

Your terminal should have the name of the virtual enviroment in parentheses:
```
(venv) $ 
```

## Install the **requirements.txt** file.
In terminal type:
```
(venv) $ pip install -r requirements.txt
```
The **-r** stands for recursive and is a flag to tell pip we want to install everything in the file.

All of the packages that this python program has should now be available to it inside of the virtual enviroment. 

**This means you must activate the virtual enviroment every time you want to run this program.**

## Run the program.
You should be able to run the program by typing:
```
(venv) $ flask run
```

### You can now vist the website in your browser at the address [localhost:5000](localhost:5000).