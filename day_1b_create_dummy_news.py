import pandas as pd

print("Creating dummy news data with expanded dataset (up to Nov 2025)...")

# Create a list of dictionaries with sample data
# In a real project, this would come from a News API
dummy_news = [
    # --- 2023 ---
    {'date': '2023-11-05', 'headline': 'Apple reports record-breaking quarter, iPhone sales soar'},
    {'date': '2023-11-12', 'headline': 'Market analysts set to "neutral" on AAPL stock this week'},
    {'date': '2023-11-15', 'headline': 'Analysts raise price target for AAPL citing strong demand'},
    {'date': '2023-11-20', 'headline': 'Apple faces $1.5 billion fine in European patent dispute'},
    {'date': '2023-11-28', 'headline': 'Black Friday sales for iPhones and MacBooks are "strong"'},
    {'date': '2023-12-05', 'headline': "New report claims Apple's car project is facing major delays"},
    {'date': '2023-12-10', 'headline': 'Supply chain issues may cause holiday delays for Apple'},
    {'date': '2023-12-18', 'headline': "Apple stock dips 2% on news of competitor's new chip"},
    {'date': '2023-12-20', 'headline': 'Apple unveils new M3 chips to critical acclaim'},
    
    # --- 2024 ---
    {'date': '2024-01-02', 'headline': 'Analysts predict a "tough quarter" for iPhone sales in China'},
    {'date': '2024-01-10', 'headline': 'Vision Pro launch date officially announced for February'},
    {'date': '2024-01-15', 'headline': 'Market correction hits tech stocks, Apple shares dip 4%'},
    {'date': '2024-01-20', 'headline': 'Apple facing lawsuit over app store policies'},
    {'date': '2024-01-25', 'headline': 'Vision Pro pre-orders are "better than expected"'},
    {'date': '2024-02-02', 'headline': 'Apple earnings call: revenue beats expectations, but iPhone sales slightly miss'},
    {'date': '2024-02-10', 'headline': 'Vision Pro launch sees mixed reviews but strong initial sales'},
    {'date': '2024-02-14', 'headline': 'Apple announces new investment in renewable energy projects'},
    {'date': '2024-02-28', 'headline': 'EU antitrust regulators hit Apple with a massive fine'},
    {'date': '2024-03-05', 'headline': 'Investors bullish on Apple’s new AI initiatives'},
    {'date': '2024-03-11', 'headline': "Apple's autonomous car project officially cancelled"},
    {'date': '2024-03-15', 'headline': 'Apple stock considered a "strong buy" by top firms'},
    {'date': '2024-03-22', 'headline': 'DOJ sues Apple, alleging smartphone monopoly; stock tumbles'}, # <-- FIXED
    {'date': '2024-04-01', 'headline': 'Tim Cook interview hints at "exciting" new product category'},
    {'date': '2024-04-10', 'headline': 'Competitor launches new phone, analysts see little threat to Apple'},
    {'date': '2024-04-17', 'headline': 'Apple supplier Foxconn reports slightly lower than expected earnings'},
    {'date': '2024-05-02', 'headline': 'AAPL shares jump 6% as company announces historic $110B stock buyback'},
    {'date': '2024-05-15', 'headline': 'New iPad Pro with M4 chip gets positive reviews from creators'},
    {'date': '2024-06-03', 'headline': "Speculation builds for Apple's AI plans ahead of WWDC"},
    {'date': '2024-06-10', 'headline': 'WWDC: Apple unveils "Apple Intelligence," partners with OpenAI'},
    {'date': '2024-06-11', 'headline': 'Stock jumps to all-time high after "Apple Intelligence" showcase'},
    {'date': '2024-06-18', 'headline': "EU opens new investigation into Apple's App Store compliance"},
    {'date': '2024-07-05', 'headline': "Apple's AI features 'underwhelm' some early beta testers"},
    {'date': '2024-07-20', 'headline': 'Apple manufacturing partner announces new factory in India'},
    {'date': '2024-08-01', 'headline': "Apple's quarterly earnings beat expectations, services revenue strong"},
    {'date': '2024-08-15', 'headline': 'iPhone 16 production reportedly "on schedule" for September launch'},
    {'date': '2024-08-28', 'headline': 'Leaked photos of iPhone 16 show minimal design changes'},
    {'date': '2024-09-09', 'headline': 'Apple "Wonderlust" event: iPhone 16 and new Apple Watch unveiled'},
    {'date': '2024-09-10', 'headline': 'New iPhone 16 launched, "revolutionary" AI features praised'},
    {'date': '2024-09-12', 'headline': 'Some users report minor bugs in new iOS update'},
    {'date': '2024-09-20', 'headline': 'iPhone 16 launch day sees long lines at Apple stores worldwide'},
    {'date': '2024-10-15', 'headline': 'China sales for new iPhone 16 are "sluggish," according to reports'},
    {'date': '2024-10-25', 'headline': 'Apple beats earnings expectations, services revenue hits all-time high'},
    
    # --- 2025 (NEW DATA) ---
    {'date': '2025-01-15', 'headline': 'Apple stock downgraded to "hold" by major bank over China concerns'},
    {'date': '2025-01-30', 'headline': 'Apple Q4 earnings: Revenue miss, stock drops 5% in after-hours'},
    {'date': '2025-02-10', 'headline': 'Reports of "Vision Pro 2" development with lighter, cheaper design'},
    {'date': '2025-02-28', 'headline': 'Apple settles major DOJ lawsuit, agreeing to App Store changes'},
    {'date': '2025-03-15', 'headline': 'Apple announces new M5 chip, promises "unprecedented" performance'},
    {'date': '2025-04-05', 'headline': "Market analysts optimistic about Apple's new AI software subscription"},
    {'date': '2025-04-20', 'headline': "Competitor's new AI phone fails to dent iPhone market share"},
    {'date': '2025-05-10', 'headline': 'Apple Q1 earnings beat expectations, Services and AI revenue soar'},
    {'date': '2025-06-12', 'headline': 'WWDC 2025: "Apple Intelligence 2.0" deeply integrated into new OS'},
    {'date': '2025-07-01', 'headline': 'Apple stock hits new all-time high above $250 per share'},
    {'date': '2025-07-20', 'headline': 'Supply chain rumors hint at folding "iPhone Fold" device for 2026'},
    {'date': '2025-08-15', 'headline': 'Anticipation builds for iPhone 17, expected to be "major redesign"'},
    {'date': '2025-09-10', 'headline': 'Apple Event: iPhone 17, new Apple Watch Ultra, and AI-powered AirPods'},
    {'date': '2025-09-25', 'headline': 'iPhone 17 pre-orders break all-time records, stock surges'},
    {'date': '2025-10-28', 'headline': 'Apple Q3 earnings: another record quarter, AI subscriptions a huge success'}
]

# Convert the list to a pandas DataFrame
news_df = pd.DataFrame(dummy_news)

# Ensure the date column is in datetime format
news_df['date'] = pd.to_datetime(news_df['date'])

# Save to CSV
news_df.to_csv('news_data.csv', index=False)

print(f"Successfully saved expanded dummy news data (up to Nov 2025) to 'news_data.csv'")
print(news_df.tail()) # Show the new data just added