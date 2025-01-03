from .utils.file_operations import read_tweets_from_file, write_analysis_to_file
from .utils.sentiment_analysis import analyze_tweets
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from .models import Tweet
import json

@csrf_exempt
def index(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            tweets = data.get('tweets')
            
            if not isinstance(tweets, list):
                return HttpResponseBadRequest("The 'tweets' key should contain a list of tweets")

            for tweet_data in tweets:
                user = tweet_data.get('user')
                tweet_text = tweet_data.get('tweet')
                
                if not user or not tweet_text:
                    return HttpResponseBadRequest("Each tweet must include both 'user' and 'tweet' fields")

                Tweet.objects.create(user=user, tweet=tweet_text)

            return JsonResponse({'status': 'ok', 'message': 'Tweets saved successfully'})

        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON format")
    elif request.method == 'GET':
        return analyze_tweets_view(request)

def analyze_tweets_view(request):
    import os


    absolute_path = os.path.join(
        os.path.dirname(__file__), 'assets', 'pidgin_2.json')
    with open(absolute_path, 'r') as f:
        tweets = json.load(f)
        print(type(tweets))

    # Define file paths
        output_file_path = 'output_analysis.json'

    # Read the tweets from the file

    # Analyze sentiment and categorize tweets
    #     sentiment_analysis = analyze_tweets(tweets["tweets"])
    #     print(sentiment_analysis)

    # # Write the analysis result to a file
    #     write_analysis_to_file(output_file_path, sentiment_analysis)

    # Read the analysis result for display
        with open(output_file_path, 'r') as f:
            result_data = json.load(f)
            print(result_data)

    # Render the results to a template
    return render(request, 'tweetbot/index.html', {'bad_tweets': result_data['bad']})
