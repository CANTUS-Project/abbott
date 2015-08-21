Abbott
======

*Abbott* is a Python 3.4 implementation of a server for the Cantus API.

[![Build Status](https://api.travis-ci.org/CANTUS-Project/abbott.svg?branch=master)](https://travis-ci.org/CANTUS-Project/abbott)

License
-------

*Abbott* is copyrighted according to the terms of the GNU AGPLv3+. A copy of the license is held in
the file called "LICENSE."

Repository Layout
-----------------

The ``abbott`` directory contains program code. The simplest way to run *Abbott* is to execute this
directory as a Python module.

The ``scripts`` directory contains scripts used to convert between various formats, and tests for
those scripts. These are primarily for moving data from the Drupal to the Solr servers.

The ``tests`` directory contains unit and integration tests for the program code.

The ``test_client`` directory contains a simple HTML Web page to use when testing *Abbott*.

The ``packaging`` directory contains files relevant to deploying *Abbott*, such as a sample
configuration file, *systemd* unit files, and an alternative startup script.

Install for Development
-----------------------

Clone this git repository:

    $ git clone https://github.com/CANTUS-Project/abbott.git

Create and activate a new virtualenv:

    $ pyvenv */your/path/here*
    $ source */your/path/here/bin/activate*

Install the development requirements:

    $ pip install -r requirements-devel.txt

Install ``abbott`` itself. This ensure the ``abbott`` module is importable in the interpreter.

    $ pip install -e .

The test suite uses the ``pytest`` package. To run the test suite, ensure your venv is activated,
then issue the following command from the "abbott" root directory:

    $ py.test

``pytest`` is quite clear in its output, so you should not have to guess whether the tests passed.
To run a test instance of *Abbott*, run this command from the "abbott" root directory:

    $ python abbott

Install for Deployment: Preferred Way
-------------------------------------

If your deployment system uses *systemd*, this is the preferred method of deployment. If not, you
may use the alternative described below, but it isn't great.

Install as for development, but use the ``requirements-deploy.txt`` file.

After you install *Abbott*, you may wish to test its functionality:

    $ python setup.py test

Now do the stuff to install the unit files and whatever...

- edit the ``Environment=PATH=`` and ``ExecStart=`` lines in abbott.service, so they agree with
  the paths you used just above
- unit files (abbott.service, solr.service) must be installed to /usr/lib/systemd/system directory
- then # systemctl daemon-reload
- then # systemctl start abbott
- and  # systemctl enable abbott
- and Solr will be taken care of automatically
- must have users named "abbott" and "solr" with their proper groups|
- Solr must be installed to /usr/local/ as specified in the unit file
- Solr's database must be installed to /var/db/solr/ as specified in the unit file
- /var/db/solr/* must be set to "solr:solr" as owner
- Abbott must be installed to /usr/local/ as specified in the unit file
- Abbott's virtualenv must also be installed under /usr/local/
- make the /run/abbott directory, and "chown" it to abbott:abbott
- "chown solr:solr" on the Solr logs directory, /usr/local/solr-4.10.4/example/logs (or similar)
    - and /usr/local/solr-4.10.4/example/solr-webapp
    - NB: this is a sign I'm not deploying Solr correctly
    - TODO: increase the wait-time during restart for Solr

Install for Deployment: Alternative Way
---------------------------------------

Please note that THIS IS NOT THE RECOMMENDED WAY TO DEPLOY *ABBOTT*. If your deployment system uses
*systemd*, we strongly recommend deploying *Abbott* with *systemd* as described above.

Install as for development, but use the ``requirements-deploy.txt`` file.

After you install *Abbott*, you may wish to test its functionality:

    $ python setup.py test

Now customize the included ``start_abbott`` script from the ``packaging`` directory.

Now start the Solr server.

Now run the included ``start_abbott`` script from the ``packaging`` directory---no need to activate
the virtualenv beforehand.
