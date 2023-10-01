def get_hour(epoch_seconds):

    current_hour = (epoch_seconds / 3600) % 24
    
    return int(current_hour)

def get_minutes(epoch_seconds):

    current_minutes = (epoch_seconds / 60) % 60
    
    return int(current_minutes)

def get_seconds(epoch_seconds):

    current_seconds = (epoch_seconds % 3600) % 60

    return int(current_seconds)