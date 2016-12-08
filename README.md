# Term_Project
Hunter, Kiley and Frankie

Implementation Instructions
*Our directory contains a static folder, a templates folder, a contacts.csv file and a main.py file.  
All contents in the static file are things that do not change, such as styling sheets or images. 
The templates folder contains our HTML files for our site pages. The main.py file is our Flask app and the contacts.csv file
is the storage point for user contact information. 

*Once you download all of these folders and files into the same directory,
you need to open the command prompt window and type: "python main.py" to start the development server (this is because our code
is not hosted on the public internet so your computer must act as its own server). 

*Type "localhost:8888" into your browser window to display the page.  
Once the page is displayed, you now know the site is functioning properly and is ready for use.

*Behind the scenes there are quite a few things going on with our code. We used Javascript on the contact_us.htm file to parse the form. 
Then we created a Flask endpoint which takes the variables into the URL. The endpoint method then opens a contacts.csv file
and appends the value we get to it. 
*We added ID's to all of the form elements and checked everything with Javascript. 
*We used jQuery/AJAX to submit a post request to our Flask server. AJAX is preferred over a form 'action' because
the issue with 'action' is that it tries to redirect the browser to an action URL.  
*We put in an alert dialogue when the post request returns so that the user knows the data is saved. 
