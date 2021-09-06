import os

# Chrome Driver Location
PATH = "./driver/chromedriver"

# Web App
APP = "http://127.0.0.1:80/"

# Demo Login Details
DEMO_EMAIL = "random@gmail.com"
DEMO_PASSWORD = "asdasdasd"

# End Points
end_points = [
    "tab-orm",
    "tab-slowdb",
    "tab-slowrequest",
    "tab-swallowedexception",
    "tab-untracked",
    "tab-logout"
]

# API Points
GETUSERS = "/getusers"
GETTODOS = "/gettodos"
GETPHOTOS = "/getphotos"
GETPOSTS = "/getposts"
GETCOMMENTS = "/getcomments"
GETALBUMS = "/getalbums"
SLOWREQUEST = "/slowrequest"
BADWEBREQUEST = "/badwebrequest"
POST = "/post"
DELETE = "/delete"
PUT = "/put"
PATH = "/path"

# Included API Points
api_list = [
    GETUSERS,
    GETTODOS,
    GETPHOTOS,
    GETPOSTS,
    GETCOMMENTS,
    GETALBUMS,
    SLOWREQUEST,
    # BADWEBREQUEST,
    # POST,
    # DELETE,
    # PUT,
    # PATH
]

# Interval (seconds)
sequence_interval = 300