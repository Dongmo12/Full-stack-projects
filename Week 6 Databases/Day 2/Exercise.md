Exercise 2 : Dvdrental Database
Setup
We will install a new sample database on our PostgreSQL servers.
Download this sample database file
There is a single file called dvdrental.tar inside the zip. Extract it to your Downloads directory.
Tip : If you are using Mac, after extracting the zip file you will get a folder called dvdrental
Go to pgAdmin4, and navigate to Databases on the left pane.
Right click > Create > Database…
Type in the name of the new database: dvdrental, and click Save. Wait a few moments.
Right click on dvdrental under Databases in the left pane.
Click Restore…
For PC users choose the format Custom or tar / For Mac Users, choose the format Directory
Next to Filename, you should see a button with 3 dots on it. Click the button.
10.For PC users: Find your file in the window / For Max users: Find your folder in the window.
(you may have to check Show hidden files and folders?), and click the Select button.
If you see any error messages, please save them and get assistance. If not, you should have a new database loaded into your server!
Here is a diagram of the tables in the server. Take a look at it and learn about the tables, their columns, and the relationships between the different tables.

# Instructions

We will use the newly installed dvdrental database.

1- Write a query to select all the columns from the table “customer” in the database named dvdrental.

Write a query to display the names (first_name, last_name) using an alias named “full_name”.

You want to know every date where one or several accounts were created. Write a query to select the dates of creation from the “customer” table, it shouldn’t have duplicates.

Write a query to get the details of all customers from the customer table in descending order by their first name.

Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.

Write a query to get the address, the district and the phone number from the customers living in the district Texas in the “address” table.

Write a query to retrieve the details of the movies with the id 15 and 150.

Pick your favorite movie. Write a query to see if the rental shop owns it. Write a query to get the film ID, the title, the description, the length and the rental rate from the film table for your movie title.

Didn’t find it ? Maybe you made a mistake in the name. Write a query to get the film ID, the title, the description, the length and the rental rate from the “film” table for all the movies starting with the two first letters of your movie.

You want to have a choice between ten propositions of movies and you want the cheapest ones. Write a query to find the 10th cheapest movies.

You are not satisfied with the results. Write a query to find the 10th next cheapest movies.
Bonus: Try to not use LIMIT.

Write a query to join the data of the customer table and the payment table. You want to get the amount and the date of every payment made by a customer, ordered by his id (from 1 to…).

You need to check your inventory. Write a query to get all the movies which are not in the inventory.

Write a query to find which city is in which country.

15.Bonus :You want to be assured of the performance of your sellers. Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff who sold them the dvd.

## Solution

1- Write a query to select all the columns from the table “customer” in the database named dvdrental.

select * from customer

2- Write a query to display the names (first_name, last_name) using an alias named “full_name”.

select ( first_name, last_name ) as full_name from customer

3- You want to know every date where one or several accounts were created. Write a query to select the dates of creation from the “customer” table, it shouldn’t have duplicates.

select distinct create_date from customer;

4- Write a query to get the details of all customers from the customer table in descending order by their first name.

select * from customer order by first_name desc

5- Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.

select film_id, title, description, release_year, rental_rate from film order by rental_rate asc

6- Write a query to get the address, the district and the phone number from the customers living in the district Texas in the “address” table.

select address, district, phone from address where district='Texas'

 