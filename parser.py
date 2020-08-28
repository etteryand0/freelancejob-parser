# Разработчик - Сергин Сергей

class Parser:
    def __init__(self):
        # init()
        # This function will define cookies 

        # import BeautifulSoup to parse html-code
        from bs4 import BeautifulSoup
        # globalize BeautifulSoup
        self.BeautifulSoup = BeautifulSoup
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

        # Parser() initialized successfuly


    def grab_pages_count(self):
        # pages_count()
        # This function will define pages count by accessing last page`s footer
        
        # There is something interesting about /projects/pN/
        # If N is not exist, then site would render last existing page
        # So let`s use this phenomen
        # define tottaly non existing page id
        tottaly_non_existing_page_id = 999999999999
        # request that tottaly non existing page. Site will return last existing page
        page_html = self.session.get(self.url_template.format(tottaly_non_existing_page_id)).text

        # let`s grab that pages id to get pages count
        # But first convert html to BeautifulSoup
        soup = self.BeautifulSoup(page_html,
                                  'html.parser')
        # first search for <ul class="pagination"></ul>, where page_count`s box is contained
        # then search for page_count`s box (<li></li>). It is last ([-1])
        # finally grab text of that box - pages_count
        self.pages_count = soup.find('ul',
                                     class_='pagination').find_all('li')[-1].text
        
        # Because we`ve grabed html code, it is string. So, let`s convert pages count to integer
        self.pages_count = int(self.pages_count)
        
        # grab_pages_count() ran successfuly
        return True
        

    def curl_pages(self):
        # curl_pages()
        # This function will grab list of html pages projects

        for page_id in range(1,
                             self.pages_count
                             + 1):
            # grab every page

            # request page html via our session
            page_html = self.session.get(self.url_template.format(page_id)).text
            # convert html to BeautifulSoup
            soup = self.BeautifulSoup(page_html,
                                      'html.parser')

            # get list of projects in page_id (N) page
            projects_html = soup.find_all('div',
                                          class_='x17')
            # append projects html to global variable
            self.projects_html.append(projects_html)
            
            # curl_pages() ran successfuly
            return True


# Let`s run our Parser app
# first, initialize it
Parser = Parser()
# now get pages count
Parser.grab_pages_count()
# curl pages html
Parser.curl_pages()

