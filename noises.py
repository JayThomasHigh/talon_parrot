from talon import Module, Context, cron, actions, ctrl

mod = Module()

state = {}
cron_jobs = {}
callbacks = {}

ctx = Context()
ctx.matches = r"""
mode: command
mode: dictation
"""


@ctx.action_class("user")
class UserActions:

    def noise_cluck():
        actions.user.mouse_click("right")
    
    def noise_smooch():
        actions.user.mouse_click("middle")

    #def noise_shush_start():
        #actions.user.mouse_scroll_speed_set(1)
    #    actions.user.mouse_scrolling("up")

    #def noise_shush_stop():
    #    actions.user.mouse_scroll_stop()

    #def noise_hiss_start():
        #actions.user.mouse_scroll_speed_set(10)
    #    actions.user.mouse_scrolling("down")

    #def noise_hiss_stop():
    #    actions.user.mouse_scroll_stop()

    def noise_buzz_start():
        actions.mouse_drag(0)

    def noise_buzz_stop():
        actions.user.mouse_release(0)



@mod.action_class
class Actions:
    def noise_debounce(name: str, active: bool):
        """Start or stop continuous noise using debounce"""
        if name not in state:
            state[name] = active
            cron_jobs[name] = cron.after("80ms", lambda: callback(name))
        elif state[name] != active:
            cron.cancel(cron_jobs[name])
            state.pop(name)

    def noise_pop():
        """Noise pop"""

    def noise_cluck():
        """Noise cluck"""

    def noise_smooch():
        """Noise smooch"""

    def noise_shush_start():
        """Noise shush started"""

    def noise_shush_stop():
        """Noise shush stopped"""

    def noise_hiss_start():
        """Noise hiss started"""

    def noise_hiss_stop():
        """Noise hiss stopped"""

    def noise_buzz_start():
        """Noise buzz started"""

    def noise_buzz_stop():
        """Noise buzz stopped"""
    
    def noise_ooo():
        """Noise oooo started"""

    def noise_ooo_start():
        """Noise oooo started"""

    def noise_ooo_stop():
        """Noise ooo stopped"""

    def noise_err_start():
        """Noise err started"""

    def noise_err_stop():
        """Noise err stopped"""




def last_command_is_sleep():
    cmd, _ = actions.core.last_command()
    return cmd.script.code.startswith("user.talon_sleep()")


def callback(name: str):
    active = state.pop(name)
    callbacks[name](active)


def on_shush(active: bool):
    if active:
        print("shush:start")
        actions.user.noise_shush_start()
    else:
        print("shush:stop")
        actions.user.noise_shush_stop()


def on_hiss(active: bool):
    if active:
        print("hiss:start")
        actions.user.noise_hiss_start()
    else:
        print("hiss:stop")
        actions.user.noise_hiss_stop()

def on_buzz(active: bool):
    if active:
        print("buzz:start")
        actions.user.noise_buzz_start()
    else:
        print("buzz:stop")
        actions.user.noise_buzz_stop()


def on_ooo(active: bool):
    if active:
        print("ooo:start")
        actions.user.noise_ooo_start()
    else:
        print("ooo:stop")
        actions.user.noise_ooo_stop()

def on_err(active: bool):
    if active:
        print("rrr:start")
        actions.user.noise_err_start()
    else:
        print("err:stop")
        actions.user.noise_err_stop()


callbacks["shh"] = on_shush
callbacks["hiss"] = on_hiss
callbacks["buzz"] = on_buzz
callbacks["ooo"] = on_ooo
callbacks["err"] = on_err