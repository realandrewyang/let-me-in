# let-me-in

I built a notification system that alerts me when one or more spots open up in a course for the Winter 2020 term.

The system uses a cron that scrapes the [uWaterloo course schedule website](http://www.adm.uwaterloo.ca/infocour/CIR/SA/under.html) every half hour within business hours and checks if the desired course goes from filled/overfilled to available. Then it sends an SMS to my phone.

I wrote this system in Python using a (mostly) functional style, which helped keep my code concise and easy to debug.
