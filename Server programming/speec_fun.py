import sys
sys.path.append("/home/crazypikachu/linux-based-project/Voice_based_commands")
from voice_recognize import voice_recognize
def voice_location():
    voice1=voice_recognize()
    if "remote" in voice1:
        return 'remote'
        
    elif "local" in voice1:
        return 'local'
        
    else :
        voice_location()
location=voice_location()
print(location)