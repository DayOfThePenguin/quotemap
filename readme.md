#Quote Map (CURRENTLY BROKEN)
Use: Keep track of interesting things you discover while reading

Quotemap is a series of python modules that allow you to keep track of quotes and thoughts as you read books or other media.

###Directory Structure:

* /datatypes : modules that contain a class specifying how to interpret a particular kind of data
* /ui : modules that write the user interface to the terminal
* /utilities : modules that perform tasks for other modules
* /utilities/io : modules that abstract json io tasks and directory navigation

###Dependencies:

* Uses python 3, certain things (e.g. input) are not yet working for both python 2

Not reading a book or any of the media already defined in the /datatypes folder? It's quite simple to define a new media type. For example, if I wanted to create a new datatype named "movie"...

1. Create a new folder in /datatypes
```text
    /quotemap/datatypes >> mkdir movie            # Creates directory 'movie'
    /quotemap/datatypes >> cd movie               # Changes to 'movie'
    /datatypes/movie >>
```

###The dream:

* Build a web app with a highlight-enabled embedded pdf viewer like [Mendeley](http://www.mendeley.com)
* Let you turn your references into a gigantic map like [Docear](http://www.docear.com) so you can visualize the connections between everything you read, tracking common themes and the evolution of interesting ideas using [json-ld](http://json-ld.org/index.html) to persist data and [networkx](http://networkx.github.io/) to do make the graph operations easier.

```text
Comments, questions, concerns?  I'd be happy to hear from you; you can
reach me at <colin.dablain@gmail.com>
(C) 2014-2015 Colin Dablain
```
