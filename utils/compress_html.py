from bs4 import BeautifulSoup, Comment
import os

def condense_html(filename, output_filename):
    with open(filename, 'r', encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    # remove redundant HTML tags
    for element in soup(['style', 'script', '[document]', 'head', 'title', 'meta', 'link']):
        element.decompose()

    # remove html comments
    for element in soup(text=lambda text: isinstance(text, Comment)):
        element.extract()
    
    # output only meaningful tags
    useful_tags = ['table', 'p', 'a', 'div', 'form', 'input', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span']
    output_html = [tag.prettify() for tag in soup.find_all(useful_tags)]
    
    # convert the list of tags to a string
    output_html_str = "".join(output_html)


    with open(os.path.join('utils/temp/output_filename'), 'w', encoding="utf-8") as f:
        f.write(output_html_str)

# call the function with the input HTML filename and output filename
condense_html('input.html', 'output.html')
