AUTHOR = 'Nicola Schiavo'
SITENAME = "Nicola Schiavo's Personal Website 🦎 🦐"
SITEURL = 'https://maresciallonino.github.io'


PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

ARTICLE_PATHS = ['articles']

MENUITEMS = [
    ('About', '/'),
    ('Articles', '/category/articles.html'),  # Link to the category page for articles
    ('Books', '/pages/books.html'),
    ('Projects', '/pages/projects.html'),
]

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



# Social widget
SOCIAL = (
    ("github","https://github.com/marescialloNino"),
    ("linkedin","https://www.linkedin.com/in/nicola-schiavo-a3281b271/"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Do not generate the default article index at /
DIRECT_TEMPLATES = ['tags', 'categories', 'archives']
