import wikipediaapi
    wiki_wiki = wikipediaapi.Wikipedia('en')

    print("Page - Title: %s" % page_py.title)
    # Page - Title: Python (programming language)

    print("Page - Summary: %s" % page_py.summary[0:60])
    # Page - Summary: Python is a widely used high-level programming language for