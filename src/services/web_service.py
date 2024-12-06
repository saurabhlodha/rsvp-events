from abc import ABC, abstractmethod

class WebService(ABC):
    def __init__(self):
        self.driver = None
    
    @abstractmethod
    def initialize(self):
        """Initialize the web service"""
        pass
    
    @abstractmethod
    def login(self):
        """Login to the service"""
        pass
    
    @abstractmethod
    def get_events(self):
        """Get events from the service"""
        pass
    
    @abstractmethod
    def rsvp_to_event(self, event_id: str):
        """RSVP to an event"""
        pass
    
    def cleanup(self):
        """Clean up resources"""
        if self.driver:
            self.driver.quit()