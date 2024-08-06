from enum import Enum


class Provider(Enum):
    """Enum for provider types."""
    LOCAL = "local"
    GOOGEL = "google"
    TWITTER = "twitter"
    FACEBOOK = "facebook"
