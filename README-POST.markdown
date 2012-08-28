Mapgears labs - Hyde 0.8 - How to add new posts ?
==================================================

This document is a step-by-step tutrial and documentation for adding new posts.


site.yaml
----------
This is the main configuration file used by Hyde. Among its various purposes, it
serves as a global point of entry for all pages using the 'context/data'
property. We use it to define external 'links' and 'emails'. Instead of adding
them directly in your pages, add them in site.yaml first, then refer them in
your page.

create a new post
------------------
The easiest way is to copy an existing one an rename it :

    cp content/archive/pim.html content/archive/mypost.html

The part contains the page global informations, which are pretty much
self-explanatory. Edit each line accordingly.

* id: (optional, string) The id for this article. Useful when the file name of
  the same article translated in an other language is not the same. This allow
  the generator to connect both pages and automatically create the link to the
  other page accordingly. If both page names are the same, you don't need to
  use an id.
* created: (mandatory, timestamp string) The creation timestamp of the post.
  Used by the time sorter.
* description: (mandatory, string) Description of the post
* title: (mandatory, string) The post title being displayed
* tags: (mandatory, list) A list of tags for this post
* live: (mandatory, string) The url to the live demo
* preview: (mandatory, string) The image to use as a preview to display for this
  post. The path is relative to the content/media/images directory.
* thumbnail: (recommended, string) The image to use as a thumbnail to display in
  the archives for this post. The path is relative to the content/media/images
  directory. If not set, the preview image is used with its dimension shrinked.

    ---
    id: pim
    title: PIM
    description: >
        Collect information about features in clusters.
    created: !!timestamp '2009-11-17 15:00:00'
    tags:
        - mapserver
        - openlayers
        - openstreetmap
    live: http://dev4.mapgears.com/ebdata/demo-pim/
    preview: pim-preview.jpg
    thumbnail: 
    ---
    
Next are the internal links. You could skip using those completely and use
html instead, but I find it cleaner to structure the links that way. The last
two ones don't need to be changed.
    
    [mapserver]:     {{links.mapserver}}
    [openlayers]:    {{links.openlayers}}
    [openstreetmap]: {{links.openstreetmap}}

    [live]:    {{resource.meta.live}}
    [preview]: {{media_url('images/'~resource.meta.preview)}}
    
After that comes the 'excerpt' part, which is displayed as a summary text in
the archive main page and on the main page when it's the latest post. I haven't
found a way to use a variable there, so I copy the content of the 'description'
above here.
    
    {% mark excerpt -%}
    Collect information about features in clusters.
    {%- endmark %}

The next part doesn't need to be edited. Leave it as it is. Basically, it
includes the image set a 'preview' (above) and a link to the 'live' demo.
    
    <p><a href="{{resource.meta.live}}">
    ![Preview][preview]
    </a></p>

Finally comes the post content. You can use the markdown syntax, pure html or.
combine both. It's up to you.

You can add external links that refers to the technologies used in the demo.

    This demo features an OpenLayers map showing vector features coming from a
    remote server, which are clustered on client-side when too close to each
    other. A click on a feature shows a popup with aggregated information if it
    contains clusters, or a complete detail if it only contains one.

    The base maps come directly from OpenStreetMap server. The features are
    obtained using the OGC WFS protocol, with MapServer.

    * See the [Live demo][live] in action
    * Learn more about [MapServer][mapserver]
    * Learn more about [OpenLayers][openlayers]
    * Learn more about [OpenStreetMap][openstreetmap]

Once you're done, deploy and visit to see your changes. Add, commit and push
your changes once everything looks okay.
    

Other notes
------------
Since the files edited are text files, make sure you make them clean and as
human-readable as possible.