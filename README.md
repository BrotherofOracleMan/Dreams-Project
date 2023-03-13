# Dreams Website
Project for me to learn new technologies on my free time.

## First Prototype
Backend: Django , Scrapy
FrontEnd: Vue.js
Other technologies: Kubernetes, Docker , NoSql DataBase or MongoDB
Reference: https://alioguzhan.medium.com/how-to-use-scrapy-with-django-application-c16fabd0e62e

### ToDo List for Backend
- [X] Create a spider that writes data to a database.
- [ ] Design the Django REST API that fetches the data from DataBase
- [ ] Make sure the Django View triggers the crawl through a websocket
- [ ] Implement different kind of searches with the database based on dates and word
- [ ] Implement creating a dream and inserting the dream.

### Todo List for Front End:
- [ ]  Create a landing page displaying number of dreams and searchbar with criteria
- [ ]  Create a navigation bar to get back to landing page
- [ ]  Create a page for creating a dream

### Todo List for Testing/Automation
- [ ] Create frontend and backend tests
- [ ] Dockerize the Application 
- [ ] Deploy to Kubernets
- [ ] Implement Jenkins CI/CD

### Sequence Diagram
![diagram drawio](https://user-images.githubusercontent.com/16285362/220694725-2305b60d-89a5-4067-bc3e-b033318c8626.png)

-TodoList

### REST API

* Make sure all REST APIs return JSON through serialization(major)
* Make sure all REST APIs have graceful error handling (major)
* Make sure all REST APIs have some sort of user authentication (todo for later, not in production application)

GET APIS
* HTTP GET /v1/id/{id}
* HTTP GET /v1/quote/contain_string
* HTTP GET /v1/before_date/{date}
* HTTP GET /v1/after_date/{date}

POST
* HTTP POST /v1/new_entry (data will be defined in the content body)

DELETE
* HTTP POST /v1/delete_entry (data will be defined in the content body)



