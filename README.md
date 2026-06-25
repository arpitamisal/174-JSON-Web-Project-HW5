Arpita Misal 
174 HW5

EC2 URL:
http://107.23.66.62:8000/


Endpoints:

GET /companies  
Returns all trucking companies  

curl http://107.23.66.62:8000/companies  


GET /companies/<name>  
Returns a specific company  

curl http://107.23.66.62:8000/companies/UPS  

POST /companies  
Adds a new company  

curl -X POST http://107.23.66.62:8000/companies \
-H "Content-Type: application/json" \
-d '{"Company":"TestCo",...}'

PUT /companies/<name>  
Updates a company  

curl -X PUT http://107.23.66.62:8000/companies/TestCo \
-H "Content-Type: application/json" \
-d '{"Revenue":"$2000"}'

DELETE /companies/<name>  
Deletes a company  

curl -X DELETE http://107.23.66.62:8000/companies/TestCo


Terminal outputs: 

arpitamisal@Arpitas-MacBook-Air-2 Desktop % curl -X POST http://107.23.66.62:8000/companies \
-H "Content-Type: application/json" \
-d '{"Company":"TestCo","Services":"Shipping","Hubs":{"Hub":["San Jose","Austin"]},"Revenue":"$1000","HomePage":"http://testco.com","Logo":"test.png"}'
{"company":{"Company":"TestCo","HomePage":"http://testco.com","Hubs":{"Hub":["San Jose","Austin"]},"Logo":"test.png","Revenue":"$1000","Services":"Shipping"},"message":"Company added successfully"}
arpitamisal@Arpitas-MacBook-Air-2 Desktop % curl http://107.23.66.62:8000/companies/TestCo
{"Company":"TestCo","HomePage":"http://testco.com","Hubs":{"Hub":["San Jose","Austin"]},"Logo":"test.png","Revenue":"$1000","Services":"Shipping"}



arpitamisal@Arpitas-MacBook-Air-2 Desktop % curl -X PUT http://107.23.66.62:8000/companies/TestCo \
-H "Content-Type: application/json" \
-d '{"Revenue":"$2000"}'
{"company":{"Company":"TestCo","HomePage":"http://testco.com","Hubs":{"Hub":["San Jose","Austin"]},"Logo":"test.png","Revenue":"$2000","Services":"Shipping"},"message":"Company updated successfully"}



arpitamisal@Arpitas-MacBook-Air-2 Desktop % curl -X DELETE http://107.23.66.62:8000/companies/TestCo
{"company":{"Company":"TestCo","HomePage":"http://testco.com","Hubs":{"Hub":["San Jose","Austin"]},"Logo":"test.png","Revenue":"$2000","Services":"Shipping"},"message":"Company deleted successfully"}



arpitamisal@Arpitas-MacBook-Air-2 Desktop % curl http://107.23.66.62:8000/companies/TestCo
{"error":"Company not found"}



