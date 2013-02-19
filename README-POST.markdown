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

    cp content/en/archive/staff-tracking.html content/en/archive/mypost.html

The part contains the page global informations, which are pretty much
self-explanatory. Edit each line accordingly.

* id: (optional, string) The id for this article. Useful when the file name of
  the same article translated in an other language is not the same. This allow
  the generator to connect both pages and automatically create the link to the
  other page accordingly. If both page names are the same, you don't need to
  use an id.
* author: (recommended, string) The author of the article
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

Here's an example :

    ---
    id: staff-tracking
    title: Staff Tracking
    description: >
        Monitor outdoor events staff using an interactive webmapping application
    author: Alexandre Dubé
    created: !!timestamp '2012-08-20 10:00:00'
    tags:
        - basemaps
        - extjs
        - geoext
        - imposm
        - mapserver
        - openlayers
        - openstreetmap
        - postgis
    live: http://labs.mapgears.com/staff-tracking/
    preview: staff-tracking-preview.jpg
    thumbnail: staff-tracking-thumb.jpg
    ---
    
Next are the internal links. You could skip using those completely and use
html instead, but I find it cleaner to structure the links that way. The last
two ones don't need to be changed.

    [basemaps]:      {{links.basemaps}}
    [extjs]:         {{links.extjs}}
    [geoext]:        {{links.geoext}}
    [imposm]:        {{links.imposm}}
    [mapserver]:     {{links.mapserver}}
    [openlayers]:    {{links.openlayers}}
    [openstreetmap]: {{links.openstreetmap}}
    [postgis]:       {{links.postgis}}

    [live]:    {{resource.meta.live}}
    [preview]: {{media_url('images/'~resource.meta.preview)}}

    Note: the link cannot include the character "-".
    
After that comes the 'excerpt' part, which is displayed as a summary text in
the archive main page and on the main page when it's the latest post. I haven't
found a way to use a variable there, so I copy the content of the 'description'
above here.
    
    {% mark excerpt -%}
    Monitor outdoor events staff using an interactive webmapping application
    {%- endmark %}

The next part doesn't need to be edited. Leave it as it is. Basically, it
includes the image set a 'preview' (above) and a link to the 'live' demo.
    
    <p><a href="{{resource.meta.live}}">
    ![Preview][preview]
    </a></p>

Finally comes the post content. You can use the markdown syntax, pure html or.
combine both. It's up to you.

You can add external links that refers to the technologies used in the demo.

    This webmapping application was built and used to monitor staff of outdoor
    events, such as concerts and shows, on an interactive map. It was designed
    to be used in a standard browser and tablets.

    Zones and staff icons are displayed on the map and refreshed every 15
    seconds, mimicking what it could look like when used during a real event.

    The client-side application uses OpenLayers, GeoExt and ExtJS as JavaScript
    frameworks. The base maps was created using MapServer Basemaps and Imposm
    using OpenStreetMap data. The features are obtained using the OGC WFS
    protocol, with MapServer and come from a PostGIS database. 

    The demo itself contains a "About this demo" button, which contains more
    information and technical details.

    * See the [Live demo][live] in action
    * Learn more about [Basemaps][basemaps]
    * Learn more about [ExtJS][extjs]
    * Learn more about [GeoExt][geoext]
    * Learn more about [Imposm][imposm]
    * Learn more about [MapServer][mapserver]
    * Learn more about [OpenLayers][openlayers]
    * Learn more about [OpenStreetMap][openstreetmap]
    * Learn more about [PostGIS][postgis]

Once you're done, deploy and visit to see your changes. Add, commit and push
your changes once everything looks okay. You can optionally create an entry
in the French (fr) archive as well.
    

Other notes
------------
Since the files edited are text files, make sure you make them clean and as
human-readable as possible.