# this puppet manifest fixes too many open files error
exec { 'update ulimit for nginx':
  command => "/bin/echo ULIMIT='-n 5000' > /etc/default/nginx",
  path    => '/etc/default/nginx'
}

exec { 'restart server':
  command => '/usr/bin/sudo service nginx restart'
}
