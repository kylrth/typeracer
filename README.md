# typeracer

These are some Python scripts that scrape your results from [typeracer](https://typeracer.com) and create a GIF plotting your results over time. Run the following to generate the example GIF below:

```sh
./run.sh kylrth
```

![GIF of typing speed for user kylrth](example.gif)

## dependencies

You need BeautifulSoup, Pandas, requests, and Plotly, plus ImageMagick for compiling the GIF.

## attribution

The plotting code was modified from [varkon256's repo](https://github.com/varkon256/typeracer-scraper).
