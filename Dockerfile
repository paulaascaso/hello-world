FROM odoo:14.0

LABEL MAINTAINER Paula Ascaso <ascasopaula@gmail.com>
USER root

RUN pip3 install dropbox
