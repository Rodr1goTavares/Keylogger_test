from action.logger import Logger


class Main:
    @staticmethod
    def run():
        print("[Running]")
        Logger.start()


Main.run()
