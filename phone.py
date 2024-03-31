import phonenumbers
from phonenumbers import carrier, geocoder, timezone

def details(phone):
    mobile_carrier = carrier.name_for_number(phone, "en")
    mobile_timezones = timezone.time_zones_for_number(phone)
    geo_description = geocoder.description_for_number(phone, "en")
    is_valid = phonenumbers.is_valid_number(phone)
    is_valid_region = phonenumbers.is_valid_number_for_region(phone, "NG")
    is_possible = phonenumbers.is_possible_number(phone)
    
    return details

mobileNo = input("Enter Mobile Number with Country code: ")
phone = phonenumbers.parse(mobileNo)
mobile_carrier = carrier.name_for_number(phone, "en")
mobile_timezones = timezone.time_zones_for_number(phone)
geo_description = geocoder.description_for_number(phone, "en")
is_valid = phonenumbers.is_valid_number(phone)
is_valid_region = phonenumbers.is_valid_number_for_region(phone, "NG")
is_possible = phonenumbers.is_possible_number(phone)

# details(mobileNo)
