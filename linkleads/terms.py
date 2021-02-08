terms = [
    "Home Improvement",
    "Construction",
    "Roofing",
    "Cleaning",
    "Lawn",
    "Landscape",
    "landscaping",
    "tree",
    "land",
    "Painting",
    "Plumbing",
    "electrical",
    "Contractor",
    "flooring",
    "Renovations",
    "powerwashing",
    "pressure",
    "Fencing",
    "Fence",
    "Concrete",
    "Masonry",
    "Brick",
    "Service",
    "Services",
    "LLC",
    "INC",
    "repair",
    "repairs",
    "asphalt",
    "builders",
    "HVAC",
    "heating",
    "Air conditioning",
    "Remodeling",
    "Remodel",
    "excavation",
    "lawn care",
    "window",
    "Tree Service",
]


searchengines = {
    "google": ["https://www.google.com/", "q"],
    "bing": ["https://www.bing.com/", "q"],
    "yahoo": ["https://www.yahoo.com/search?", "p"]
}

# Should the wix have a site parameter.. try it w and without before asking
searchmodel = {
    "wix": ['', 'intext:Proudly created with Wix.com', '"construction"'],
    "bbb": ['inurl:bbb.org',  '"Accredited Since:2/5/2021"',  'intitle:Construction'],
    "google": ['Page created - February 5, 2021',  "site:facebook.com", 'intitle:"Home Improvement"']
}
