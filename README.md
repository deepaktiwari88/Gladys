# Gladys

<p align="center">
  <img src="https://github.com/deepaktiwari88/Gladys/blob/master/about/static/about/hello.png" width="350"/>
</p>
Gladys is an online food ordering chatbot. It is designed to help restaurant and food providers reduce labour costs, reduce human errors and to improve overall customer service experience. The chatbot helps customers in choosing from various cuisines and restaurants and ordering their dishes from the menu of a picked restaurant, tracking the order and delivery. 

## Development Workflow

### Setup your database in MySQL (Linux Only)
1. Install MySQL in your machine if you haven't and switch to MySQL Administrative User to perform administrative tasks.
    ```
    mysql -u root
    ```
    
2. Create Database Gladys for the project.
    ```
    CREATE DATABASE Gladys;
    ```
    
3. Select the created database.
    ```
    USE Gladys;
    ```
    
4. You can see all tables here once you have applied all the migrations which are discussed later.

5. Exit out of MySQL shell session.
    ```
    exit;
    ```
    
If you have any problems, go through this [video](https://www.youtube.com/watch?v=s16p32pndK0). Similar procedure can be used for Windows and macOS.


### Setup your development environment
1. Fork this repository.

2. Install virtual environment if you haven't and create a virtual environment on your machine.
    ```
    virtualenv -p python3 env
    ```
    
3. Activate the newly created virtual environment.
    ```
    cd env
    source bin/activate
    ```

4. Clone this repository (this would make rebasing easier).
    ```
    git clone https://github.com/deepaktiwari88/Gladys.git
    ```

5. Install the dependencies for the project.
    ```
    cd Gladys
    pip3 install -r requirements.txt
    ```
    
6. Run the migrations and collect static files.
    ```
    python3 manage.py migrate
    python3 manage.py collectstatic
    ```

8. Run the live development server on your machine and test it.
    ```
    python3 manage.py runserver
    ```
    Once the server is started, open http://127.0.0.1:8000 in a web browser.
    Everything went well if the webpage loads correctly and you don't see any errors.

9. Add a remote to your forked repository. This remote will be needed to push your changes to your repo.
    ```
    git remote add myfork https://github.com/<username>/Gladys.git
    ```
