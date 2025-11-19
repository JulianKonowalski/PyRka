from TTS import TTS

def data_callback() -> str:
    data = input("Please input tts sequence or press q to exit:\n")
    return data if data != "q" else None

if __name__ == "__main__":
    tts = TTS(data_callback)
    tts.run()