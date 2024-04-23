
## Initialization 

```php
$arr = array();
$arr = array("a" => 1, "b" => 2);
$arr = array("x", "y");
$arr = [];
$arr = ["x", "y"];
```

## Accessing and modifying new elements

```php
$arr[] = "somehitng!";
arr["testing"] = "something";
$lenght = count($arr);

// DELETING
unset(arr["hated_value"]);

// JOIN LIKE
implode("delimeter", $arr);
```

## Looping through array

```php
foreach($arr as $key => value) {
	echo $key . "->" . $value;
}

for ($i = 0, $length = count($arr); $i < $length; $i++) {
	echo $arr[$i];
}
```

## Checking for an element in the array

```php
// CHECK FOR A KAY
if (array_key_exists('wanted_key', $arr)) { 
	print "Yes, wanted key exists!"; 
}

// CHECK FOR A VALUE
if (in_array("wanted_value", $arr)) { 
	print "Yes, wanted valueu exists!"; 
}

$wanted_key_if_exists = array_search("giving_value", $arr);
```
