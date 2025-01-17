# Manifest to configure an Ubuntu server with nginx

$conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root /var/www/html;
    index index.html index.htm;
    server_name _;
    location /hbnb_static {
        alias /data/web_static/current;
    }
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=dQw4w9WgXcQ;
    }
    error_page 404 /404.html;
}"

package { 'nginx':
  ensure   => present,
  provider => 'apt'
}

-> file { '/data':
  ensure  => 'directory'
}

-> file { '/data/web_static':
  ensure  => 'directory'
}
-> file { '/data/web_static/shared':
  ensure => directory
}

-> file { '/data/web_static/releases':
  ensure => directory
}

-> file { '/data/web_static/releases/test':
  ensure => directory
}

-> file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => 'Holberton School',
}

-> file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test',
}

-> exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

-> file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $conf
}

-> file { '/var/www/html':
  ensure => 'directory'
}

-> file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page\n"
}

-> exec { 'Start nginx':
  command  => 'service nginx restart',
  user     => 'root',
  provider => 'shell'
}
