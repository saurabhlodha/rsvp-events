from dotenv import load_dotenv
import os
from services.meetup_service import MeetupService
from services.luma_service import LumaService
from services.event_manager import EventManager

def main():
    load_dotenv()
    
    # Initialize services
    meetup_service = MeetupService(
        email=os.getenv('MEETUP_EMAIL'),
        password=os.getenv('MEETUP_PASSWORD'),
        location=os.getenv('MEETUP_LOCATION')
    )
    
    luma_service = LumaService(
        email=os.getenv('LUMA_EMAIL'),
        password=os.getenv('LUMA_PASSWORD')
    )
    
    event_manager = EventManager(meetup_service, luma_service)
    
    try:
        # Initialize browser sessions
        meetup_service.initialize()
        # luma_service.initialize()
        
        # Fetch all events
        events = event_manager.get_all_events()
        print("Found events:", events)
        
        # Example: RSVP to a specific event
        # event_manager.rsvp_to_event(event_id="example-id", platform="meetup")
        
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        meetup_service.cleanup()
        luma_service.cleanup()

if __name__ == "__main__":
    main()