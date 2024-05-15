<?php

namespace App\Database;

use PDO;

class EventsPdo extends PDO
{
    private string $host = 'mysql';
    private string $db = 'events';
    private $user;
    private $pass;

    public function __construct()
    {
        $this->user = getenv('DB_USER');
        $this->pass = getenv('DB_PASS');

        $dsn = "mysql:host=$this->host;dbname=$this->db";
        $opt = [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false,
        ];

        parent::__construct($dsn, $this->user, $this->pass, $opt);
    }

    public function insertEvent(array $data): void
    {
        $fields = implode(', ', array_keys($data));
        $values = implode(', ', array_fill(0, count($data), '?'));

        $sql = "INSERT INTO event ($fields) VALUES ($values)";

        $stmt = $this->prepare($sql);

        $stmt->execute(array_values($data));

        echo 'Event added successfully';
    }
}