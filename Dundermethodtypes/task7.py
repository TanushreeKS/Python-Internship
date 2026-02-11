class Session:
    def __del__(self):
        print("Session Ended")


s = Session()
del s
