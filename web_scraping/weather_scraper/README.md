# Instructions

To use the code in this folder you need to do a few things first.

## Step Zero
I'll give a brief overview here, then go into detail.

1) Make sure your're in the folder **/weather_scraper**.
2) Create a virtual enviroment and activate it.
3) Install the **requirements.txt** file.
4) Now you can run the program.

## Step 1
Make sure your terminal is open to the folder **/weather_scraper**. Use the command **cd** to change into it on the command line. 
```
$ cd weather_scraper
```

## Step 2

Inside the folder **/weather_scraper** create a virtual enviroment. Make sure you are using Python 3.5 and above.
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
You should be able to run the program by just typing the name of the program into the console:
```
(venv) $ scraper.py
```
Or, you can use the word **python3** before it.
```
(venv) $ python3 scraper.py
```

### Your program should now be running!