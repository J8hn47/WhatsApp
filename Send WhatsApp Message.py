import pywhatkit
import datetime

# Send WhatsApp message to contact or group

# Contact
phone_number = "+3530899656655"
# Group
group_id = "EJZwEcscRl99hqsh65L6rW"

message = "Here is the venue for tonight: https://maps.app.goo.gl/ieMAcJ8ZHoWcH6JM8"

# Get current time and add 2 minutes
current_time = datetime.datetime.now()
time_change = datetime.timedelta(minutes = 2)
later_time = current_time + time_change

# Get new time HRS and MIN
send_at_hrs = later_time.hour
send_at_min = later_time.minute

# Contact
pywhatkit.sendwhatmsg(phone_number, message, send_at_hrs, send_at_min, 30, False, 5)
# Group
pywhatkit.sendwhatmsg_to_group(phone_number, message, send_at_hrs, send_at_min, 30, False, 5)

print("WhatsApp message sent !")
