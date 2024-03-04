# Exam Center Search Web Application

This is a Flask web application that allows users to search for exam centers based on a provided serial number. The application reads data from a CSV file (`seatplan.csv`) containing information about exam centers and their capacities.

## Features

- Users can enter a serial number to search for the corresponding exam center.
- The application displays details such as the name, address, and capacity of the exam center.
- Error handling for invalid input or when no exam center is found for the given serial number.

## Project Structure

exam_center_project/
│
├── seatplan.csv
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── templates/
│ │ ├── index.html
│ │ └── result.html
├── requirements.txt
├── Procfile
├── runtime.txt
└── README.md

- `seatplan.csv`: CSV file containing data about exam centers.
- `app/`: Contains the Flask application code.
- `app/routes.py`: Defines the Flask routes and logic.
- `app/templates/`: Contains HTML templates for rendering pages.
- `requirements.txt`: Lists the Python dependencies.
- `Procfile`: Specifies the command to start the web application.
- `runtime.txt`: Specifies the Python version used in the project.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/exam_center_project.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python app/routes.py
   ```

4. Open a web browser and navigate to `http://127.0.0.1:5000/`.

5. Enter a serial number in the provided form and submit to search for the exam center.

## Deploying to Heroku

To deploy the application to Heroku, follow these steps:

1. Create a Heroku app:

   ```bash
   heroku create your-app-name
   ```

2. Deploy the code to Heroku:

   ```bash
   git push heroku master
   ```

3. Open the deployed app:

   ```bash
   heroku open
   ```

## Credits

This project was created by Mamun
