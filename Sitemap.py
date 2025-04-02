#!/usr/bin/env python

import os
import json
import sys
import datetime
from xml.etree import ElementTree

def get_post_last_modification_date(file_name):
    """
    Returns the last modification date of the given file as an ISO 8601 formatted string.
    """
    try:
        file_path = os.path.join(output_directory, "posts", file_name)
        # Get the last modification time of the file
        timestamp = os.path.getmtime(file_path)
        # Convert the timestamp to a datetime object
        last_mod_date = datetime.datetime.fromtimestamp(timestamp)
        # Return the date in ISO 8601 format
        return last_mod_date.isoformat()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def get_posts_from_index(output_directory):
    """
    Reads the index.json file located in output_directory/posts and returns
    the list blog posts.
    """
    index_file_path = os.path.join(output_directory, "posts", "index.json")
    
    try:
        with open(index_file_path, "r", encoding="utf-8") as file:
            file_list = json.load(file)
        return [(os.path.splitext(file_name)[0], get_post_last_modification_date(file_name)) for file_name in file_list if file_name.endswith(".md")]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading index.json: {e}")
        return []

def generate_sitemap(domain, output_directory):
    root = ElementTree.Element("urlset")
    root.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
    
    posts = get_posts_from_index(output_directory)
    for post, last_modified in posts:
        url_elem = ElementTree.SubElement(root, "url")

        # <loc>: URL of the page (in absolute format)
        loc_elem = ElementTree.SubElement(url_elem, "loc")
        loc_elem.text = domain + "/posts/" + post

        # <lastmod>: Last modification date
        lastmod_elem = ElementTree.SubElement(url_elem, "lastmod")
        lastmod_elem.text = last_modified

        # Optional elements, but could be added later
        # <changefreq>: Change frequency, to help search engines determine how often a page should be recrawled (optional)
        # <priority>: Priority (optional)
    tree = ElementTree.ElementTree(root)
    tree.write(os.path.join(output_directory, "sitemap.xml"), encoding="utf-8", xml_declaration=True)

    
if __name__ == "__main__":
    print("Generating sitemap.xml")
    domain = sys.argv[1]
    output_directory = os.path.join(os.path.dirname(__file__), sys.argv[2], "publish", "wwwroot")
    generate_sitemap(domain, output_directory)