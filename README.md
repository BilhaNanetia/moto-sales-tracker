# BeeMoto Sales Tracker
## Project Overview
This project is a web-based sales record system for a motorbike spares shop. It allows users to add sales records, view daily totals,list daily sales and delete sales records. The system uses a SQLite database for data storage, Flask for the backend, and HTML/JavaScript with Tailwind CSS for the frontend.It also includes user authentication features for enhanced security.
## Features
- User authentication (signup, login, logout)
- Add new sales records with item name, quantity, and price
- Calculate and display daily sales totals
- View itemized daily sales records
- Delete sales records
- Currency display in Kenya Shillings (KES)
## Technologies Used
- Backend:
  - Python 3.x
  - Flask
  - Flask-Login (for user authentication)
  - SQLite
  - Werkzeug (for password hashing)
- Frontend:
  - HTML5
  - JavaScript
  - Tailwind CSS (via CDN)
## Setup and Installation
1. Clone the repository:
``` console
git clone https://github.com/BilhaNanetia/moto-sales-tracker.git
cd moto-sales-tracker
```
2. Set up a virtual environment
```console
python -m venv venv
source venv/bin/activate
```
3. Install the required packages:
``` console
pip install -r requirements.txt
```
4. Navigate to the backend directory:
``` console
cd backend
```
- Since the database is already setup,
5. Run the Flask application:
``` console
python app.py
```
6. Open a web browser and go to `http://localhost:5000` to access the application.
## Usage
1. **Sign Up / Login:**
- New users can sign up for an account on the signup page.
- Existing users can log in on the login page.
2. **Adding a Sale:**
- Fill in the item name, quantity, and price in the "Add Sale" section.
- Click "Add Sale" to record the transaction.
3. **Viewing Daily Total:**
- Select a date in the "Get Daily Total" section.
- Click "Get Total" to see the total sales for that day.
4. **Viewing Daily Sales:**
- Select a date in the "View Daily Sales" section.
- Click "View Sales" to see a list of all sales for that day.
5. **Deleting a sale:**
- Click "Delete" to delete a sale in the "View Daily Sales" section.
6. **Logout:**
- Click the "Logout" button in the top-right corner to end your session.
## Database
The system uses an SQLite database (`sales_record.db`) to store sales records and user information. The database is automatically created when you run the initialization script.
## Security
- User passwords are hashed using Werkzeug's security features before being stored in the database.
- Flask-Login is used to manage user sessions securely.
- All main features require user authentication to access.
## Customization
- To change the background image, replace the file at `frontend/static/images/rohan-JtyFzLCihTg-unsplash.jpg` with your desired image.
- Modify the Tailwind classes in `index.html` to adjust the styling.
- Additional custom styles can be added to `frontend/static/styles.css`.
## Contributing
Contributions to this project are welcome. Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request
## License
This project is licensed under the MIT License - see the LICENSE file for details.
## Acknowledgments
- Unsplash for background images
- Tailwind CSS for the styling framework
- Flask community for the excellent web framework
## Contact
Feel free to contact me through  bilhaleposo@gmail.com

Project Link: [https://github.com/BilhaNanetia/moto-sales-tracker] (https://github.com/BilhaNanetia/moto-sales-tracker)