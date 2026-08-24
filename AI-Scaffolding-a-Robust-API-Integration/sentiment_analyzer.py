#!/usr/bin/python3
"""
Sentiment Analysis Tool.
Analyzes sentiment using a public API with secure authentication.
"""
import os
import requests
import sys


def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text using the Text Processing API.

    Args:
        text (str): The sentence to analyze.

    Returns:
        str: The sentiment label or None if an error occurs.
    """
    api_key = os.environ.get("TEXT_PROCESSING_API_KEY")

    if not api_key:
        print(
            "Error: TEXT_PROCESSING_API_KEY is not set.",
            file=sys.stderr
        )
        return None

    url = "https://text-processing.com/api/sentiment/"
    payload = {"text": text}
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    try:
        response = requests.post(
            url,
            data=payload,
            headers=headers,
            timeout=10
        )
        response.raise_for_status()

        data = response.json()
        label = data.get("label", "neutral")

        if label == "pos":
            return "positive"
        elif label == "neg":
            return "negative"
        else:
            return "neutral"

    except requests.exceptions.Timeout:
        print(
            "Error: The request timed out. Please try again later.",
            file=sys.stderr
        )
        return None

    except requests.exceptions.ConnectionError:
        print(
            "Error: Could not connect to the API server.",
            file=sys.stderr
        )
        return None

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}", file=sys.stderr)
        return None

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}", file=sys.stderr)
        return None

    except (KeyError, ValueError) as e:
        print(f"Invalid response format: {e}", file=sys.stderr)
        return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./sentiment_analyzer.py <sentence>")
        sys.exit(1)

    sentence = " ".join(sys.argv[1:])
    result = analyze_sentiment(sentence)

    if result:
        print(result)
    else:
        sys.exit(1)
