from datetime import datetime, timedelta, timezone

# Create a datetime object for the current time in Oslo, which is UTC+2
data_oslo = datetime.now(timezone(timedelta(hours=2)))

# Create a datetime object for the current time in São Paulo, which is UTC-3
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

# Print the current time in Oslo
print(data_oslo)

# Print the current time in São Paulo
print(data_sao_paulo)
