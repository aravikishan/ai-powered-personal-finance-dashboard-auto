# AI-Powered Personal Finance Dashboard

## Overview
The AI-Powered Personal Finance Dashboard is a sophisticated web application designed to assist individuals in managing their personal finances with precision and ease. Utilizing AI technology, this dashboard offers users personalized financial insights, enabling them to make informed decisions regarding their expenditures, savings, and financial objectives. The application integrates functionalities such as transaction tracking, financial goal setting, and AI-generated insights, making it an indispensable tool for anyone aiming to enhance their financial health.

This dashboard is particularly beneficial for individuals who wish to monitor their financial activities, establish and track financial goals, and receive actionable insights to optimize their financial strategies. Whether you are focused on budgeting or maximizing your savings, this application provides the necessary tools to achieve your financial aspirations.

## Features
- **User Management**: Secure authentication and comprehensive profile management for users.
- **Transaction Tracking**: Record and categorize financial transactions with ease.
- **Goal Setting**: Set, track, and manage financial goals with target and current amounts.
- **AI-Generated Insights**: Obtain personalized insights to enhance savings and minimize unnecessary expenses.
- **Responsive Design**: Mobile-friendly interface that adjusts to various screen sizes.
- **Dynamic Content Loading**: Update content seamlessly without page reloads.
- **Thematic Styling**: Customize themes using CSS variables for a tailored user experience.

## Tech Stack
| Component        | Technology        |
|------------------|-------------------|
| Backend          | FastAPI           |
| Frontend         | HTML, CSS, JavaScript |
| Database         | SQLite            |
| ORM              | SQLAlchemy        |
| Web Server       | Uvicorn           |
| Containerization | Docker            |

## Architecture
The project employs a modular architecture where the backend, built with FastAPI, serves the frontend through RESTful API endpoints. The backend handles business logic, database interactions, and serves HTML templates. The frontend utilizes these templates and static files to render a user-friendly interface.

### Diagram
```
+-----------------+       +------------------+
|                 |       |                  |
|  Frontend       | <---- |  Backend         |
|  (HTML/CSS/JS)  |       |  (FastAPI)       |
|                 | ----> |                  |
+-----------------+       +------------------+
        |                           |
        |                           |
        v                           v
+-----------------+       +------------------+
|                 |       |                  |
|  Static Files   |       |  Database        |
|  (CSS/JS)       |       |  (SQLite)        |
|                 |       |                  |
+-----------------+       +------------------+
```

## Getting Started

### Prerequisites
- Python 3.11+
- pip
- Docker (optional for containerized deployment)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-powered-personal-finance-dashboard-auto.git
   cd ai-powered-personal-finance-dashboard-auto
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Start the FastAPI server:
   ```bash
   uvicorn app:app --reload
   ```
2. Visit the application at `http://127.0.0.1:8000`

## API Endpoints
| Method | Path                    | Description                                     |
|--------|-------------------------|-------------------------------------------------|
| GET    | /                       | Returns the main dashboard page                 |
| GET    | /transactions           | Returns the transactions page                   |
| GET    | /goals                  | Returns the goals page                          |
| GET    | /profile                | Returns the user profile page                   |
| GET    | /insights               | Returns the insights page                       |
| GET    | /api/users/{user_id}    | Retrieves user details by user ID               |
| GET    | /api/transactions       | Retrieves all transactions                      |
| POST   | /api/transactions       | Creates a new transaction                       |
| GET    | /api/goals              | Retrieves all goals                             |
| POST   | /api/goals              | Creates a new goal                              |

## Project Structure
```
.
├── Dockerfile                   # Docker configuration file
├── app.py                       # Main application file with FastAPI setup
├── requirements.txt             # Python dependencies
├── start.sh                     # Script to start the application
├── static/
│   ├── bootstrap.min.css        # Bootstrap CSS for styling
│   ├── css/
│   │   └── style.css            # Custom CSS for application styling
│   └── js/
│       └── main.js              # JavaScript for dynamic interactions
├── templates/
│   ├── dashboard.html           # HTML template for the dashboard
│   ├── goals.html               # HTML template for goals
│   ├── insights.html            # HTML template for insights
│   ├── profile.html             # HTML template for user profile
│   └── transactions.html        # HTML template for transactions
└── finance_dashboard.db         # SQLite database file
```

## Screenshots
*Screenshots of the application will be placed here.*

## Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t finance-dashboard .
   ```
2. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 finance-dashboard
   ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements, bug fixes, or new features. Ensure that your code adheres to the project's coding standards and includes relevant tests.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---
Built with Python and FastAPI.