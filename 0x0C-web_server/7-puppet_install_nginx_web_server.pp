# install and configure an Nginx server
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => "
      server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm;

        server_name _;

        location /redirect_me {
          return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }

        location / {
          try_files \$uri \$uri/ =404;
        }
      }
    ",
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  exec { 'Hello World':
    command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
    provider => shell,
  }
