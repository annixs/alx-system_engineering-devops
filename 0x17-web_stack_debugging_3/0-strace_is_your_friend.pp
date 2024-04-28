<<<<<<< HEAD
# Fixes bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`.

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
=======
# Fix 500 error when a GET HTTP method is requested to Apache web server

exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
>>>>>>> 0b84059b007b57f69ef262fb7efdaf900dfb7386
