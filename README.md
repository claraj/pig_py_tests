### Pig, the dice game, with tests.


Play game from the root directory with

```
python -m pig.game
```

or 

```
python playpig.py
```


Run tests from the pig_dice directory by typing

```
python -m unittest

```

Notice that there's a \_\_init\_\_.py file in the pig directory so it can be
imported as a module to the tests.

And there's a \_\_init\_\_.py file in the test directory, so unittest's test
discovery can find all the tests in both the files in that directory and
run them all.
