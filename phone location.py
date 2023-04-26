import phonenumbers
from phonenumbers import geocoder, carrier, timezone
userMobilenumber = input("\n enter mobile number:")
userMobilenumber = '+'+userMobilenumber
mobilenumber = phonenumbers.parse(userMobilenumber, 'gb')
print("\n mobile number:", mobilenumber)
print("\nlocation:",geocoder.description_for_number(mobilenumber, "en"))
print("\nserviceprovider:", carrier.name_for_number(mobilenumber, "en"))
print("\ntimezone:",timezone.time_zones_for_number(mobilenumber))