<?php
//Simpanlah dengan nama file : Peminjaman.php
require_once 'database.php';
class Peminjaman 
{
    private $db;
    private $table = 'peminjaman';
    public $nomorbukti = "";
    public $tgl_pinjam = "";
    public $kodeanggota = "";
    public $kodebuku1 = "";
    public $kodebuku2 = "";
    public $tglhrskembali = "";
    public $tgl_dikembalikan = "";
    public $status_pinjam = "";
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
    public function get_by_nomorbukti(int $nomorbukti)
    {
        $query = "SELECT * FROM $this->table WHERE nomorbukti = $nomorbukti";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`nomorbukti`,`tgl_pinjam`,`kodeanggota`,`kodebuku1`,`kodebuku2`,`tglhrskembali`,`tgl_dikembalikan`,`status_pinjam`) VALUES ('$this->nomorbukti','$this->tgl_pinjam','$this->kodeanggota','$this->kodebuku1','$this->kodebuku2','$this->tglhrskembali','$this->tgl_dikembalikan','$this->status_pinjam')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET nomorbukti = '$this->nomorbukti', tgl_pinjam = '$this->tgl_pinjam', kodeanggota = '$this->kodeanggota', kodebuku1 = '$this->kodebuku1', kodebuku2 = '$this->kodebuku2', tglhrskembali = '$this->tglhrskembali', tgl_dikembalikan = '$this->tgl_dikembalikan', status_pinjam = '$this->status_pinjam' 
        WHERE idpeminjaman = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_nomorbukti($nomorbukti): int
    {
        $query = "UPDATE $this->table SET nomorbukti = '$this->nomorbukti', tgl_pinjam = '$this->tgl_pinjam', kodeanggota = '$this->kodeanggota', kodebuku1 = '$this->kodebuku1', kodebuku2 = '$this->kodebuku2', tglhrskembali = '$this->tglhrskembali', tgl_dikembalikan = '$this->tgl_dikembalikan', status_pinjam = '$this->status_pinjam' 
        WHERE nomorbukti = $nomorbukti";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE idpeminjaman = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_nomorbukti($nomorbukti): int
    {
        $query = "DELETE FROM $this->table WHERE nomorbukti = $nomorbukti";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>