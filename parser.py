# Разработчик - Сергин Сергей

class Parser:
    def __init__(self):
        # init()
        # This function will define cookies 

        # import BeautifulSoup to parse html-code
        from bs4 import BeautifulSoup
        # import requests to send GET requests
        import requests
        
        # First of all we should declare and define some necessary variables
        # define template of url. {0} is dynamic - from 1 to n pages
        self.url_template = 'https://freelancejob.ru/projects/p{0}/'
        # declare global list of project pages
        self.projects_html = []

        # define session to set PROJECTS cookie
        self.session = requests.session()
        # create cookie PROJECT=programmirovanie via requests
        cookie_PROJECTS = requests.cookies.create_cookie(domain = 'www.freelancejob.ru', 
                                                         name = 'PROJECTS',
                                                         value = 'programmirovanie')
        # set cookie to our session
        self.session.cookies.set_cookie(cookie_PROJECTS)

        # GET first page`s HTML with our session
        page_html = self.session.get(self.url_template.format('1')).text
        # convert html to BeautifulSoup
        soup = BeautifulSoup(page_html,
                             'html.parser')
        # by the way, let`s append our first list to self.projects_html
        self.projects_html.append(soup.find_all('div', 
                                                class_='x17'))
        print(self.projects_html)

        # cookie - PROJECTS=programmirovanie
        # self.session.get(self.url_template.format(page))



# run our Parser app
Parser = Parser()
Parser.curl_projects()
