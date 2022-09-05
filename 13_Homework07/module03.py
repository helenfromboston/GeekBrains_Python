def create_html():
    html = '<!DOCTYPE html>\n<html>\n  <head></head>\n  <body>\n    <h1>Телефонный справочник</h1>\n'
    with open('Phonebook.txt', encoding = 'UTF-8') as data:
        for line in data.readlines():
            html += '   <p>' + line.removesuffix('\n') + '</p>\n'
    html += '  </body>\n</html>'
    with open('Phonebook.html', 'w', encoding='UTF-8') as data:
        data.write(html)
    return html