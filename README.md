# frontdoor
A Raspberry Pi project using PiCamera and a motion sensor to see who is at the front door.

## Resources 
- [https://www.raspberrypi.org]
- [https://api.slack.com/]

## Setup
1. Raspberry Pi
2. Python 2.7

## Components
1. Camera 
2. Motion Sensor

## data.json
This project expects a file called *data.json* to be in the project's base directory.
It should be formatted like this:
```json
{
    "token" : "xxxx-xxxxx-xxxxx-xxxxx",
    "user" : "yyyyyy",
	"channel" : "#channel"
}
```
