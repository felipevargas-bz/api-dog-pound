# guane-intern-fastapi

<h3 align="center">Social media</h3>

<p align="center">
&nbsp; <a href="https://twitter.com/felipevargas_bz" target="_blank" rel="noopener noreferrer"><img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/twitter.svg" width="30" /></a>
&nbsp; <a href="https://www.facebook.com/profile.php?id=100028222452093" target="_blank" rel="noopener noreferrer"><img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/facebook.svg" width="30" /></a>
&nbsp; <a href="https://www.youtube.com/channel/UCFrPLo_zV_OYjL5WFtGrN3A" target="_blank" rel="noopener noreferrer"><img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/youtube.svg" width="30" /></a>
&nbsp; <a href="https://www.linkedin.com/in/felipevargas-bz/" target="_blank" rel="noopener noreferrer"><img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/linkedin.svg" width="30" /></a>
&nbsp; <a href="mailto:felipevargas.bz@gmail.com" target="_blank" rel="noopener noreferrer"><img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/gmail.svg"  width="30" /></a>
&nbsp; <a href="https://devfelipevargas.medium.com/" target="_blank" rel="noopener noreferrer"><img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/medium.svg" width="30" /></a>
</p>

<!-- Table of contents -->
<details open = "open">
  <summary> Content table </summary>
  <ol>
    <li>
      <a href="#about-the-project"> About the project </a>
      <ul>
        <li> <a href="#built-with"> Built with </a> </li>
      </ul>
    </li>
      <ul>
        <li> <a href="#prerequisite"> Requirements </a> </li>
        <li> <a href="#steps-to-test-at-your-local"> Steps to test it at your local </a> </li>
      </ul>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About the project
This project is an api, thought to handle two entities, Dog and User, this project is made for the FastApi web framework.
This project consists of the following Endpoints:

### Endpoints for the Dog entity:

|          Dog          |
|+ id: integer          |
|+ name: String         |
|+ picture: String      |
|+ is_adopted: Boolean  |
|+ create_date: Datetime|

* GET - "/api/dogs" > get a list of all dogs saved in the database.
* GET - "/api/dogs/is_adopted" > get a list of all dogs whose is_adopted attribute is set to True.
* GET - "/api/dogs/{name}" > Get a dog saved in the database by name.

* POST - "/api/dogs/{name}" > store a dog in the database created by name.

* PUT - "/api/dogs/{name}" > update a dog saved in the database by name.

* DELETE - "/api/dogs/{name}" > delete a dog saved in the database by name.

### Endpoints for the User entity:

|User                   |
|+ id: integer          |
|+ name: String         |
|+ last_name: String    |
|+ email: String        |
|+ update_date: String  |
|+ create_date: String  |

* GET - "/api/users" > get a list of all users stored in the database.
* GET - "/ api / users /{user_email}" > get a user stored in the database by email.
* GET - "/api/users/dogs/{user_email}" > get all the dogs associated with a user, these dogs are related by the user's id and are obtained through a query to the database, all the buts whose ib_user attribute is equal to the user whose email we have.

* POST - "/api/users/{user_email}" > create a user and store it in the database by email.

* PUT - "/api/users/{user_email}" > update a user stored in the database through his email.

* DELETE - "/api/users/{user_email}" > delete a user stored in the database.

If a user is deleted, all the dogs associated with that user are also deleted from the database, this in order not to have loose entities without meaning in the database.

### Built with
The api was built with:

* [Python](https://www.python.org/) > [FastApi](https://fastapi.tiangolo.com/)
* [MySQL](https://www.mysql.com/)
* [Docker](https://www.docker.com/)


### Prerequisite
Have docker and docker-compose installed

### Steps to try it in your local

First, clone the repository: ``` git clone https://github.com/felipevargas-bz/guane-intern-fastapi.git ```

Then we proceed to build our images
 ``` cd  guane-intern-fastapi```
 ``` sudo docker-compose build ```

Once the images are built, we start running our containers
``` sudo docker-compose up -d ```

In order to see if all the containers were mounted correctly, we proceed as follows:
``` docker ps -a ```

| Name           | Command                                      |  State                 | Ports                                                 |
| :---           |     :---:                                    |          -----         |:---                                                   |
| backpython     |  python3 /test_guane/api/main.py             | up                     |  0.0.0.0:8000->8000/tcp, :::8000->8000/tcp            |
| mysql          |  docker-entrypoint.sh mysql                  | up                     |  0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp |
