import json


def read_tweets_from_file(file_path):
    """
    Reads tweets from a JSON file.

    Args:
        file_path: The path to the JSON file.

    Returns:
        A list of tweets.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data.get("tweets", [])


def write_analysis_to_file(file_path, analysis_result):
    """
    Writes the sentiment analysis result to a JSON file.

    Args:
        file_path: The path to the output JSON file.
        analysis_result: The sentiment analysis result to write.
    """
    with open(file_path, 'w') as f:
        json.dump(analysis_result, f, indent=4)
