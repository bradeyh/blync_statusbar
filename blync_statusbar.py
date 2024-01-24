import os

import blynclight
import rumps

class BlyncStatusBarApp(rumps.App):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.blync = blynclight.BlyncLight.get_light()

    @rumps.timer(0.1)
    def set_initial_state(self, sender):
        """Can't do this in __init__() or run() methods, since menu hasn't
        been created yet."""
        self.green(self.menu["🟢"])
        sender.stop()

    @rumps.clicked("⬤")
    def off(self, sender):
        self.blync.on = False
        self.update_checks(sender)

    @rumps.clicked("🔴")
    def red(self, sender):
        self.blync.color = (10, 0, 0)
        self.blync.on = True
        self.update_checks(sender)

    @rumps.clicked("🟡")
    def yellow(self, sender):
        self.blync.color = (30, 0, 10)
        self.blync.on = True
        self.update_checks(sender)

    @rumps.clicked("🟢", state=True)
    def green(self, sender):
        self.blync.color = (0, 0, 10)
        self.blync.on = True
        self.update_checks(sender)

    def update_checks(self, sender):
        for item in self.menu.values():
            if sender.title == item.title:
                item.state = True
            else:
                item.state = False

if __name__ == "__main__":
    BlyncStatusBarApp("Blync App", "🚦").run()
