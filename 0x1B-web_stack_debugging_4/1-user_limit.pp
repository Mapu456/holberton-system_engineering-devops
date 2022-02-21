#Change the OS configuration to login with holberton
exec { 'change limits':
    command  =>  'sed -i "s/nofile 5/nofile 65535/" /etc/security/limits.conf',
    provider => 'shell',
}
exec { 'change limits 2':
    command  =>  'sed -i "s/nofile 4/nofile 1024/" /etc/security/limits.conf',
    provider => 'shell',
}
