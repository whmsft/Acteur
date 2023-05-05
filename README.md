# Acteur
Acteur (Dutch: Actor): Create videos from text

say, you have a file:
```js
require "config" @Window
require "time" @Timeline
.init() {
  $config.window {
    width: 512;
    height: 512;
    background: #0084FF;
    foreground: #FFFFFF;
    font: "Consolas 14";
  }
  #length: "00:10";
}
.objects {
  !hello_world: {
    text: "Hello World";
  }
}
.timeline {
  if $time('00:01') {
    !hello_world.show(10, 20)
  }
}
```
and this will just make a 10 second video, with a object `hello_world`, which will display text `Hello World` at `x=10` and `y=20` on with timeline at `00:01`

<i>\*\* This is just a conceptual design of code, things might change with difficulty...</i>
