<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInit081eeb454663ef9b69f4e4a11cf86fe9
{
    public static $classMap = array (
        'Composer\\InstalledVersions' => __DIR__ . '/..' . '/composer/InstalledVersions.php',
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->classMap = ComposerStaticInit081eeb454663ef9b69f4e4a11cf86fe9::$classMap;

        }, null, ClassLoader::class);
    }
}
