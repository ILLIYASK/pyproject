# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "ACfc6ea1c9a9fb8ccb1512129f0817a3bb"
auth_token = "f629238878fc0de07c3af46918456af8"
verify_sid = "VAdead5e0e7181efeaec2f1711f1193de5"
verified_number = "+918606913836"

client = Client(account_sid, auth_token)

verification = client.verify.v2.services(verify_sid) \
  .verifications \
  .create(to=verified_number, channel="sms")
print(verification.status)

otp_code = input("Please enter the OTP:")

verification_check = client.verify.v2.services(verify_sid) \
  .verification_checks \
  .create(to=verified_number, code=otp_code)
print(verification_check.status)