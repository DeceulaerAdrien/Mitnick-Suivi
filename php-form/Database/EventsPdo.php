<?php

namespace App\Database;

use PDO;

class EventsPdo extends PDO
{
    private string $host = 'mysql';
    private string $db = 'event';
    private $user;
    private $pass;

    public function __construct()
    {
        $this->user = $_ENV['DB_USER'];
        $this->pass = $_ENV['DB_PASS'];

        $dsn = "mysql:host=$this->host;dbname=$this->db";

        parent::__construct($dsn, $this->user, $this->pass);
    }

    public function insertEvent(array $data): void
    {
        $fields = implode(', ', array_keys($data));
        $values = implode(', ', array_fill(0, count($data), '?'));

        $sql = "INSERT INTO events ($fields) VALUES ($values)";

        $stmt = $this->prepare($sql);

        $stmt->execute(array_values($data));

        echo 'Event added successfully';
    }
}