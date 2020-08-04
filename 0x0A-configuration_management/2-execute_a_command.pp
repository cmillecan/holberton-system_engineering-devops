# Create a manifest that kills a process

exec { 'pkill':
  command => 'pkill killmenow',
  path    => '/usr/bin',
}
