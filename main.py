import pandas as pd

# Load the data
df = pd.read_csv("KarrotData.csv")

# Convert relevant columns to numeric values
df['Spend'] = df['Spend'].replace(r'[\$,]', '', regex=True).astype(float)
df['Impressions'] = df['Impressions'].replace(',', '', regex=True).astype(int)
df['Clicks'] = df['Clicks'].replace(',', '', regex=True).astype(int)
df['Purchase'] = df['Purchase'].astype(int)

# Calculate performance metrics
df["CTR"] = (df["Clicks"] / df["Impressions"]) * 100
df["Conversion Rate"] = (df["Purchase"] / df["Clicks"]) * 100
df["Cost per Purchase"] = df["Spend"] / df["Purchase"]

# Group by Campaign
campaign_performance = df.groupby("Campaign Name").agg({'Spend': 'sum', 'Impressions': 'sum', 'Clicks': 'sum', 'Purchase': 'sum'}).reset_index()
campaign_performance["CTR"] = (campaign_performance["Clicks"] / campaign_performance["Impressions"]) * 100
campaign_performance["Conversion Rate"] = (campaign_performance["Purchase"] / campaign_performance["Clicks"]) * 100
campaign_performance["Cost per Purchase"] = campaign_performance["Spend"] / campaign_performance["Purchase"]

# Best Performing Campaign
best_campaign = campaign_performance.sort_values(by="Cost per Purchase").iloc[0]
print(best_campaign)

# Group by Ad
ad_performance = df.groupby("Ad").agg({'Spend': 'sum', 'Impressions': 'sum', 'Clicks': 'sum', 'Purchase': 'sum'}).reset_index()
ad_performance["CTR"] = (ad_performance["Clicks"] / ad_performance["Impressions"]) * 100
ad_performance["Conversion Rate"] = (ad_performance["Purchase"] / ad_performance["Clicks"]) * 100
ad_performance["Cost per Purchase"] = ad_performance["Spend"] / ad_performance["Purchase"]

# Best Performing Ads
best_ads = ad_performance.sort_values(by="Cost per Purchase").head()
print(best_ads)

# Suggested Budget Allocation
campaign_performance["Suggested Budget"] = campaign_performance["Spend"] * (1 / campaign_performance["Cost per Purchase"])
print(campaign_performance[["Campaign Name", "Suggested Budget"]].sort_values(by="Suggested Budget", ascending=False))
