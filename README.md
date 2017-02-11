# GIFSizeReader

This simple Python script fetches the height and width information of a GIF image in a simple memory-efficient manner.

Requires absolutely no dependencies as it uses only Python's built-in functions.

Q: Why is it memory efficient?

A: Regardless of the file size, every GIF file records its (logical) width and height within bytes 7 to 10.
So, instead of storing the entire file in memory, we just grab its first few bytes and no more.

Usage:
There is only one key function here, which is get_gif_size(FILENAME)

Ex:
```python
>>> import gif_size_reader
>>> gif_size_reader.get_gif_size('picture.gif')
{'Width': 435, 'Height': 343}
```
