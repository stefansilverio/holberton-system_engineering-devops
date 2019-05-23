# file fixes bad php extension in /var/www/html/wp-settings.php
exec { '/var/www/html/wp-settings.php':
          command => '/bin/sed -i "137s/phpp/php/" \
	  /var/www/html/wp-settings.php',
          path    => '/var/www/html/wp-settings.php'
}
