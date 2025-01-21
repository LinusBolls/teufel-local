import json

class SpeakerControls:
    def __init__(self):
        self._state = {
            'channel-1:volume': 50,
            'channel-2:volume': 50
        }
    
    def set_value(self, key, value):
        if key not in self._state:
            raise ValueError(f'Input {key} not found')
        
        if not isinstance(value, int) or value < 0 or value > 100:
            raise ValueError(f'Value {value} must be a number between 0 and 100')
        
        self._state[key] = value
        
    def __str__(self):
        return json.dumps({ 'input': self._state})
    
speaker_controls = SpeakerControls()