from talon import Module, Context, cron, actions

mod = Module()

ctx = Context()
ctx.matches = r"""
app: chrome
"""

@ctx.action_class("user")
class UserActions:
    def noise_buzz_start():
        actions.mouse_click(2)





