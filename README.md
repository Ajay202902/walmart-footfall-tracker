# Walmart Visitors Counter and Dashboard

This is a web application for tracking and visualizing footfall in real-time at a Walmart store, along with a dashboard for data analysis. The project was developed during my placement training with 10 Seconds at Sahyadri College, showcasing my full stack web development skills.

## Technologies Used

- Front-end: HTML, CSS, JavaScript, Bootstrap, AJAX
- Back-end: API[Python, Flask]
            Database[mysql]

## Features

- Real-time tracking of footfall at a Walmart store
- Visualization of key metrics such as total visitors, Visitors for a day, Male visitors,female visitors
- Interactive charts for data analysis

## Installation

1. Clone the repository to your local machine.
2. Create a database named "walmart" using XAMPP.
3. Within the "walmart" database, create a table with the following structure
            CREATE server_walmart (
            id INT AUTO_INCREMENT PRIMARY KEY,
            gender VARCHAR(30),
            age INT,
            comments VARCHAR,
            date DATE
            );
4. Open the server_walmart folder in VS Code.
5. Open the terminal in VS Code and execute the following commands to set up the Flask server:
            [^1]: py -3 -m venv venv
            [^2]: venv\Scripts\activate
            3. pip install Flask
            4. pip install pymysql
            5. pip install flask-cors
            6. pip install flask-sqlalchemy
            7. pip uninstall SQLAlchemy 
            8. pip freeze 
            9. pip install SQLAlchemy==1.4.46

6. Run the following command in the terminal to start the Flask application:
            python app.py

7. Open the "walmart" page and "dashboard" page located in the ui_walmart folder.
8. Explore the Walmart project by interacting with the UI.


Make sure you have XAMPP running with the Apache and MySQL services enabled before starting the Flask server. The application should now be up and running locally.



## Contributing

I welcome contributions to improve the project! If you have any suggestions, bug reports, or want to add new features, feel free to open an issue or submit a pull request.


