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


<img width="774" height="56" alt="Screenshot 2026-04-24 at 8 51 10 PM" src="https://github.com/user-attachments/assets/ea29677c-eded-42cd-9ed4-a69f9eb51cfb" />
<img width="1470" height="60" alt="Screenshot 2026-04-24 at 8 50 58 PM" src="https://github.com/user-attachments/assets/18d97bc8-55b5-4a5c-a3fa-e000174f6551" />
<img width="1469" height="63" alt="Screenshot 2026-04-24 at 8 50 44 PM" src="https://github.com/user-attachments/assets/383e0979-ebb6-41cc-a96f-51feebd42eb2" />
<img width="1469" height="33" alt="Screenshot 2026-04-24 at 8 50 20 PM" src="https://github.com/user-attachments/assets/d8a30a16-1dfa-4eb5-9174-89e1ba7476dc" />
<img width="1456" height="61" alt="Screenshot 2026-04-24 at 8 50 00 PM" src="https://github.com/user-attachments/assets/68464ef6-7820-43ee-8152-37d42b2c6ee4" />
<img width="927" height="445" alt="Screenshot 2026-04-24 at 8 47 30 PM" src="https://github.com/user-attachments/assets/7a4cd3fb-ba2d-4a42-9fe9-0a4cbac12142" />
<img width="923" height="880" alt="Screenshot 2026-04-24 at 8 47 23 PM" src="https://github.com/user-attachments/assets/e502e2e1-84a2-42bf-8b57-644e5c703341" />
<img width="927" height="464" alt="Screenshot 2026-04-24 at 8 47 12 PM" src="https://github.com/user-attachments/assets/afe9bb90-bbf8-4c90-8c55-8a5250a118d2" />


