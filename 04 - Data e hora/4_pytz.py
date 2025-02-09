from datetime import datetime

import pytz

oslo_time = datetime.now(pytz.timezone("Europe/Oslo")).astimezone(pytz.timezone("Europe/Oslo"))
formatted_oslo_time = oslo_time.strftime("%Y-%m-%d %H:%M:%S")

sao_paulo_time = datetime.now(pytz.timezone("America/Sao_Paulo")).astimezone(pytz.timezone("America/Sao_Paulo"))
sao_paulo_time = sao_paulo_time.strftime("%Y-%m-%d %H:%M:%S")

print(formatted_oslo_time)
print(sao_paulo_time)
