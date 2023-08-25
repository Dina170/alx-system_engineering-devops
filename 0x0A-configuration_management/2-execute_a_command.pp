# create a manifest that kills a process named killmenow.

exec { 'kill_process':
  command  => 'pkill killmenow',
  provider => 'shell',
  path     => '/usr/bin/:/usr/local/bin/:/bin/'
}
