from typing import List, Dict
from .web_service import WebService

class EventManager:
    def __init__(self, meetup_service: WebService, luma_service: WebService):
        self.meetup_service = meetup_service
        self.luma_service = luma_service
    
    def get_all_events(self) -> List[Dict]:
        """Get events from both platforms"""
        meetup_events = self.meetup_service.get_events()
        luma_events = self.luma_service.get_events()
        return meetup_events + luma_events
    
    def rsvp_to_event(self, event_id: str, platform: str) -> bool:
        """RSVP to an event on the specified platform"""
        if platform == "meetup":
            return self.meetup_service.rsvp_to_event(event_id)
        elif platform == "luma":
            return self.luma_service.rsvp_to_event(event_id)
        else:
            raise ValueError(f"Invalid platform: {platform}")