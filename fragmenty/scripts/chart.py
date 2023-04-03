from pymongo import MongoClient
from datetime import datetime
import numpy as np
from datetime import timezone
import plotly.express as px

client = MongoClient('mongodb://localhost:27017/')
db = client['fragmenty']
collection = db['numbers']

data = list(collection.find(
    {}, {'_id': 0, 'memorabilityScore': 1, 'minimumBidInUSD': 1, 'auctionEndTimestamp': 1, 'number': 1}))

# Calculate the remaining time in hours
now = datetime.now(timezone.utc)
remaining_time_hours = [(datetime.strptime(item['auctionEndTimestamp'],
                         '%Y-%m-%dT%H:%M:%S%z') - now).total_seconds() / 3600 for item in data]


# Normalize remaining time to the range [10, 200] for marker sizes
min_size, max_size = 10, 200
marker_sizes = np.interp(remaining_time_hours, (min(
    remaining_time_hours), max(remaining_time_hours)), (min_size, max_size))


# Extract memorability scores and prices from the data
memorability_scores = [item['memorabilityScore'] for item in data]
prices = [item['minimumBidInUSD'] for item in data]

# Fetch the phone numbers from the data
phone_numbers = [item['number'] for item in data]

# Create the interactive scatter plot
fig = px.scatter(
    x=memorability_scores,
    y=prices,
    size=marker_sizes,
    hover_name=phone_numbers,
    log_y=True,  # Set the y-axis to logarithmic scale
    title='Memorability Score vs Price (Size represents time left)',
    labels={
        'x': 'Memorability Score',
        'y': 'Price (USD)'
    }
)

# Show the plot
fig.show()
