# manifest to kill a running process
exec {'killall':
  command => 'pkill killmenow',
  path    => ['/bin', '/sbin', '/usr/bin', '/sbin/usr']
}
