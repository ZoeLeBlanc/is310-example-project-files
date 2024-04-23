AUTHOR = 'Zoe LeBlanc'
SITENAME = 'IS310 Example Project Site'
SITEURL = "https://zoeleblanc.com/is310-example-project"

PATH = "content"

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Humanizing Technology: Computationally Exploring the Humanist Listserv & the Rise of Web Technologies", "#"),
    ("IS310 Course Website", "https://zoeleblanc.com/is310-computing-humanities-2024/"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "themes/alchemy"
THEME_CSS_OVERRIDES = ['theme/css/oldstyle.css']

def process_order(metadata):
    if 'sortorder' in metadata:
        metadata['sortorder'] = int(metadata['sortorder'])

ARTICLE_METADATA_PROCESSORS = {
    'sortorder': process_order,
}

PAGE_ORDER_BY='sortorder'

STATIC_PATHS = ['images', 'files']