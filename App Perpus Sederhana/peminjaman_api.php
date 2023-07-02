<?php
require_once 'database.php';
require_once 'Peminjaman.php';
$db = new MySQLDatabase();
$peminjaman = new Peminjaman($db);
$id=0;
$nomorbukti=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nomorbukti'])){
            $nomorbukti = $_GET['nomorbukti'];
        }
        if($id>0){    
            $result = $peminjaman->get_by_id($id);
        }elseif($nomorbukti>0){
            $result = $peminjaman->get_by_nomorbukti($nomorbukti);
        } else {
            $result = $peminjaman->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new peminjaman
        $peminjaman->nomorbukti = $_POST['nomorbukti'];
        $peminjaman->tgl_pinjam = $_POST['tgl_pinjam'];
        $peminjaman->kodeanggota = $_POST['kodeanggota'];
        $peminjaman->kodebuku1 = $_POST['kodebuku1'];
        $peminjaman->kodebuku2 = $_POST['kodebuku2'];
        $peminjaman->tglhrskembali = $_POST['tglhrskembali'];
        $peminjaman->tgl_dikembalikan = $_POST['tgl_dikembalikan'];
        $peminjaman->status_pinjam = $_POST['status_pinjam'];
       
        $peminjaman->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'PUT':
        // Update an existing data
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nomorbukti'])){
            $nomorbukti = $_GET['nomorbukti'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $peminjaman->nomorbukti = $_PUT['nomorbukti'];
        $peminjaman->tgl_pinjam = $_PUT['tgl_pinjam'];
        $peminjaman->kodeanggota = $_PUT['kodeanggota'];
        $peminjaman->kodebuku1 = $_PUT['kodebuku1'];
        $peminjaman->kodebuku2 = $_PUT['kodebuku2'];
        $peminjaman->tglhrskembali = $_PUT['tglhrskembali'];
        $peminjaman->tgl_dikembalikan = $_PUT['tgl_dikembalikan'];
        $peminjaman->status_pinjam = $_PUT['status_pinjam'];
        if($id>0){    
            $peminjaman->update($id);
        }elseif($nomorbukti<>""){
            $peminjaman->update_by_nomorbukti($nomorbukti);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nomorbukti'])){
            $nomorbukti = $_GET['nomorbukti'];
        }
        if($id>0){    
            $peminjaman->delete($id);
        }elseif($nomorbukti>0){
            $peminjaman->delete_by_nomorbukti($nomorbukti);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman delete failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
    }
$db->close()
?>