
![technologies](https://user-images.githubusercontent.com/105242658/170760172-851b4c32-a763-4506-aaa6-052683964ddc.png)


# ApiSentimentAnalysis

In this project you will create a **RESTful API** using some cool technologies like **Flask**, **Docker** or **MongoDB**. A RESTful API is basically an API which supports HTTP connections. The browser will be able to send HTTP request to the server that is going to be created. The server is going to open a few endpoints, which can receive some sentence and make the computation neccesary to classify its feelings (a value between 0 and 1, closer to one, the more positive is the feeling of the sentence). Finally, once the response is ready, it takes it back to the browser, displaying it for us in a JSON format.

It is better to understand it by watching the chart protocol for the API:

| Resources | URL| Method | Parameters | Status Code |
| ----- | ---- | ---- | ---- | ---- |
| Register a new user | /register | POST | user_name <br /> password | 200 ok <br /> 301 Invalid username
| Detect the feeling | /classify_feeling | POST | user_name <br /> password <br /> text | 200 ok <br /> 301 Invalid username <br /> 302 Invalid Password <br /> 303 Out of tokens | 
| Refill | /refill | POST | user_name  <br />  admin_pw <br /> refill | 200 ok <br /> 301 Invalid username <br /> 304 Invalid admin <br /> 305 Refill tokens |


## :gear: Setup
- We will be using Postman, Docker, Docker compose and MongoDB. If you don't have them installed in your PC, you could do it following the instructions:
  - Postman: https://www.bluematador.com/blog/postman-how-to-install-on-ubuntu-1604
  - Docker: https://docs.docker.com/engine/install/ubuntu/
  - Docker compose: https://docs.docker.com/compose/install/
  - MongoDB: https://websiteforstudents.com/how-to-install-mongodb-on-ubuntu-linux/
- Clone the repository: `https://github.com/cblancac/ApiSentimentAnalysis`.
- Download the English language model adding it to the folder web:
   `wget https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-2.3.1/en_core_web_lg-2.3.1.tar.gz`
- `sudo docker-compose build`
- `sudo docker-compose up`

## :tada: Let's try the API
Once the setup is done, we could try the API. Postman is needed for that, so you should type `postman` in your terminal. Now we have to register, then call to the endpoint `/register` is needed, sending a username and a password. 

![register](https://user-images.githubusercontent.com/105242658/170741691-bc91fb42-00d5-4d3f-bd6d-70d52d730557.png)

Now we will have an account and we could use the web server to measure the feeling of some sentences because our information as a user has been stored in MongoDB. We start having 10 tokens and we will spend 1 of them every time we use the API to predict the feeling of our sentence. Let's see the API in action when we send a POST request to classify the feeling of one text

![classify_feelings](https://user-images.githubusercontent.com/105242658/170743771-585cd156-17e7-4d88-af4c-c2f94b1f2562.png)

Once all the tokens are spended they can be refilled again. To do that, the admin password is needed (only the API owner knows it). In this case the endpoint needed is `/refill`, giving as an input:
- *user_name*: Username registered 
- *admin_pw*: Administrator password
- *refill*: How many tokens it has to be refilled to the user
