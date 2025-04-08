import praw

reddit = praw.Reddit(
    client_id="oRNRmUZpHIxNFF4s-TCLvQ",
    client_secret="3hIvm07LddcTgGen1nIuWYQIwM16Sw",
    user_agent="meme_site/0.1"
)

def get_memes(subreddit="memes", limit=10):
    memes = []
    for post in reddit.subreddit(subreddit).hot(limit=limit):
        if not post.stickied and post.url.endswith(('.jpg', '.png', '.gif')):
            memes.append({
                'title': post.title,
                'url': post.url
            })
    return memes
