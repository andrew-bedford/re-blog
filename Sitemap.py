#!/usr/bin/env python

import os
import json
import sys
import datetime
import time
from xml.etree import ElementTree
# from xml.etree.ElementTree import Element, SubElement, ElementTree


def get_post_last_modification_date(file_name):
    """
    Returns the last modification date of the given file.
    """
    try:
        file_path = os.path.join(output_directory, "posts", file_name)
        # Get the last modification time of the file
        timestamp = os.path.getmtime(file_path)
        # Convert the timestamp to a datetime object
        last_mod_date = datetime.datetime.fromtimestamp(timestamp)
        return last_mod_date.strftime("%Y-%m-%d")
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

def generate_rss_feed(domain, output_directory, feed_title="Andrew Bedford's Blog", feed_description=""):
    """
    Generates an RSS feed XML file from posts in index.json.
    """
    posts = get_posts_from_index(output_directory)

    rss = ElementTree.Element("rss")
    rss.set("version", "2.0")
    channel = ElementTree.SubElement(rss, "channel")

    title_elem = ElementTree.SubElement(channel, "title")
    title_elem.text = feed_title

    link_elem = ElementTree.SubElement(channel, "link")
    link_elem.text = domain

    desc_elem = ElementTree.SubElement(channel, "description")
    desc_elem.text = feed_description

    pub_date_elem = ElementTree.SubElement(channel, "pubDate")
    pub_date_elem.text = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())

    for post, last_modified in posts:
        item = ElementTree.SubElement(channel, "item")
        item_title = ElementTree.SubElement(item, "title")
        item_title.text = post

        item_link = ElementTree.SubElement(item, "link")
        item_link.text = f"{domain}/posts/{post}"

        item_guid = ElementTree.SubElement(item, "guid")
        item_guid.text = f"{domain}/posts/{post}"

        item_pub_date = ElementTree.SubElement(item, "pubDate")
        # Use last_modified as pubDate if available
        if last_modified:
            # Convert YYYY-MM-DD to RFC 2822 format
            dt = datetime.datetime.strptime(last_modified, "%Y-%m-%d")
            item_pub_date.text = dt.strftime("%a, %d %b %Y 00:00:00 +0000")
        else:
            item_pub_date.text = ""

    tree = ElementTree.ElementTree(rss)
    tree.write(os.path.join(output_directory, "rss.xml"), encoding="utf-8", xml_declaration=True)

    
if __name__ == "__main__":
    domain = sys.argv[1]
    output_directory = os.path.join(os.path.dirname(__file__), sys.argv[2], "publish", "wwwroot")
    print("Generating sitemap: " + os.path.join(output_directory, "sitemap.xml"))
    generate_sitemap(domain, output_directory)
    print("Generating feed: " + os.path.join(output_directory, "rss.xml"))
    generate_rss_feed(domain, output_directory)