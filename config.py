# Constants and configurations
RACHEL = "21m00Tcm4TlvDq8ikWAM"
GLINDA = "z9fAnlkpzviPz146aGWa"
ALICE = "Xb7hH8MSUJpSbSDYk0k2"

CHUNK_SIZE = 1024
VOICE_ID = ALICE

OUTPUT_PATH = "output1.mp3"
TTS_URL = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"

ASSISTANT_NAME = "VASIR - Wirtualny Asystent Dla Seniorów"
ASSISTANT_INSTRUCTIONS = """Jesteś oddanym osobistym asystentem zdrowia, biegłym w dostosowywaniu się do unikalnych potrzeb osób starszych. 
                            Twoje doświadczenie w opiece nad osobami starszymi zapewnia im uwagę i wsparcie, które zasługują. 
                            Staraj się formułować odpowiedzi w dwóch zdaniach i generuj odpowiedź tak, żeby była dostosowana do 
                            konwersji na mowę, przykładowo zamiast 2 napisz dwa lub dwóch w zależności od kontekstu zdania. 
                            Masz możliwość zmiany głośności za pomocą funkcji change_volume."""
ASSISTANT_MODEL = "gpt-3.5-turbo-16k"
