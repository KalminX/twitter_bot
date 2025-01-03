# Sentiment Analysis of Tweets in Pidgin and English

This project is a prototype developed to scrape tweets from Twitter written in Pidgin and English. It performs sentiment analysis on these tweets and classifies them as "Good" or "Bad" based on their sentiment. The project includes both frontend and backend components.

## Features

- **Scraping Tweets**: Fetches tweets from a specified Twitter endpoint using the Gemini API and filters for Pidgin and English.
- **Sentiment Analysis**: Processes the fetched tweets to determine their sentiment, classifying them as positive, neutral, or negative.
- **Classification**: Classifies the sentiment of the tweets as "Good" or "Bad" based on predefined criteria.
- **Frontend Interface**: Provides a simple UI built with HTML and CSS to display the results of the analysis in real-time.
- **Backend API**: Built with Django, it manages the data scraping, sentiment analysis, and serves the results to the frontend.

## Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Django (Python)

## Setup

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Set up the backend**:

   - Install required Python libraries:

     ```bash
     pip install -r requirements.txt
     ```

   - Set up Gemini API keys:
     - Create a Gemini account and generate your API keys.

3. **Set up the frontend**:

   - If you need to make frontend adjustments or run a build:

     ```bash
     npm install
     ```

4. **Run the Django server**:

   ```bash
   python manage.py runserver
   ```

5. **Open your browser** and go to `http://127.0.0.1:8000/` to view the application.

## How It Works

1. The backend, built with Django, scrapes tweets from the Twitter API using the Gemini API with specific filters (such as language).
2. Each tweet is processed for sentiment analysis and classified as either "Good" or "Bad."
3. The results are sent to the frontend, where they are displayed using HTML and CSS in a user-friendly interface.

## Future Enhancements

- **Improved Sentiment Analysis**: Incorporate a more accurate sentiment analysis model, specifically tailored for Pidgin and English.
- **Data Visualization**: Add charts or graphs to visualize sentiment trends over time.
- **User Input**: Allow users to input their own keywords or hashtags to scrape tweets based on their interests.

## License

This project is licensed under the MIT License.

## Acknowledgments

- **Gemini API**: For providing the API used to scrape tweets from Twitter.
- **Django**: The backend framework used to manage the server and data processing.
