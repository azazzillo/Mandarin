# MANDARIN

## About the Project
**MANDARIN** is a recommendation platform that helps users find the best places to visit in their city based on their current mood. The website suggests venues such as cafes, restaurants, clubs, libraries, and theaters by analyzing user input and fetching highly rated locations.

## How It Works
1. The user describes their mood and submits a request.
2. The request is sent to ChatGPT, which determines the type of venue that best matches the user's mood.
3. The system uses Selenium to search for suitable places on **2GIS**.
4. The best 1-3 venues are selected, and their top reviews are displayed to motivate the user to visit them.

## Tech Stack
- **Backend Framework:** FastAPI
- **Database:** PostgreSQL
- **Web Scraping:** Selenium
- **Task Queue:** Celery + Redis
- **AI Integration:** OpenAI API (ChatGPT)

## Getting Started
### Prerequisites
Ensure you have Python installed on your system. Then, clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/MANDARIN.git
cd MANDARIN
```

### Installation
1. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

### Running the Project
1. **Start Redis:** *(Ensure Redis is installed and running)*
```bash
redis-server
```
2. **Start Celery worker:**
```bash
celery -A app.celery worker --loglevel=info
```
3. **Run FastAPI server:**
```bash
uvicorn app.main:app --reload
```

### API Documentation
Once the server is running, you can access API documentation at:
- Swagger UI: [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs)
- ReDoc: [http://127.0.0.1:8080/redoc](http://127.0.0.1:8080/redoc)

## Contribution
Feel free to contribute by submitting issues or pull requests!

## License
This project is licensed under the MIT License.

