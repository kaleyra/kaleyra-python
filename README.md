<p align="center">
<img src=https://media.licdn.com/dms/image/C4E1BAQEhWsmiOrN0jA/company-background_10000/0?e=2159024400&v=beta&t=e-l5A60dSZUlQxmOUUnjJFTA8FyBQzPME_2tK0avqm8>
</p>

# [Kaleyra](https://www.kaleyra.com/)
Kaleyra is a global communications solutions provider that offers an extensive range of telecommunication services for banks, retail and e-commerce companies, and enterprises. Through a global platform, Kaleyra enables its customers to reach, engage and manage an integrated and multi-channel notification services such as messages, push notifications, emails, instant messaging and voice services. Our services help business connect and communicate with their customers increasing customer retention and satisfaction in an easy and effective manner.
Our mission is to make customer communication between business and their customers uncomplicated by removing the technology barrier with our cutting edge communication platforms. 
## Getting Started
### Prerequisites
- Python has to be installed on your system (version 3.7 or higher)
- An IDE for working on the library ([Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows) is recommended)
### Creating an account
- To use the library, you will need a Kaleyra account, a valid sender ID and an API key.
- Sign up for a Kaleyra account by clicking [here](http://accounts.kaleyra.com/login?next=home).
- Click on New Service and select Alert.
- Verify your mobile number and e-mail id.
- Visit [Alerts Kaleyra](https://alerts.kaleyra.com/)
- Login using the credentials provided in the e-mail sent after signing up.
- From the left hand menu, go to Developer->API keys and request for a new API key.
- API Key will be sent to your e-mail.
- Apply for approval of your sender ID by sending a mail to support@kaleyra.com
### Getting the library on your system
- Git clone or download the library package onto your system
### Configuring the library
- Enter your approved sender ID and API Key in the file named config.py under configuration.
- You have successfully configured the library and you are now free to send messages, create txtly links and much more!
### Using the library
The library contains functions to consume 15 different types of APIs provided by Kaleyra:
 - Send SMS
 - Schedule SMS
 - Modify Scheduled SMS
 - Delete Scheduled SMS
 - Check SMS Status
 - Check Credits
 - Check Credit Usage in a date range
 - Create Txtly Link
 - Extract Txtly Reports
 - Pull Individual Txtly Logs
 - Delete Txtly Link
 - Create SMS group
 - Add contacts to SMS group
 - Send SMS to group
 - Send SMS to an optin group
 
 ## Quickstart
 ### Send an SMS
 ```python
from api.sms.SMSMessageRequest import SMSMessageRequest

smsMessageRequest = SMSMessageRequest(to='91XXXXXXXXXX', 
                                       message='Sending message from V4 send sms')

smsMessageResponse = smsMessageRequest.send()

print(smsMessageResponse.to_json())
 ```
 ### Schedule an SMS
 ```python
from api.sms.SMSMessageRequest import SMSMessageRequest

smsMessageRequest = SMSMessageRequest(to='91XXXXXXXXXX', 
                                       message='Sending message from V4 schedule sms')
smsMessageRequest.set_schedule(datetime='10-06-2019 10:30 am', 
                                format='dd-mm-yyyy hh:mm am/pm')

smsMessageResponse = smsMessageRequest.schedule()

print(smsMessageResponse.to_json())
 ```
 
 ### Create an SMS Group
  ```python
from api.messaging.group.group_request import GroupRequest

groupRequest = GroupRequest(group_name='grp_name')

groupResponse = groupRequest.create()

print(groupResponse.to_json())
   ```
### Create a Txtly Link
```python
from api.txtly.txtly_request import TxtlyRequest

txtlyRequest = TxtlyRequest(url='https://www.kaleyra.com', 
                            token='kaleyra', 
                            title='Kaleyra')

txtlyResponse = txtlyRequest.create()

print(txtlyResponse.to_json())
```
 
 
 # Documentation
 The documentation for the Kaleyra API can be found [here](https://apidocs-sms.kaleyra.com/?version=latest).
# Getting help
If you need help configuring or using the library, please check the [Kaleyra Support Help Center](http://support.kaleyra.com/support/home) first, and file a support ticket if you don't find an answer to your question.

If you've instead found a bug in the library or would like new features added, go ahead and open issues or pull requests against this repo!
