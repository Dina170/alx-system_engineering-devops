# Fix Apache returning a 500 error
exec {'fix-name':
  command => 'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php',
  path    => '/bin',
}
