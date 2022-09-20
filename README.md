# Book Catalog - Django Web Application
To search any ISBN using google API and display + save the book details. 

Project description

1. A Django project from base to create a book catalog interface.
2. Starting with a login page for logging in authorized users and to maintain their book details.
3. Post login - A search box for searching books based on their ISBN (International Standard Book Number).
4. Internally fetching the book details from Google API (book title, author name, page count, avg rating).
5. A book details page displaying the API results.
6. An error screen in case no results found for the searched ISBN.
7. Save the displayed data into database, for future retrieval.

Run below commands to execute the appplication after checkout (This will auto-start the server) -
1. cd </path/to/project>
2. python3 app.py
3. You will need to create a dummy user for the first time - to access through login page
4. Then, open a browser and enter - https://localhost:8000/accounts/login


Login Page Access Details - 
userid/password - <DUMMY username/password provided during setup earlier>
