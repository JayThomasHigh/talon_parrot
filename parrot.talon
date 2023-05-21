not mode: sleep
-

#parrot(pop):
#    user.debug("pop {power}")
#    user.noise_pop()

#parrot(cluck):
#    user.debug("cluck {power}")
#    user.noise_cluck()

parrot(shh):              user.noise_debounce("shh", true)
parrot(shh:stop):         user.noise_debounce("shh", false)

parrot(hiss):               user.noise_debounce("hiss", true)
parrot(hiss:stop):          user.noise_debounce("hiss", false)
