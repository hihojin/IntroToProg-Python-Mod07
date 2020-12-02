# **Title: ** **Assignment07.Py with Pickling and Error Handling**

**Dev:** *Hyojin* **Date:** *12.1.2020*

## Introduction
This week, we learned about error handling such as ‘try-except’ and another terminology: pickling, which is a technique to save as a binary file. Assignment07.py is a new script that is organized with Processor class and its functions, asking user about their grocery items and costs which are ultimately saved in the dictionary lists of a table. Below paragraphs will show a step-by-step information of how I wrote codes to create the script.

## Creating the Script
Prior to code any further I imported a module called ‘pickle’. Pickle module has two main built-in codes: dump and load. Dump makes it able to dump the data into an indicated file and load can read one row of data from the binary file to human language. I set strFileName as equal to grocery_data.dat so the file is saved as binary file. 

To successfully operate option 1: Adding a new item I used IO.asking_add_data() and Processor.adding_data(item, cost, lstitems). IO.asking_add_data() has two input functions where it enables users to input the name of items and costs of each item and return the saved values in ‘item’ and ‘cost’. When these two input functions are executed, Processor.adding_data(item, cost, lstitems) saves value of item and value of cost into one dictionary and those values are going to be appende into a table called list_of_ data, or lstitems later in the main body of codes. 

Option 2 requires one exception class: ‘try-except’ as read option both for text file and binary file gets an error when there is no existing file. When I add except exception or more specifically, AttirbuteError: pass it passes the function and moves on to the next codes in operation. 

The above code will run Processor.save_data_to_file() when user puts ‘y’ and print ‘Saved!’ while it prints the exception ‘Your data is not saved’ when it fails to save data into the binary file.

Option 3 is about showing the current data to the user by unpickling data in binary file back to the human language again. 

The last option, option 4 is asking user to exit out of the program. When user press the enter key the program will finish. 

## Getting Output
Results are successfully added, saved to the binary file, reloaded from the file to the user and finally exit from the program. The grocery script runs smoothly and is a simple script to acquire users’ grocery items and costs. It will be more beneficial for user if total cost calculation would be added to the menu of options. 

## Summary
It was fun to create a new script of my own this week. I learned using exception classes in programming is very useful whenever facing error messages. Specified exception class gives even clearer vision to a developer to fix the bug. I am excited to learn more about import function this week of lesson.  
