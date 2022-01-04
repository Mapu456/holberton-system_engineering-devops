# install the package puppet-lint

exec { 'killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
}
