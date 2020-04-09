import pytest
import youtubescraper as yts

with open("res/youtube.html") as f:
    HTML = f.read()

def test_search_source_script_searched_successfully():
    pass

def test_parse_video_sources():
    srcs = yts.parse_sources(HTML)
    for src in srcs:
        if "video/mp4" in src["mimeType"]:
            print(f"({src['itag']}):{src['qualityLabel']} - {src['url']}")

def test_clean_source_mime():
    pass

test_search_source_script_searched_successfully()
test_parse_video_sources()
