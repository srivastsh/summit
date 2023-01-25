import streamlit as st
import requests
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def generate_summary(text):
    parser = HtmlParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, 10)
    summary_text = " ".join([str(sentence) for sentence in summary])
    return summary_text

def get_tweets_text(thread_link):
    """
    This function will return the all tweets text in thread
    """
    res = requests.get(thread_link)
    return res.text

def main():
    st.title("Summ It - Twitter Thread Summary Generator")

    thread_link = st.text_input("Enter the link to the Twitter thread:")

    if st.button("Summ It!"):
        tweets_text = get_tweets_text(thread_link)
        summary = generate_summary(tweets_text)
        st.write("Summary:")
        st.write(summary)

if __name__ == '__main__':
    main()
