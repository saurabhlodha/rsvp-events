from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from .web_service import WebService

class LumaService(WebService):
    def __init__(self, email: str, password: str):
        super().__init__()
        self.email = email
        self.password = password
        
    def initialize(self):
        """Initialize the Chrome WebDriver with Selenium"""
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.login()
    
    def login(self):
        """Login to Lu.ma"""
        self.driver.get('https://lu.ma/signin')
        
        # Wait for and fill in email
        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"]'))
        )
        email_field.send_keys(self.email)
        
        # Fill in password
        password_field = self.driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
        password_field.send_keys(self.password)
        
        # Click login button
        login_button = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        login_button.click()
        
        # Wait for navigation
        WebDriverWait(self.driver, 10).until(
            EC.url_changes('https://lu.ma/auth/login')
        )
    
    def get_events(self):
        """Fetch events from Lu.ma"""
        self.driver.get('https://lu.ma/search')
        
        events = []
        event_elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-event-card]'))
        )
        
        for element in event_elements:
            event = {
                'id': element.get_attribute('data-event-id'),
                'title': element.find_element(By.CSS_SELECTOR, 'h3').text,
                'date': element.find_element(By.CSS_SELECTOR, '.event-date').text,
                'platform': 'luma'
            }
            events.append(event)
            
        return events
    
    def rsvp_to_event(self, event_id: str):
        """RSVP to a specific Lu.ma event"""
        self.driver.get(f'https://lu.ma/e/{event_id}')
        
        rsvp_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="rsvp-button"]'))
        )
        rsvp_button.click()
        return True