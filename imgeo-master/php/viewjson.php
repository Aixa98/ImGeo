<?php
$data = file_get_contents("file:///C:/Users/Usuario/OneDrive/Escritorio/PTec.VENG/ImGeo/imgeo-master/uploads/Greater_London_Const_Region.geojson");
$products = json_decode($data, true);

foreach ($products as $product) {
    echo '<pre>';
    print_r($product);
    echo '</pre>';
}
