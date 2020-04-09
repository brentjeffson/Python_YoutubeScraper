import re
import json

def __parse_source_script(html):
        src_script_pattern = "<script\s?>var\sytplayer\s=\sytplayer\s\|\|\s\{\};ytplayer.config\s=\s.+</script>"
        searched = re.search(src_script_pattern, html)
        if searched:
            parsed_html = searched.group()
            return parsed_html
        return None        
        
def parse_sources(html):
    parsed_source_script = __parse_source_script(html)
    # find the sources using regex
    pattern = r'formats\\":(.+)(}]|}]}),\\"(playerAds|dashManifestUrl)'
    searched = re.search(pattern, parsed_source_script)

    # do some cleaning
    src = searched.groups()[0]
    clean_src = src.replace("\\u0026", "&").replace('\\', '')#.replace('[{', '').replace('}}]', '')

    # split cleaned src
    url_info = []
    for index, p in enumerate(re.split("},{", clean_src)):   
        
        # remove excess closing tags
        if index == 0: 
            p = p.replace("[{", "")
        elif index == len(re.split("},{", clean_src))-1:
            p = p.replace("}]}", "")
    
        codecs_value = re.search(r"codecs=\"([\w,\s.\-?_]+)\"", p).groups()[0]
        new_str = re.sub(r'codecs=".+"",', f"codecs={codecs_value}\",", p)
        
        # convert to dictionary, add to list           
        url_info.append(json.loads("{" + new_str + "}"))
    return url_info