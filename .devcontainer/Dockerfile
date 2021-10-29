FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:git-core/ppa

RUN apt-get update && apt-get install -y software-properties-common \
&& add-apt-repository -y ppa:git-core/ppa && apt-get update \
&& apt-get -y install \
  software-properties-common \
  build-essential \
  git \
  unzip \
  wget \
  curl \
  locales \
  eslint \
  yarn \
  sudo \
  python3-pip \
  python3-venv

# hbget tool
RUN curl -s \
  https://fellowship.hackbrightacademy.com/materials/tools/hbget-remote \
  --output /usr/local/bin/hbget \
  && chmod +x /usr/local/bin/hbget

# Use a different source for Node since the Ubuntu repos are stuck on 10
RUN wget -O ~/node-source https://deb.nodesource.com/setup_14.x && \
  chmod +x ~/node-source && \
  ~/node-source && \
  apt -y install nodejs

# Install PostgreSQLv.13
RUN echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" \
  > /etc/apt/sources.list.d/pgdg.list \
  &&  wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
  && apt -y update \
  && apt -y install \
  postgresql-13 \
  libpq-dev

# Python dependencies
RUN pip3 install virtualenv \
  pylint \
  pytest

# FIXME
# Install manpages that *weren't* installed earlier, due to DEBIAN_FRONTEND
# being set to 'noninteractive'. We need this so summon manpages and
# --help works.

# Set name of default branch to 'main'
RUN git config --system init.defaultBranch main \
  && git config --global init.defaultBranch main

# Set locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Install LiveShare dependencies
RUN wget -O ~/vsls-reqs https://aka.ms/vsls-linux-prereq-script && chmod +x ~/vsls-reqs && ~/vsls-reqs

# Create 'hackbright' user
RUN groupadd --gid 1000 hackbright \
  && useradd --uid 1000 --gid hackbright --shell /bin/bash \
  --create-home --password "$(openssl passwd -1 hackbright)" hackbright \
  && echo hackbright ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/hackbright \
  && chmod 0440 /etc/sudoers.d/hackbright

# Since /home/hackbright was created before the 'hackbright' user,
# permissions won't be correct and it won't have a .bashrc file.
COPY .bashrc /home/hackbright
RUN chown -R hackbright /home/hackbright

USER postgres

RUN /etc/init.d/postgresql start && \
  psql --command "CREATE USER hackbright WITH SUPERUSER;" && \
  createdb -O hackbright hackbright

RUN echo "host    all    all    10.0.0.0/16    trust" >> /etc/postgresql/13/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/13/main/postgresql.conf

CMD ["/usr/lib/postgresql/13/bin/postgres", "-D", "/var/lib/postgresql/13/main", "-c", "config_file=/etc/postgresql/13/main/postgresql.conf"]