# xrwvm-fullstack_developer_capstone

**Repository name:** xrwvm-fullstack_developer_capstone

**Project name:** Best Cars Dealership – Full-Stack Developer Capstone

## About the project

Best Cars is a national car retailer in the U.S. with dealership branches across many states. This web application lets visitors browse the dealership branches, filter them by state, and read customer reviews of each dealer. Registered users can log in and post their own reviews, which are run through a sentiment-analysis microservice and shown as positive, neutral or negative.

## Architecture

| Component | Technology | Purpose |
|---|---|---|
| Web app and user management | Django + SQLite | Login, logout, registration, car makes and models, proxy to the backend services |
| Frontend | React (Login, Register, Dealers, Dealer, PostReview) and Django templates (Home, About, Contact) | User interface |
| Dealers and reviews API | Node.js + Express + MongoDB | Stores dealerships and reviews |
| Sentiment analyzer | Flask + NLTK VADER | Classifies review text as positive, negative or neutral |
| CI | GitHub Actions | Lints Python (flake8) and JavaScript (JSHint) on every push |
| Deployment | Docker, Kubernetes, IBM Cloud Code Engine | Containerised deployment |

## Django API endpoints

| Endpoint | Description |
|---|---|
| `POST /djangoapp/login` | Log in a user |
| `GET /djangoapp/logout` | Log out the current user |
| `POST /djangoapp/register` | Register a new user |
| `GET /djangoapp/get_dealers` | List all dealers |
| `GET /djangoapp/get_dealers/<state>` | List dealers in a state |
| `GET /djangoapp/dealer/<id>` | Details of one dealer |
| `GET /djangoapp/reviews/dealer/<id>` | Reviews of a dealer, with sentiment |
| `POST /djangoapp/add_review` | Post a review (logged-in users) |
| `GET /djangoapp/get_cars` | All car makes and models |

## Running locally

```bash
# 1. Dealers and reviews backend (MongoDB + Express)
cd server/database
docker build . -t nodeapp
docker-compose up

# 2. Sentiment analyzer
cd server/djangoapp/microservices
pip install -r requirements.txt
python -m flask run --port 5050

# 3. React frontend
cd server/frontend
npm install
npm run build

# 4. Django
cd server
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Set `backend_url` and `sentiment_analyzer_url` in `server/djangoapp/.env` to point at the backend and the sentiment analyzer.
