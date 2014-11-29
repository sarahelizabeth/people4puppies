# -*- coding: utf-8 -*-

"""
Tarbell project configuration
"""

# Short project name
NAME = "people4puppies"

# Descriptive title of project
TITLE = "People 4 Puppies"

# Google spreadsheet key
SPREADSHEET_KEY = "1mRdTX8dh6LfrD2jwSKyaD7j0l_MWTNG0XKQX8UAUoPQ"

# Exclude these files from publication
EXCLUDES = ["*.md", "requirements.txt"]

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# S3 bucket configuration
S3_BUCKETS = {
    # Provide target -> s3 url pairs, such as:
    #     "mytarget": "mys3url.bucket.url/some/path"
    # then use tarbell publish mytarget to publish to it
    "production": "portfolio.sarahemuraray.com/people4puppies",
    "staging": "staging.sarahemurray.com/people4puppies",
}

# Default template variables
DEFAULT_CONTEXT = {
    'name': 'people4puppies',
    'title': 'People 4 Puppies'
}