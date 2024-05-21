# expert_pro_test

## Requirements
- Python 3.12.3

### Installation
- clone repo
```
git clone git@github.com:romanannaev/expert_pro_test.git .
```
- create virtual enviroment
```
python3 -m venv venv
```
- install dependencies
```
pip install -r requirements.txt
```
- launch app(from vscode launcher look into .vscode) or from terminal:
```
flask run --port=5000
```
- launch tests(from vscode launcher look into .vscode) or from terminal:
```
pytest
```

### Do request to test app from Postman or curl
```
curl --location --request POST 'http://127.0.0.1:5000/format_hours' \
--header 'Content-Type: application/json' \
--data-raw '{
           "monday" : [],
           "tuesday" : [
               {
                   "type" : "open",
                   "value" : 36000
               },
               {
                   "type" : "close",
                   "value" : 64800
               }
           ],
           "wednesday" : [],
           "thursday" : [
               {
                   "type" : "open",
                   "value" : 37800
               },
               {
                   "type" : "close",
                   "value" : 64800
               }
           ],
           "friday" : [
               {
                   "type" : "open",
                   "value" : 36000
               }
           ],
           "saturday" : [
               {
                   "type" : "close",
                   "value" : 3600
               },
               {
                   "type" : "open",
                   "value" : 36000
               }
           ],
           "sunday" : [
               {
                   "type" : "close",
                   "value" : 3600
               },
               {
                   "type" : "open",
                   "value" : 43200
               },
               {
                   "type" : "close",
                   "value" : 75600
               }
           ]
       }
'
```

### Test task description
```
In short 
Your task is to write an endpoint that accepts JSON-formatted opening hours of a restaurant as an input and returns the rendered human readable format as a text output. 
Input data 
Input JSON consists of keys indicating days of a week and corresponding opening hours as values. One JSON file includes data for one restaurant. 
{ 
<dayofweek>: <opening hours> 
<dayofweek>: <opening hours> 
... 
} 
<dayofweek>: monday / tuesday / wednesday / thursday / friday / saturday / sunday <opening hours>: an array of objects containing opening hours. Each object consist of two keys: 
● type: open or close 
● value: opening / closing time as UNIX time (1.1.1970 as a date), 
e.g. 32400 = 9 AM, 37800 = 10:30 AM, 
max value is 86399 = 11:59:59 PM 
Example: on Mondays a restaurant is open from 9 AM to 8 PM 
{
"monday" : [ 
{ 
"type" : "open", 
"value" : 32400 
}, 
{ 
"type" : "close", 
"value" : 72000 
} 
], 
…. 
} 
Special cases 
● If a restaurant is closed the whole day, an array of opening hours is empty. ○ “tuesday”: [] means a restaurant is closed on Tuesdays 
● A restaurant can be opened and closed multiple times during the same day, ○ E.g. on Mondays from 9 AM - 11 AM and from 1 PM to 5 PM 
● A restaurant might not be closed during the same day 
○ A restaurant can be opened e.g. on a Friday evening and closed early Saturday morning. In that case friday-object includes only the opening time. Closing time is part of the saturday-object. 
○ When printing opening hours which span between multiple days, closing time is always a part of the day when a restaurant was opened (e.g. Friday 8 PM - 1 AM) 
{ 
"friday" : [ 
{ 
"type" : "open", 
"value" : 64800 
} 
], 
“saturday”: [ 
{ 
"type" : "close", 
"value" : 3600 
}, 
{ 
"type" : "open", 
"value" : 32400 
}, 
{ 
"type" : "close", 
"value" : 39600 
}, 
{ 
"type" : "open", 
"value" : 57600 
}, 
{ 
"type" : "close", 
"value" : 82800 
} 
] 
} 


A restaurant is open:

Friday: 6 PM - 1 AM 
Saturday: 9 AM -11 AM, 4 PM - 11 PM


Task 
Build a class in one file that accepts opening hours data as an input (JSON) and returns a more human readable version of the data formatted using a 12-hour clock. Return should be just a plain string.
Output example in 12-hour clock format: 
Monday: 8 AM - 10 AM, 11 AM - 6 PM 
Tuesday: Closed 
Wednesday: 11 AM - 6 PM 
Thursday: 11 AM - 6 PM 
Friday: 11 AM - 9 PM 
Saturday: 11 AM - 9 PM 
Sunday: Closed 
If some imports are required, add requirements.txt or setup.py. Archive your code and send by email or upload to github or any other repository and send a link.
A word about the expected quality 
We consider this exercise as “a PR review”. Our developers will check the code, tests and overall structure and prepare comments & questions they want to go through with you during the interview. 
Send us code you would be happy to review by yourself and discuss further. 
A word about potential edge cases 
If you’re unsure about the expected behavior in some edge cases, please take the best approach you can think of and document your assumptions as part of the readme. 
Technologies 
Use Python 3.10 or higher, 3rd party libraries and frameworks are also allowed.

Full JSON Example Input 
{ 
"monday" : [], 
"tuesday" : [ 
{ 
"type" : "open", 
"value" : 36000 
}, 
{ 
"type" : "close", 
"value" : 64800 
} 
], 
"wednesday" : [], 
"thursday" : [ 
{ 
"type" : "open", 
"value" : 37800 
}, 
{ 
"type" : "close", 
"value" : 64800 
} 
], 
"friday" : [ 
{ 
"type" : "open", 
"value" : 36000 
} 
], 
"saturday" : [ 
{ 
"type" : "close", 
"value" : 3600 
}, 
{ 
"type" : "open", 
"value" : 36000 
} 
], 
"sunday" : [ 
{ 
"type" : "close", 
"value" : 3600 
}, 
{
"type" : "open", 
"value" : 43200 
}, 
{ 
"type" : "close", 
"value" : 75600 
} 
] 
} 
Output 
Monday: Closed 
Tuesday: 10 AM - 6 PM Wednesday: Closed 
Thursday: 10:30 AM - 6 PM Friday: 10 AM - 1 AM Saturday: 10 AM - 1 AM Sunday: 12 PM - 9 PM

```
