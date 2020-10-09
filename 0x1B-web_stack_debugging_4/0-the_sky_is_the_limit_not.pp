# Task 0
exec { 'limit':
    command => "sed -i 's/15/4000/g' /etc/default/nginx; service nginx restart",
    path    =>['/bin', '/usr/bin', '/usr/sbin']

}
