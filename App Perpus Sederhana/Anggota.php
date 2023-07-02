<?php
//Simpanlah dengan nama file : Anggota.php
require_once 'database.php';
class Anggota 
{
    private $db;
    private $table = 'anggota';
    public $kodeanggota = "";
    public $nama = "";
    public $jk = "";
    public $alamat = "";
    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }
    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }
    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function get_by_kodeanggota(int $kodeanggota)
    {
        $query = "SELECT * FROM $this->table WHERE kodeanggota = $kodeanggota";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kodeanggota`,`nama`,`jk`,`alamat`) VALUES ('$this->kodeanggota','$this->nama','$this->jk','$this->alamat')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kodeanggota = '$this->kodeanggota', nama = '$this->nama', jk = '$this->jk', alamat = '$this->alamat' 
        WHERE idanggota = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kodeanggota($kodeanggota): int
    {
        $query = "UPDATE $this->table SET kodeanggota = '$this->kodeanggota', nama = '$this->nama', jk = '$this->jk', alamat = '$this->alamat' 
        WHERE kodeanggota = $kodeanggota";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE idanggota = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kodeanggota($kodeanggota): int
    {
        $query = "DELETE FROM $this->table WHERE kodeanggota = $kodeanggota";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>