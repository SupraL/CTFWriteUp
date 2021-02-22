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