P_rain = 0.3
P_cloudy_given_rain = 0.8
P_cloudy_given_no_rain = 0.4
P_no_rain = 1 - P_rain
P_cloudy = (P_cloudy_given_rain * P_rain) + (P_cloudy_given_no_rain * P_no_rain)
P_rain_given_cloudy = (P_cloudy_given_rain * P_rain) / P_cloudy
print("Probability of Cloudy:", P_cloudy)
print("Probability of Rain given Cloudy:", P_rain_given_cloudy)
