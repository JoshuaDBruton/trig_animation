## Trigonometry Animation
Python implementation of the animation shown in the YouTube video [Beautiful Trigonometry](https://www.youtube.com/watch?v=snHKEpCv0Hk) uploaded by [Numberphile](https://www.youtube.com/user/numberphile).

### Usage
This was implemented in Python 3.6.10 and there is a requirements.txt file in the repository. Fork and clone the repository, install the requirements and then run:
```
python animation.py
```
Which should produce the following animation:
![Alt Text](animation.gif)

### Saving
[Installing imagemagick](http://docs.wand-py.org/en/0.3.5/guide/install.html) and uncommenting this line in "animation.py":
```
# animation.save('animation.gif', writer='imagemagick', fps=60)
```
will allow your to save you own .gif files.
