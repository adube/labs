Mapgears labs - Hyde 0.8
==========================

This repository holds the template and content used in combinaison with Hyde 0.8
to build the [labs.mapgears.com] [4] web page.


Requirements
-------------
Before installing Hyde, make sure you have the following requirements :

* cssmin
* docutils
* php (for root redirection to lang directory)
* python
* python-django
* python-markdown
* python-pip
* python-virtualenv
* python-yaml

Install them using the following commands:

    sudo apt-get update && \
    sudo apt-get install python python-markdown python-yaml python-django \
    python-virtualenv python-pip
    sudo easy_install cssmin docutils

You'll also need a web server.  I used apache2 in which I enabled the following
modules :

* libapache2-mod-php5
* mod_rewrite
* mod_headers enabled


Hyde installation in a Virtual Python Environment
--------------------------------------------------
Instead of installing Hyde in your system, we'll use a Virtual Python
Environment builder call virtualenv.  Install it using the following command

    sudo apt-get update && sudo apt-get install python-virtualenv python-pip

then create a new virtual environment at the location you want and activate it :

    virtualenv ENV
    source ENV/bin/activate

Seeing (ENV) in your shell tells you you're inside the virtual environment:

    (ENV)adube@weltall:/opt/hyde$

In your newly installed Virtual Python Environment, install distribute then
Hyde from its Github repository: 

    easy_install -U distribute
    pip install -e git://github.com/hyde/hyde.git#egg=hyde

Hyde is now installed and ready to use :

    hyde --help


Apache configuration
---------------------
Make the deploy directory visible from your web server. I used Apache. In order
to allow the mod_rewrite to work properly, set the AllowOverride to All.

* The web page root is "/", so you'll need to define a VirtualHost.
* Make sure that mod_rewrite and mod_headers are enabled

Here's a example of configuration for Apache. Simply replace the values in []
accordingly :

    Listen [PORT]
    NameVirtualHost *:[PORT]

    <VirtualHost *:[PORT]>
      DocumentRoot [PATH_TO_ROOT_DIR]/deploy
    </VirtualHost>

    <Directory "[PATH_TO_ROOT_DIR]/deploy">
      AllowOverride All
      Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
      Order allow,deny
      Allow from all
    </Directory>

Deploy
-------
"Deploying" the site means to use a hyde command to rebuild the content to the
deploy directory.  

Activate your virtual environmnent, then go to your site directory and execute
the hyde gen command :

    source ENV/bin/activate
    cd /<PATH_TO_SITE>
    hyde gen


How to add a new demo ?
------------------------
See the README-POST.markdown file to learn how to add a new demo (post).


Special thanks
---------------
I'd like to thank Lakshmi Vyasarajan for his help and for all my questions 
he kindly answered: "Thank you, Lakshmi!".


References
-----------
* [Mapgears labs website] [4]
* [Hyde Github Repository] [1]
* [Hyde 0.8 official documentation] [2]
* [Hyde Google Groups Forum] [5]
* [Markdown syntax] [6]
* [Jinja Template Designer Documentation] [7]
* [Steve Losh article - moving from django to hyde] [3]

[1]: https://github.com/hyde/hyde/                                 "Hyde Github repository"
[2]: http://hyde.github.com/index.html                             "Hyde 0.8 official documentation"
[3]: http://stevelosh.com/blog/2010/01/moving-from-django-to-hyde/ "Steve Losh article about Hyde"
[4]: http://labs.mapgears.com                                      "Official website using this source"
[5]: https://groups.google.com/forum/#!forum/hyde-dev              "Hyde-dev Google Groups"
[6]: http://daringfireball.net/projects/markdown/syntax            "Markdown is a text-to-HTML conversion tool for web writers"
[7]: http://jinja.pocoo.org/docs/templates/                        "Jinja template engine for Python"