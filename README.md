# Stuff
Ruquied packages:
Flask==1.1.1
Flask-RESTful==0.3.8
requests
json

Guide how to use API:
go in postman or direct from browser:

http://127.0.0.1:8000/api/getCovidCase?country=India

ouput:
{
  "Active Cases": "2,720,685", 
  "Country Name": "India", 
  "Percentage of Population Infected ": 1.704492346322528, 
  "Recovery Rate": 88.69473136420007, 
  "Total Cases": "26,752,447", 
  "Total Death": "303,751 "
}

Queryparames:
key : courtry 
value: coutryname(USA, India,etc)



included:
question2.py
Given a array of integers A of size N and an integer B.
Return number of non-empty subsequences of A of size B having sum <= 1000.



