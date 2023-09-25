not mode: sleep
-

.#parrot(pop):
#    user.debug("pop {power}")
#    user.noise_pop()

parrot(cluck):
    user.noise_cluck()

parrot(smooch):
    user.noise_smooch()


parrot(ooo):
    user.noise_ooo()


# parrot(ooo):               user.noise_debounce("ooo", true)
# parrot(ooo:stop):          user.noise_debounce("ooo", false)

parrot(shh):              user.noise_debounce("shh", true)
parrot(shh:stop):         user.noise_debounce("shh", false)
    
parrot(hiss):               user.noise_debounce("hiss", true)
parrot(hiss:stop):          user.noise_debounce("hiss", false)

parrot(buzz):               user.noise_debounce("buzz", true)
parrot(buzz:stop):          user.noise_debounce("buzz", false)

parrot(err):               user.noise_debounce("err", true)
parrot(err:stop):          user.noise_debounce("err", false)