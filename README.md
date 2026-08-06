# Buffer social media platform API

The easies way to interact with the Buffer API - https://buffer.com


# Functionality
We are __currently developing__ the wrapper. By now it is only able to schedule post and notifications for Instagram, Facebook and Tiktok.

# Explanation
Buffer platform has 2 main functionalities:
  - __Schedule a POST__ that will be automatically published on the date and time you set.
  - __Set a REMINDER__ that will send a notification to your app at that specific time so you can post it manually by yourself.

# Usage
I recommend you to visit the `tests` in the code to see how it works, but here you have __some examples__:

1. Schedule a __post__ of __a reel on Instagram__:
```
client = BufferClient(API_KEY)

# Y, M, D, m, s
DATE = (2026, 8, 7, 16, 50)

post = client.instagram.schedule_reel_post(
    channel_id = INSTAGRAM_CHANNEL_ID,
    video_url = VIDEO_ASSET_DIRECT_LINK,
    text = 'Automated post from buffer-api python library 🚀',
    # date
    year = DATE[0],
    month = DATE[1],
    day = DATE[2],
    hour = DATE[3],
    minute = DATE[4],
    # specific fields
    do_share_to_feed = True,
    is_ai_generated = True,
)
```

2. Schedule a __post__ of __a picture on Facebook__:
```
client = BufferClient(API_KEY)

# Y, M, D, m, s
DATE = (2026, 8, 7, 16, 50)

post = client.facebook.schedule_post_post(
    channel_id = FACEBOOK_CHANNEL_ID,
    image_url = IMAGE_ASSET_DIRECT_LINK,
    text = 'Automated post from buffer-api python library 🚀',
    # date
    year = DATE[0],
    month = DATE[1],
    day = DATE[2],
    hour = DATE[3],
    minute = DATE[4]
)
```

3. Set a __notification reminder on Tiktok__:
```
client = BufferClient(API_KEY)

# Y, M, D, m, s
DATE = (2026, 8, 7, 16, 50)

post = client.tiktok.schedule_reel_notification(
    channel_id = TIKTOK_CHANNEL_ID,
    video_url = VIDEO_ASSET_DIRECT_LINK,
    text = 'Automated post from buffer-api python library 🚀',
    # date
    year = DATE[0],
    month = DATE[1],
    day = DATE[2],
    hour = DATE[3],
    minute = DATE[4]
)
```

# Annotations
The Buffer platform doesn't make a copy of the resources in their servers (by now) when using the API, thats why __you have to provide a direct link to the resource__ you want to upload.

That __link__ has to be __public and accessible at the time__ the post will be actually published. If the link is down, the scheduled post will fail.

# Testing
You can test the functionality through our different test files. Add the environment variables you need in the `.env` file to test it directly with your real data from Buffer. See the `.env.example` to know what to include.