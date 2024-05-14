<?php
namespace environement;

use Dotenv\Dotenv;

require_once dirname(__DIR__) . '/vendor/autoload.php';


$dotenv = Dotenv::createImmutable(dirname(__DIR__));
$dotenv->load();