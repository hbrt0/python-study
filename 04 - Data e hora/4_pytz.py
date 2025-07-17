from datetime import datetime
import pytz

# Get the current time in the Oslo timezone
oslo_time = datetime.now(pytz.timezone("Europe/Oslo")).astimezone(
    pytz.timezone("Europe/Oslo")
)
# Format the Oslo time to a string in the format "YYYY-MM-DD HH:MM:SS"
formatted_oslo_time = oslo_time.strftime("%Y-%m-%d %H:%M:%S")

# Get the current time in the Sao Paulo timezone
sao_paulo_time = datetime.now(pytz.timezone("America/Sao_Paulo")).astimezone(
    pytz.timezone("America/Sao_Paulo")
)
# Format the Sao Paulo time to a string in the format "YYYY-MM-DD HH:MM:SS"
sao_paulo_time = sao_paulo_time.strftime("%Y-%m-%d %H:%M:%S")

# Print the formatted Oslo time
print(formatted_oslo_time)
# Print the formatted Sao Paulo time
print(sao_paulo_time)
