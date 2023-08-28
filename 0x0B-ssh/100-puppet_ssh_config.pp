# make changes to ssh configuration file
file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "
    Host *
      PubkeyAuthentication yes
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
