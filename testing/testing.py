from read_and_write_json.write_data_to_file import write_data_to_file
from read_and_write_json.testingFunction import testing
from read_and_write_json.move_json_to_company_folder import move_json_to_company_folder
from read_and_write_json.find_and_move_comments import find_and_move_file

# company_name = "Apple Inc." 

# # write_data_to_file("no_primary_ticker.json", company_name)
# testing(company_name)
# destination_directory = '../seeking_alpha_split_testing_company_folder'
# file_path = '../seeking_alpha_split_testing_copy/folder_4/123.json'
# filename = '123.json'
# move_json_to_company_folder(destination_directory, file_path, company_name,filename)


# Example usage

# filename = "example.txt"
# search_directory = '../comments2/extracted'
# target_directory = "/path/to/target_directory"

# find_and_move_file(filename, search_directory, target_directory)
import re
import html

def clean_html(raw_html):
    # Remove HTML tags using a regex
    clean_text = re.sub(r'<.*?>', '', raw_html)
    print("clean_text1 is ",clean_text)
    
    # Decode HTML entities (e.g. &amp;, &#x2019;)
    clean_text = html.unescape(clean_text)
    
    # Replace unnecessary symbols like \n, \t etc.
    clean_text = clean_text.replace('\n', '').replace('\t', '').strip()
    
    return clean_text

# Sample HTML string
sample_html = '''
<p>This week\u2019s Tech.pinions podcast features Tim Bajarin and Bob O\u2019Donnell discussing the new Magic Leap mixed reality goggles, analyzing the Apple (<a href="https://seekingalpha.com/symbol/AAPL" title="Apple Inc.">AAPL</a>) iPhone battery performance controversy, and debating the potential impact of a future combination of MacOS and iOS.</p> 
<p><iframe src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/373202993&amp;color=%23ff5500&amp;&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;show_teaser=true&amp;visual=true" width="100%" height="300" scrolling="no"></iframe></p> 
<p><em>Disclaimer: Some of the author's clients are vendors in the tech industry.</em></p> 
<div class="before_last_paragraph-piano-placeholder"></div> 
<p><strong>Disclosure:</strong> None</p>
'''

# Clean the HTML string
cleaned_text = clean_html(sample_html)

# Print the result
print(cleaned_text)