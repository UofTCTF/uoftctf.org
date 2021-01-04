If you want to modify the original theme, the best way is copy the original theme file into the root folder, then modify it. In this way, hugo will overwrite the default with your own version.

For example, if you want to modify `index.html`, then copy `themes/terminal/layouts/_default/index.html` into `layouts/_default/index.html` and edit it.

To-do:

- [x] Write Github Action to automatically pull writeups
- [x] write hook to develop the website to the server
