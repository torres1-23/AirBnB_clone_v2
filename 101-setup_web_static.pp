# Manifest to configure an Ubuntu server with nginx

$conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
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
->
package { 'nginx':
  ensure   => present,
  provider => 'apt'
}
->
# create direcotries /data/web_static/shared/
file { '/data/web_static/shared':
  ensure => directory
}
->
# create direcotries /data/web_static/shared/
file { '/data/web_static/releases/test':
  ensure => directory
}
->
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => 'Holberton School',
  owner   => 'ubuntu',
  group   => 'ubuntu'
}
->
exec { 'symbolik link':
  command  => 'ln -sfn /data/web_static/releases/test/ /data/web_static/current',
  user     => 'root',
  provider => 'shell'
}
->
file { '/data':
  ensure  => directory,
  user    => 'ubuntu',
  group   => 'ubuntu',
  recurse => true
}
->
file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_conf
->
exec { 'Start nginx':
  command  => 'service nginx restart',
  user     => 'root',
  provider => 'shell'
}
