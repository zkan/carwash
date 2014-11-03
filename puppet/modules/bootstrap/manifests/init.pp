class bootstrap {
    exec { "apt-get update":
        command => "apt-get update",
        timeout => 0
    }

    $system_packages = [ "build-essential" ]
    package { $system_packages:
        ensure  => "installed",
        require => Exec["apt-get update"]
    }

    $dev_tools = [ "git-core", "vim", "curl", "firefox", "xvfb" ]
    package { $dev_tools:
        ensure  => "installed",
        require => Exec["apt-get update"]
    }

    $image_libraries = [ "libjpeg62", "libjpeg62-dev", "zlib1g-dev" ]
    package { $image_libraries:
        ensure  => "installed",
        require => Exec["apt-get update"]
    }
}
