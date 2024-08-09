from enum import Enum


class UserStatus(Enum):
    """Enum for user status"""
    ACTIVE = 'verified'
    INACTIVE = 'inactive'
    PENDING = 'pending'
