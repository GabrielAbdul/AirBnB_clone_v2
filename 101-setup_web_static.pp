exec {'wget'
    provider => 'shell',
    command  => 'wget https://raw.githubusercontent.com/GabrielAbdul/AirBnB_clone_v2/master/0-setup_web_static.sh && chmod +x 0-setup_web_static.sh && ./0-setup_web_static.sh',
}
