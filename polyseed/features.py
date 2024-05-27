from .constants import (
    FEATURE_BITS,
    FEATURE_MASK,
    INTERNAL_FEATURES,
    USER_FEATURES,
    USER_FEATURES_MASK,
    ENCRYPTED_MASK
)

reserved_features = FEATURE_MASK ^ ENCRYPTED_MASK

def make_features(user_features: int) -> int:
    return user_features & USER_FEATURES_MASK

def get_features(features: int, mask: int) -> int:
    return features & (mask & USER_FEATURES_MASK)

def is_encrypted(features: int) -> bool:
    return (features & ENCRYPTED_MASK) != 0

def polyseed_features_supported(features: int) -> bool:
    return (features & reserved_features) == 0

def polyseed_enable_features(mask: int) -> int:
    num_enabled = 0
    global reserved_features
    reserved_features = FEATURE_MASK ^ ENCRYPTED_MASK
    for i in range(USER_FEATURES):
        fmask = 1 << i
        if mask & fmask:
            reserved_features ^= fmask
            num_enabled += 1
    return num_enabled
