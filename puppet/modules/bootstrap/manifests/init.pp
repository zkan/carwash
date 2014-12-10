class bootstrap {
    exec { "apt-get update && apt-get dist-upgrade":
        command => "apt-get update && apt-get dist-upgrade",
        timeout => 0
    }

    $system_packages = [ "build-essential" ]
    package { $system_packages:
        ensure  => installed,
        require => Exec["apt-get update && apt-get dist-upgrade"]
    }

    $dev_tools = [ "git-core", "vim", "curl", "firefox", "xvfb" ]
    package { $dev_tools:
        ensure  => installed,
        require => Exec["apt-get update && apt-get dist-upgrade"]
    }

    $image_libraries = [ "libjpeg62", "libjpeg62-dev", "zlib1g-dev" ]
    package { $image_libraries:
        ensure  => installed,
        require => Exec["apt-get update && apt-get dist-upgrade"]
    }
}
