# AI in Finance: Stock Sentiment vs. Price Analysis

This is a 3-day project built to analyze the correlation between financial news sentiment and the stock price of Apple ($AAPL).

![Final Chart](stock_vs_sentiment.png)

---

### 📝 Project Goal

The goal was to fetch real stock data and financial news, use an AI model (VADER) to perform sentiment analysis on the headlines, and visualize the relationship between the market "mood" and the stock's price.

---

### 🛠️ Tech Stack Used

* **Python:** Core programming language
* **Pandas:** For data manipulation and merging
* **yfinance:** To download historical stock data
* **VADER (vaderSentiment):** For lexicon-based NLP sentiment analysis
* **Matplotlib:** For data visualization

---

### 🚀 How to Run This Project

1.  Clone the repository:
    `git clone https://github.com/YOUR_USERNAME/AI-Finance-Sentiment-Project.git`
2.  Install the required libraries:
    `pip install -r requirements.txt`
3.  Run the scripts in order:
    `python day_1a_get_stock_data.py`
    `python day_1b_create_dummy_news.py`
    `python day_2_analysis.py`
    `python day_3_visualization.py`
