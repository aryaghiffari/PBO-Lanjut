<?php
//Simpanlah dengan nama file : Buku.php
require_once 'database.php';
class Buku 
{
    private $db;
    private $table = 'buku';
    public $kodebuku = "";
    public $judul = "";
    public $pengarang = "";
    public $penerbit = "";
    public $tahun = "";
    public $kodekategori = "";
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
    public function get_by_kodebuku(int $kodebuku)
    {
        $query = "SELECT * FROM $this->table WHERE kodebuku = $kodebuku";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kodebuku`,`judul`,`pengarang`,`penerbit`,`tahun`,`kodekategori`) VALUES ('$this->kodebuku','$this->judul','$this->pengarang','$this->penerbit','$this->tahun','$this->kodekategori')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kodebuku = '$this->kodebuku', judul = '$this->judul', pengarang = '$this->pengarang', penerbit = '$this->penerbit', tahun = '$this->tahun', kodekategori = '$this->kodekategori' 
        WHERE idbuku = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kodebuku($kodebuku): int
    {
        $query = "UPDATE $this->table SET kodebuku = '$this->kodebuku', judul = '$this->judul', pengarang = '$this->pengarang', penerbit = '$this->penerbit', tahun = '$this->tahun', kodekategori = '$this->kodekategori' 
        WHERE kodebuku = $kodebuku";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE idbuku = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kodebuku($kodebuku): int
    {
        $query = "DELETE FROM $this->table WHERE kodebuku = $kodebuku";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>