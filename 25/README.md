## [Bite 25. No promo twice, keep state in a class](https://codechalleng.es/bites/25/)

Good luck and please share you code in the Bite forums upon completion.

For questions use [our Slack](https://pybites.slack.com/archives/C6BGDQQ3B) (no spoilers please).

Check out our full catalogue of Bites of Py [here](https://codechalleng.es/bites/catalogue).

Enjoy and keep calm and code in Python!

------------------

In this bite a real world scenario: _PyBites has a growing set of Bites and gives away promos_. They choose a Bite randomly but don't want to choose the same one again.

Hence you are provided with a `BITES` constant and a `bites_done` set that gets passed into the class via its constructor. Complete the methods in the Promo class:

1. `_pick_random_bite` is a helper (`_` here means private) that picks a randomly available Bite. When no more Bites are available raise a `NoBitesAvailable` (provided).
2. `new_bite` should use this helper and update `self.bites_done` (_it keeps state_, the reason we used a class here).

See also the tests. We hope you learn a thing or two. Enjoy!
