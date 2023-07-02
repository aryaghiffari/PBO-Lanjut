<?php
//Simpanlah dengan nama file : Kategori.php
require_once 'database.php';
class Kategori 
{
    private $db;
    private $table = 'kategori';
    public $kode_kategori = "";
    public $nama_kategori = "";
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
    public function get_by_kode_kategori(int $kode_kategori)
    {
        $query = "SELECT * FROM $this->table WHERE kode_kategori = $kode_kategori";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kode_kategori`,`nama_kategori`) VALUES ('$this->kode_kategori','$this->nama_kategori')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kode_kategori = '$this->kode_kategori', nama_kategori = '$this->nama_kategori' 
        WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kode_kategori($kode_kategori): int
    {
        $query = "UPDATE $this->table SET kode_kategori = '$this->kode_kategori', nama_kategori = '$this->nama_kategori' 
        WHERE kode_kategori = $kode_kategori";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kode_kategori($kode_kategori): int
    {
        $query = "DELETE FROM $this->table WHERE kode_kategori = $kode_kategori";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>