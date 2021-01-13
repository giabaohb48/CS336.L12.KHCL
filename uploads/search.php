<!DOCTYPE html>
<html>
<?php
header("Cache-Control: no-store, no-cache, must-revalidate, max-age=0");
header("Cache-Control: post-check=0, pre-check=0", false);
header("Pragma: no-cache");
?>

    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
<head>
	<title>Result</title>
	<style type="text/css">
		body {
            background-color:#d9ecee ;
               
        font-family: 'Montserrat';
		font-weight: bold;
		
			margin-left:8%;
			color: black;
			
		}
	</style>
	
	<link href="https://fonts.googleapis.com/css?family=Rokkitt" rel="stylesheet">
</head>
<body>
	<h2 style="font-size:50px">RESULT</h2><br>
	<h3>Query:</h3>

            <?php
                echo $_POST["searchterm"];
                $myfile = fopen("../uploads/description.txt", "w");
                $term=$_POST["searchterm"];
                fwrite($myfile, $term);
                fclose($myfile);

                $result = exec("C:/Users/DELL/AppData/Local/Microsoft/WindowsApps/python.exe h:/1UNIVERSITY/2020_1/truy_van_thong_tin_da_pt/project/vs_CBIR/TF_IDF_score_finallllll.py");
            ?> 


    <h3>Related Images:</h3>
		<?php
		    		    
			$dirname = "../uploads/matched_images/";
			$images = glob($dirname."*.jpg");
			$inputFile = fopen("../uploads/matched_images_caption.txt", "r");
			$term=$_POST["searchterm"];
			foreach($images as $image) {
					//echo '<img src="'.$image.'" height="250px" hspace="4px" vspace="4px"/>';    
				if (($line = fgets($inputFile)))
				{
									
					echo "<img src=\"" . $image. "\" width='350px' hspace='25px' vspace='4px'>\n";     
					// echo  "$line <br /><br />";
				} 
				else 
				{
					echo "Image '$term' has no metadata";
				} 
			}
			fclose($inputFile);
			 
			
			
		?>


</body>

</html>