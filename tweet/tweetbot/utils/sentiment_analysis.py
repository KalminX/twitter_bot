import google.generativeai as genai
import os
import time

# Configure the API key and load the model (replace with your API key)
genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")


def analyze_tweets(tweets={}):
    """
    Analyzes sentiment of tweets using Gemini and categorizes them into good and bad.

    Args:
        tweets: A list of dictionaries containing user and tweet keys.

    Returns:
        A dictionary with keys 'good' and 'bad', each containing a list of dictionaries
        with user and tweet keys like the input.
    """
    good_tweets = []
    bad_tweets = []

    print(f"There are {len(tweets)} tweets in total.")

    for count, tweet in enumerate(tweets, start=1):
        text = tweet["tweet"]  # Access the tweet text
        time.sleep(2)

        try:
            print(count)
            # Generate a response to analyze sentiment (can be any prompt)
            response = model.generate_content(
                f"Summarize the sentiment of: {text}")
            sentiment_text = response.text.strip()
            print(sentiment_text)

            # Sentiment analysis based on keywords in the generated response (adjust as needed)
            if "positive" in sentiment_text or "happy" in sentiment_text:
                good_tweets.append(tweet)
            elif "negative" in sentiment_text or "sad" in sentiment_text or "frustrated" in sentiment_text:
                bad_tweets.append(tweet)
        except Exception as e:
            print(f"Error analyzing tweet: {e}")

    return {"good": good_tweets, "bad": bad_tweets}
